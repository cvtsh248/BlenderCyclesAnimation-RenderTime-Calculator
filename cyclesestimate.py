import math

mins = raw_input("Input render time for 4 frames (mins): ")
frames = raw_input("Input number of frames: ")
#parsing
mins = mins.split(" ")
mins = [y for x in mins for y in x.split(':')]

fmins = []
for n in range (0, 8, 2):
	fmins.append(float(mins[n])+float(mins[n+1])/60)

#calculation
avg = 0
for i in range (0,len(fmins)):
	avg = avg+float(fmins[i])

avg = avg/len(fmins) #find average render time

minutes = avg*int(frames) #How many minutes

hrs = min/60 #how many hours

frac, whole = math.modf(hrs) #find decimal section of hrs

formathrs = str(int(math.floor(hrs)))+":"+str(int(round(frac*60))) #format number of hours i.e. hrs:mins

#output
print "Estimated total render time (hrs): ", formathrs
print "Estimated total render time (mins): ", minutes

