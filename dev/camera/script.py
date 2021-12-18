from multivision.common import Camera
from multivision.cycles import init_cycles

init_cycles(device='gpu')


cam = Camera("cam")


cam.render("img.png")
