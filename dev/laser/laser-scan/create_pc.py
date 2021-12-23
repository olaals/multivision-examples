import numpy as np
import os
from PIL import Image
import open3d as o3d
from numba import njit

@njit
def project_pixel(pix, t_cl, rx, K_inv, T_wc):
    s = K_inv@pix
    u4 = np.dot(t_cl, rx)
    bot = np.dot(s, rx)
    x = u4/bot*s
    x = np.append(x, 1.0)
    x = x.astype(np.float32)
    x = T_wc@x
    x = x/x[-1]
    x = x[:3]
    return x
    
def load_image(filename):
    img = Image.open(filename)
    img = np.array(img)
    return img




WORK_DIR = "output"
SCAN_DIRS = [os.path.join(WORK_DIR, scan_dir) for scan_dir in os.listdir(WORK_DIR)]
SCAN_DIRS.sort()
print(SCAN_DIRS)
point_clouds = []


for scan_dir in SCAN_DIRS:
    img_path = os.path.join(scan_dir, "scan.png")
    img = load_image(img_path)
    print(img.shape)

    T_cl = np.load(os.path.join(scan_dir, "T_cl.npy")).astype(np.float32)
    T_wc = np.load(os.path.join(scan_dir, "T_wc.npy")).astype(np.float32)
    K = np.load(os.path.join(scan_dir, "K.npy")).astype(np.float32)
    K_inv = np.linalg.inv(K).astype(np.float32)
    transl = T_cl[:3,-1]
    rot = T_cl[:3,:3]

    plane_normal = rot[:3,0]

    points = []

    # loop through pixels in img
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j,0] < 20:
                continue
            pix = np.array([j,i,1], dtype=np.float32)
            x = project_pixel(pix, transl, plane_normal, K_inv, T_wc)
            points.append(x)

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    point_clouds.append(pcd)

o3d.visualization.draw_geometries(point_clouds)
