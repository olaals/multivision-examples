import multivision
from multivision.scanners import LaserScanner
from multivision.common import Camera
from multivision.luxcore import init_luxcore_bidir, LuxcoreLaser
import pickle
import numpy as np
import bpy
import matplotlib.pyplot as plt
import os

init_luxcore_bidir(samples=6, eye_depth=3, light_depth=3)

laser = LuxcoreLaser("cycLaser", lumens=2000, width_angle_deg=0.1, pixels_per_deg=80)
cam = Camera("cam", resolution=(512,512), focal_length=50, sensor_width=36)




baseline = 0.2
angle = 15*3.14/180

settings = pickle.load(open("settings.pkl","rb"))
print(settings)
pose = settings["pose"]
idx = settings["idx"]

scanner = LaserScanner("laserScanner", pose, baseline, angle, cam, laser)

K = scanner.camera.get_camera_matrix()
T_cl = scanner.get_transformation("c->l", "numpy")
T_wc = scanner.camera.axis.get_transf_from_world(True)


print("hie")

bpy.context.view_layer.update()
#bpy.context.scene.update()

out_dir = f'output/scan{format(idx,"02d")}'
os.makedirs(out_dir, exist_ok=True)

img = scanner.camera.render(filename=f'scan.png', directory=out_dir, exposure=-5)
pose_np = pose*1.0
np.save(os.path.join(out_dir, "pose.npy"), pose_np)
np.save(os.path.join(out_dir, "T_cl.npy"), T_cl)
np.save(os.path.join(out_dir, "K.npy"), K)
np.save(os.path.join(out_dir, "T_wc.npy"), T_wc)





