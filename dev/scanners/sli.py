from multivision.scanners import GrayCodeSLIScanner
from multivision.cycles import CyclesProjector, init_cycles
from multivision.common import Camera, delete_all
import bpy

delete_all()
init_cycles(samples=5, device='GPU')
bpy.ops.mesh.primitive_plane_add()
bpy.context.object.scale = [3,3,3]
bpy.ops.mesh.primitive_monkey_add()
bpy.context.object.scale = [0.4,0.4,0.4]
bpy.context.object.rotation_euler = [-3.14/2,0,0]




proj = CyclesProjector("Projector")
cam = Camera("Camera")

sli_pose = ((0,0,2),(0,0,0))
baseline = 0.2
angle = 5*3.14/180

sli_scanner = GrayCodeSLIScanner("sli_scanner",
                                     sli_pose,
                                     baseline,
                                     angle,
                                     cam,
                                     proj)
#sli_scanner.set_gray_code_pattern(4)
sli_scanner.scan_gray_code(4)

