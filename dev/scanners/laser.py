from multivision.scanners import GrayCodeSLIScanner
from multivision.cycles import init_cycles, CyclesLaser
from multivision.common import Camera, delete_all
import bpy
import matplotlib.pyplot as plt

delete_all()
init_cycles(samples=5, device='GPU')
bpy.ops.mesh.primitive_plane_add()
bpy.context.object.scale = [3,3,3]
bpy.ops.mesh.primitive_monkey_add()
bpy.context.object.scale = [0.4,0.4,0.4]
bpy.context.object.rotation_euler = [-3.14/2,0,0]




laser = CyclesLaser("Laser", width_angle_deg=0.15, fan_angle_deg=60, lumens=2000)
cam = Camera("Camera")

scanner_pose = ((0,0,2),(0,0,0))
baseline = 0.2
angle = 5*3.14/180

laser_scanner = GrayCodeSLIScanner("laser_scanner",
                                     scanner_pose,
                                     baseline,
                                     angle,
                                     cam,
                                     laser)


img = laser_scanner.camera.get_image(exposure=-6)
plt.imshow(img)
plt.show()




