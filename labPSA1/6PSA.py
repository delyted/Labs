import random
from PIL import Image
filename = "danger_zone.png"
danger_zone = Image.open(filename)
mined_area = 0
times = int(input())
i = 0
for i in range(times):
    x = random.randint(0, 3199)
    y = random.randint(0, 1529)
    coordinates = x, y
    color = danger_zone.getpixel(coordinates)
    if color == (255, 0, 0, 255):
        mined_area += 1

print("The mined area is", (mined_area/times)*42, "square miles")
