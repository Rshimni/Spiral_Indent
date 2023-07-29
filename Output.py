import os
from math import *


def abaqus_sketch(nodes):
    inner = [c for c in nodes[0]]
    outer = [c for c in nodes[1]]

    heading = '''from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=50.0)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)\n'''
    with open(f"./Abaqus_script/sketch.py", mode='w+') as file:
        file.write(heading)
        file.write(f"curve_1 = (")
        for _ in inner:
            file.write(f"({round(_[0], 5)}, {round(_[1], 5)}),\n")
        file.write(f")\ncurve_2 = (")
        for _ in outer:
            file.write(f"({round(_[0], 5)}, {round(_[1], 5)}),\n")
        file.write(f")\ns.Spline(points=(curve_1))\n")
        file.write(f"s.Spline(points=(curve_2))\n")
        # file.write(f"s.Line(point1={inner[0]}, point2={outer[0]})\n")
        file.write(f"s.Line(point1={inner[-1]}, point2={outer[-1]})\n")
        file.write(
            f"mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type=DEFORMABLE_BODY)\n")
        file.write(
            f"mdb.models['Model-1'].parts['Part-1'].BaseSolidExtrude(depth=20.0, sketch=s)\n")
        file.write(f"p = mdb.models['Model-1'].parts['Part-1']\n")
        file.write(f"del mdb.models['Model-1'].sketches['__profile__']\n")


def properties(log):
    with open(f"information.txt", mode='w') as file:
        for key, value in log.items():
            file.write(f"{key}:{value}\n")


def abaqus_sketch2(nodes):

    inner = [(c[0], c[1]) for c in nodes]
    outer = [(c[2], c[3]) for c in nodes]

    heading = '''from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=50.0)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)\n'''
    with open(f"sketch2.py", mode='w') as file:
        file.write(heading)
        file.write(f"curve_1 = (")
        for _ in inner:
            file.write(f"({round(_[0], 5)}, {round(_[1], 5)}),\n")
        file.write(f")\ncurve_2 = (")
        for _ in outer:
            file.write(f"({round(_[0], 5)}, {round(_[1], 5)}),\n")
        file.write(f")\ns.Spline(points=(curve_1))\n")
        file.write(f"s.Spline(points=(curve_2))\n")
        file.write(f"s.Line(point1={inner[0]}, point2={outer[0]})\n")
        file.write(f"s.Line(point1={inner[-1]}, point2={outer[-1]})\n")
        file.write(
            f"mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type=DEFORMABLE_BODY)\n")
        file.write(
            f"mdb.models['Model-1'].parts['Part-1'].BaseSolidExtrude(depth=20.0, sketch=s)\n")
        file.write(f"p = mdb.models['Model-1'].parts['Part-1']\n")
        file.write(f"del mdb.models['Model-1'].sketches['__profile__']\n")
