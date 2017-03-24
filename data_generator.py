from random import randint
def gen_time():
    hr = randint(10,24)
    min = randint(10,59)
    return ":".join([str(hr),str(min)])

f_no = ("1210","8512","8655")
arr = ("12:10","20:23","15:43")
dep = ("14:20","23:12","19:55")
delay = 0
dest = ("Mumbai","Delhi","Raipur")
src = ("Nagpur","Kolkata","Banglore")
d = {0:(f_no[0],src[0],dest[0],arr[0],dep[0]),1:(f_no[1],src[1],dest[1],arr[1],dep[1]),2:(f_no[2],src[2],dest[2],arr[2],dep[2])}
f = file("Data.csv","w")
f.write(",".join(("FLIGHTNO","SRC","DES","DEP","ARR","DELAY",)))
f.write("\n")
for i in xrange(150):
    dep = gen_time()
    arr = gen_time()
    while dep[:2]<arr[:2]:
        dep = gen_time()
        arr = gen_time()
    f.write(",".join((",".join((d[randint(0,2)])),str(randint(-15,150)))))
    f.write("\n")
f.close()
