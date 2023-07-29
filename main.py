from Spirals import *
from Division import *
from Roughness import *
from Coordinates import *
from Plot import *
from Output import *
# ########################################### Geometry Parameters ################################################## #
start_angle = 360
angle_step = 1
end_angle = 1080
b_rat = 2.5
ratio = b_rat / pi
divides = 138
roughness_amp = 0.4
offset = 1.5
inform = {"start_angle": start_angle, "angle_step": angle_step, "end_angle": end_angle, "ratio": ratio,
          "divide": divides, "spiral": "archimedean", "roughness_amp": roughness_amp, "thickness": offset}

data = archimedean_spiral(r=ratio, theta_1=start_angle, step=angle_step, theta_2=end_angle, dis=offset)
# abaqus_sketch2(nodes=data)
dd = total_length(data)

print(f"total length:{dd}")

seg = segmentation(divide=divides+1, length=dd, points=data)

plot_cord = rotate(delta=slope(coord=seg), amp=roughness_amp, coord=seg)

xy_coord = spiral_nodes(nodes=plot_cord, dis=offset, b=ratio)
plot_coord(nodes=xy_coord, head="archimedean", dis=offset)
abaqus_sketch(nodes=xy_coord)
properties(log=inform)
print(f"total nodes inner: {len(plot_cord[0])}")
print(f"total nodes outer: {len(plot_cord[3])}")

