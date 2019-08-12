import random

class team:
	def __init__(self, name, id, odds):
		
		self.name = name
		self.id = id
		self.odds = odds
		self.numbers = []
		self.order = 0
	def printInfo(self):
		print "Team: %s\nID: %d\nOdds: %d\nNumbers: %ls" % (self.name, self.id, self.odds, self.numbers)
	
	def buildBalls(self, array):
		i=0
		while i < self.odds and array:
			x=(random.choice(array))
			self.numbers.append(x)
			array.remove(x)
			i+=1
		self.numbers.sort()


def lotto(array, orderList, remaining):
	i=1
	while i < 4:
		choice = random.choice(array)
		
		if choice in phx.numbers:
			phx.order = i
			orderList.append("%d. PHX" % (i))
			remaining.remove("PHX")
			for x in phx.numbers:
				array.remove(x)
		elif choice in mem.numbers:
			mem.order = i
			orderList.append("%d. MEM" % (i))
			remaining.remove("MEM")
			for x in mem.numbers:
				array.remove(x)
		elif choice in atl.numbers:
			atl.order = i
			orderList.append("%d. ATL" % (i))
			remaining.remove("ATL")
			for x in atl.numbers:
				array.remove(x)
		elif choice in chi.numbers:
			chi.order = i
			orderList.append("%d. CHI" % (i))
			remaining.remove("CHI")
			for x in chi.numbers:
				array.remove(x)
		elif choice in orl.numbers:
			orl.order = i
			orderList.append("%d. ORL" % (i))
			remaining.remove("ORL")
			for x in orl.numbers:
				array.remove(x)
		elif choice in nyk.numbers:
			nyk.order = i
			orderList.append("%d. NYK" % (i))
			remaining.remove("NYK")
			for x in nyk.numbers:
				array.remove(x)
		elif choice in sac.numbers:
			sac.order = i
			if i != 1:
				orderList.append("%d. BOS (From SAC)" % (i))
			elif i == 1:
				orderList.append("%d. SAC" % (i))
			remaining.remove("SAC")
			for x in sac.numbers:
				array.remove(x)
		elif choice in brk.numbers:
			brk.order = i
			orderList.append("%d. BRK" % (i))
			remaining.remove("BRK")
			for x in brk.numbers:
				array.remove(x)
		elif choice in dal.numbers:
			dal.order = i
			orderList.append("%d. DAL" % (i))
			remaining.remove("DAL")
			for x in dal.numbers:
				array.remove(x)
		elif choice in lal.numbers:
			lal.order = i
			orderList.append("%d. LAL" % (i))
			remaining.remove("LAL")
			for x in lal.numbers:
				array.remove(x)
		elif choice in cha.numbers:
			cha.order = i
			orderList.append("%d. CHA" % (i))
			remaining.remove("CHA")
			for x in cha.numbers:
				array.remove(x)
		elif choice in cle.numbers:
			cle.order = i
			orderList.append("%d. CLE" % (i))
			remaining.remove("CLE")
			for x in cle.numbers:
				array.remove(x)
		elif choice in lac.numbers:
			lac.order = i
			orderList.append("%d. LAC" % (i))
			remaining.remove("LAC")
			for x in lac.numbers:
				array.remove(x)
		elif choice in min.numbers:
			min.order = i
			orderList.append("%d. MIN" % (i))
			remaining.remove("MIN")
			for x in min.numbers:
				array.remove(x)
		else:
			print "Something Wrong"
		i+=1

def fillOutList(orderList, remaining):
	i=0
	while i <= 10:
		if i > 7 and remaining[i] == "CLE":
			orderList.append("%d. ATL (From CLE)" % (i+4))
		elif i > 2 and remaining[i] == "DAL":
			orderList.append("%d. ATL (From DAL)" % (i+4))
		elif remaining[i] == "SAC":
			orderList.append("%d. BOS (From SAC)" % (i+4))
		else:
			orderList.append("%d. %s" % (i+4, remaining[i]))
		i+=1


def printOrder(orderList):
	for x in orderList:
		print x

def buildArray(numArray):
	for i in range(1,1001):
		numArray.append(i)

def allTeamsBalls(numArray):
	phx.buildBalls(numArray)
	mem.buildBalls(numArray)
	atl.buildBalls(numArray)
	chi.buildBalls(numArray)
	orl.buildBalls(numArray)
	nyk.buildBalls(numArray)
	sac.buildBalls(numArray)
	brk.buildBalls(numArray)
	dal.buildBalls(numArray)
	lal.buildBalls(numArray)
	cha.buildBalls(numArray)
	cle.buildBalls(numArray)
	lac.buildBalls(numArray)
	min.buildBalls(numArray)

#Initialize
phx = team('Phoenix Suns', 0, 140)
chi = team('Chicago Bulls', 1, 140)
atl = team('Atlanta Hawks', 2, 140)
cle = team('Cleveland Cavaliers', 3, 125)
orl = team('Orlando Magic', 4, 105)
nyk = team('New York Knicks', 5, 90)
sac = team('Sacramento Kings', 6, 75)
brk = team('Brooklyn Nets', 7, 60)
mem = team('Memphis Grizzlies', 8, 45)
cha = team('Charlotte Hornets', 9, 30)
dal = team('Dallas Mavericks', 10, 20)
lac = team('Los Angeles Clippers', 11, 15)
min = team('Minnesota Timberwolves', 12, 10)
lal = team('Los Angeles Lakers', 13, 5)
numArray = []
orderList = []
remaining = ["PHX","CHI","ATL","CLE","ORL","NYK","SAC","BRK","MEM","CHA","DAL","LAC","MIN","LAL"]