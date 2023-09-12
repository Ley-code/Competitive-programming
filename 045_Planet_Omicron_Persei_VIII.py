import math
force,mass,distance = map(int,(input() for i in range(3)))
print("It will take the object "+ str(round(math.sqrt((2*distance)/(force/mass)),1)) +" seconds to fall "+ str(float(distance))+" meters")