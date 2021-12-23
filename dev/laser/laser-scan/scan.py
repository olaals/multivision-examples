from spatialmath import *
import spatialmath.base.transforms3d as tf3
import numpy as np
import pickle
import os
import time

NUM_IMAGES = 50

settings = {}

start = SE3(0.5,0.4,0.4)@SE3.Rz(180, 'deg')@SE3.Rx(45, 'deg')
end = SE3(-0.5,0.4,0.4)@SE3.Rz(180, 'deg')@SE3.Rx(45, 'deg')


interp = np.linspace(0,1,NUM_IMAGES)




for idx,s in enumerate(interp):
    print(idx,s)
    mid = tf3.trinterp(start=start*1.0,end=end*1.0, s=s)
    settings["pose"] = mid
    settings["idx"] = idx
    
    pickle.dump(settings, open("settings.pkl", "wb"))
    time.sleep(0.2)
    os.system("~/library/blender283/blender --background scene.blend --python script.py")



