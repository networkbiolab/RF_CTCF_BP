#c.villaman@gmail.com
#Usage: python matrixmaker.py <fimo bed> <second bed> <window size> <bin size> <prefix>

from sys import argv
import subprocess

bedposlist = []

with open(argv[1]) as f1:
	tempbed = open('temp1.bed', 'w')
	for f in f1:
		winsize = int(argv[3])
		binsize = int(argv[4])
		splitfirst = f.strip().split()
		bedposname=splitfirst[0]+":"+splitfirst[1]+"-"+splitfirst[2]+splitfirst[3]
		bedposlist.append(bedposname)
		middlepoint = int((int(splitfirst[1])+int(splitfirst[2]))/2)
		backpoint = middlepoint - int(binsize/2)
		frontpoint = middlepoint + int(binsize/2)
		numbins = int(winsize/binsize)-1
		startpoint = backpoint-(numbins*binsize)
		endpoint = frontpoint+(numbins*binsize)
		if bedposname[-1] == "+":
			countrange = 0
			for pos in range(startpoint,backpoint,binsize):
				print (splitfirst[0]+"	"+str(pos)+"	"+str(pos+binsize-1), file=tempbed)
				countrange += 1
			print (splitfirst[0]+"	"+str(backpoint)+"	"+str(frontpoint-1), file=tempbed)
			countrange += 1
			for pos in range(frontpoint,endpoint,binsize):
				print (splitfirst[0]+"	"+str(pos)+"	"+str(pos+binsize-1), file=tempbed)
				countrange += 1
		else:
			countrange = 0
			for pos in reversed(range(frontpoint,endpoint,binsize)):
				print (splitfirst[0]+"	"+str(pos)+"	"+str(pos+binsize-1), file=tempbed)
				countrange += 1
			print (splitfirst[0]+"	"+str(backpoint)+"	"+str(frontpoint-1), file=tempbed)
			countrange += 1
			for pos in reversed(range(startpoint,backpoint,binsize)):
				print (splitfirst[0]+"	"+str(pos)+"	"+str(pos+binsize-1), file=tempbed)
				countrange += 1
	tempbed.close()

outputintersect = open("temp2.bed", "w")
bedlist = subprocess.run(["intersectBed","-a","temp1.bed","-b",argv[2],"-c"],stdout=outputintersect)
outputintersect.close()

outputtable = open("temp2.bed", "r")
newbedlist = outputtable.readlines()

outputhing = str(argv[-1])+".txt"
outputname = open(outputhing, "w")

prefix = argv[-1]
winsize = int(argv[3])
binsize = int(argv[4])
startpoint = winsize-binsize

print("pos", end="	",file=outputname)
for i in range(-startpoint,0,binsize):
	print(prefix+"."+str(i), end="	",file=outputname)
for i in range(0,winsize,binsize):
	print(prefix+"."+str(i), end="	",file=outputname)
print("",file=outputname)

for i in bedposlist:
	print(i,end="	",file=outputname)
	breaker = countrange
	while(int(breaker>0)):
		ii = newbedlist.pop(0)
		ctcfvalue = int(ii.strip().split()[-1])
		if ctcfvalue > 1:
			ctcfvalue = 1		
		print(str(ctcfvalue),end="	",file=outputname)
		breaker -= 1
	print("",file=outputname)

outputtable.close()
outputname.close()

subprocess.call(["rm","-rf","temp1.bed"])
subprocess.call(["rm","-rf","temp2.bed"])
