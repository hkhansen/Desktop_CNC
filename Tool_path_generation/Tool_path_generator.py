import math
import matplotlib.pyplot as plt


lines = []

def hole(pos_x, pos_y, rad):
    drill = 3.175
    stepSize = 0.1
    
    x = []
    y = []
    
    r = 0
    while (r + drill/2 < rad):
        t = 0
        while t <= 2 * math.pi:
            x.append(r * math.cos(t) + pos_x )
            y.append(r * math.sin(t) + pos_y)
            t += stepSize
        r += stepSize
    
    return (x,y)
    
def rectangle(pos_x, pos_y, length, width):
    x = []
    y = []
    # start position
    x.append(pos_x)
    y.append(pos_y)
    # notch for bed screws
    x.append(pos_x)
    y.append(pos_y+50)
    x.append(pos_x+5)
    y.append(pos_y+50)
    x.append(pos_x+5)
    y.append(pos_y+60)
    x.append(pos_x)
    y.append(pos_y+60)
    x.append(pos_x)
    y.append(pos_y + length)
    # notch for bed screws
    x.append(pos_x)
    y.append(pos_y+60)
    x.append(pos_x+5)
    y.append(pos_y+60)
    x.append(pos_x+5)
    y.append(pos_y+50)
    x.append(pos_x)
    y.append(pos_y+50)
    # Back to start
    x.append(pos_x)
    y.append(pos_y)
    x.append(pos_x + width)
    y.append(pos_y)
    x.append(pos_x + width)
    y.append(pos_y + length)
    x.append(pos_x + width)
    y.append(pos_y)
    x.append(pos_x)
    y.append(pos_y)
    
    return (x,y)


def generate_gcode(x, y, z, feedrate):
    lines.append("G21\n")
    lines.append("G90\n")
    string = "G1 X" + str(x[0]) + " Y" + str(y[0]) + " Z1 F250\n"
    lines.append(string)
    for i in range(0, -z*10, -1):
        string = "G1 Z" + str(i/10) + " F250\n"
        lines.append(string)
        for j in range(len(x)):
            string = "G1 X" + str(x[j]) + " Y" + str(y[j]) + " F" + str(feedrate) + "\n"
            lines.append(string)
    lines.append("G1 Z1 F250\n")

x,y = rectangle(0, 0, 200, 40)
plt.plot(x,y)
#generate_gcode(x, y, 8, 500)
x,y = hole(10, 10, 6)
plt.plot(x,y)
generate_gcode(x, y, 8, 500)
x,y = hole(30, 10, 6)
plt.plot(x,y)
generate_gcode(x, y, 8, 500)
x,y = hole(10, 74.5, 8)
plt.plot(x,y)
generate_gcode(x, y, 8, 500)


file = open("Tool_path.gcode", "w")
file.writelines(lines)
hole(10, 10, 6)

#rectangle(0, 0, 200, 40)
#hole(10, 10, 6)
#hole(30, 10, 6)
#hole(10, 74.5, 8)
#hole(20, 160, 16)

plt.xlim([-5, 200])
plt.ylim([-5, 200])
plt.show()  