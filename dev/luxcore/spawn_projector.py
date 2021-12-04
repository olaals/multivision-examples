import bpy
import multivision as mv
from multivision.luxcore import LuxcoreProjector, init_luxcore
from multivision.common import Camera, delete_all

delete_all()
init_luxcore()

bpy.ops.mesh.primitive_plane_add()

luxcore_proj = LuxcoreProjector(pose=((0,0,3),(0,0,0)))