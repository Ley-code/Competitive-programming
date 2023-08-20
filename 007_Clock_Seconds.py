time = []
for i in range(3):
    time.append(int(input()))
am_or_pm = input()
t_seconds = 0
if am_or_pm == "AM":
    if time[0] == 12:
        t_seconds = 24*3600
    else:
        t_seconds=(time[0]*3600) + (time[1]*60) +(time[2])
else:
    if time[0] == 12:
        t_seconds = 12*3600
    else:
        t_seconds = (12*3600) + (time[0]*3600) + (time[1]*60) +(time[2])
print(t_seconds)