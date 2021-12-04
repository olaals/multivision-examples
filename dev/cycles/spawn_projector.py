import bpy
import multivision as mv
from multivision.cycles import CyclesProjector, init_cycles
from multivision.common import Camera, delete_all

delete_all()
init_cycles()

bpy.ops.mesh.primitive_plane_add()

cycles_proj = CyclesProjector(pose=((0,0,3),(0,0,0)))


