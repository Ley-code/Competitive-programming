import math
values = []
for i in range(6):
    values.append(input())
t1,t2,t3,r1,r2,r3 = map(int,values)
l1= math.log1p(float(r1))
l2 = math.log1p(float(r2))
l3 = math.log1p(float(r3))
y1 = 1/(float(t1))
y2 = 1/(float(t2))
y3 = 1/(float(t3))
gamma2 = float(y2-y1)/(l2-l1)
gamma3 = float(y3 - y1)/(l3-l1)
c = ((gamma3-gamma2)/(l3-l2)) * (1/(l1+l2+l3))
b = gamma2-(c*(pow(l1,2)+(l1*l2)+pow(l2,2)))
print(y1-(l1*(b+pow(l1,2)*c)))