import multivision as mv
from multivision.cycles import CyclesProjector, init_cycles
from multivision.common import Camera, delete_all
from multivision.templates import TemplateScanner
import spatialmath as sm
from scipy.spatial.transform import Rotation as R
import bpy

delete_all()
init_cycles()
bpy.ops.mesh.primitive_plane_add(scale=[3,3,3])

t1 = ((0.3,0,0), R.from_euler('xyz', [0,0.1,0]))
t2 = ((-0.3,0,0), R.from_euler('xyz', [0,-0.1,0]))
proj = CyclesProjector("cycProj")
cam = Camera("cam")
sc_dict = {
    "camera":{
        "object":cam,
        "short":"c",
        "transform":t1,
    },
    "proj":{
        "object":proj,
        "short":"p",
        "transform":t2
    }
}
ts = TemplateScanner("sfd", sc_dict, pose=((0,0,3), (0,0,0) ))