import multivision
from multivision.scanners import LaserScanner
from multivision.common import Camera
from multivision.luxcore import init_luxcore, LuxcoreLaser
from spatialmath import *
import spatialmath.base.transforms3d as tf3
import numpy as np
import bpy
init_luxcore(render_time=3, path_trace_depth=4, device='gpu')

laser = LuxcoreLaser("cycLaser", lumens=2000, width_angle_deg=0.1, pixels_per_deg=80)
cam = Camera("cam", resolution=(512,512), focal_length=50, sensor_width=36)




baseline = 0.2
angle = 15*3.14/180

start = SE3(1,0.4,0.4)@SE3.Rz(180, 'deg')@SE3.Rx(45, 'deg')
end = SE3(-1,0.4,0.4)@SE3.Rz(180, 'deg')
mid = tf3.trinterp(start=start*1.0,end=end*1.0, s=0.5)
print(mid)

scanner = LaserScanner("laserScanner", start, baseline, angle, cam, laser)

print("hie")

bpy.context.view_layer.update()
#bpy.context.scene.update()

scanner.camera.get_image(exposure=-5)



