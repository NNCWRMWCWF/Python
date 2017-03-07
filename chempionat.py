import random

l = ["Zenit", "Spartak", "Tom'", "CSKA", "Rostov", "Rubin", "Terek", "Dinamo"]
dic = {}
def go(a,d):
	s = set(a)
	win = set()
	st = len(s)//2
	for i in range(st):
		team1 = s.pop()
		team2 = s.pop()
		while True :
			point1 = random.randint(0,5)
			point2 = random.randint(0,5)
			if point1 != point2:
				break
		win.add(team1) if point1 > point2 else win.add(team2)
		if len(s) == 0 and len(win) == 1:
			d[("final", team1)] = [team2, ""+str(point1)+"-"+str(point2)]
			d[("final", team2)] = [team1, ""+str(point2)+"-"+str(point1)]
		else:
			d[("1/"+str(st), team1)] = [team2, ""+str(point1)+"-"+str(point2)]
			d[("1/"+str(st), team2)] = [team1, ""+str(point2)+"-"+str(point1)]
	return d if len(win) == 1 else go(list(win),d)	
	
def inform(s,d):
	for key, value in d.items():
		if key[1] == s:
			print(key[0]+":"+key[1]+"-"+value[0]+":"+value[1])
go(l,dic)
inform("Spartak", dic)
#inform("Zenit", dic)
#inform("Tom'", dic)
#inform("CSKA", dic)
#inform("Rostov", dic)
#inform("Rubin", dic)
#inform("Terek", dic)
inform("Dinamo", dic)

