import copy

class Node:
	def __init__(self, abs, ord, kanan, kiri, atas, bawah):
		self.absis = abs
		self.ordinat = ord
		self.kanan = kanan
		self.kiri = kiri
		self.atas = atas
		self.bawah = bawah

class Maze:
	def __init__(self):

		self.matrmaze = []
		self.curweight = 0;
		self.namafile = "mazetc.txt"
		with open(self.namafile, "r") as f:
			content = f.readlines()
		#print(content)
		for x in content:
			strinp = []
			for k in x:
				if(k != '\n'):
					strinp.append(k)
			self.matrmaze.append(strinp)
		#print(self.matrmaze)
		print("1 = manual input, 2 = let scan") 
		pilihan = input()
		if(pilihan == '1'):
			print("INPUT POINT ENTRY DAN EXIT MAZE")
			inp = input().split(' ')
			self.entry = (int(inp[0]), int(inp[1]))
			inp = input().split(' ')
			self.exit = (int(inp[0]), int(inp[1]))
		else:
			for x in range(len(self.matrmaze) - 1):
				if(self.matrmaze[x][0] == '0'):
					self.entry = (x, 0)
			for x in range(len(self.matrmaze) - 1):
				if(self.matrmaze[x][len(self.matrmaze) - 1] == '0'):
					self.exit = (x, len(self.matrmaze) - 1)
		self.baris = len(self.matrmaze)
		self.kolom = len(self.matrmaze[0])
		self.expanded = []
		self.steps = []
		self.edges = []
		self.been = []
		self.permasteps = []
		self.matrmaze[self.entry[0]][self.entry[1]] = '3'
		self.matrmaze[self.exit[0]][self.exit[1]] = '0'
		for x in range(self.baris):
			for y in range(self.kolom):
				kanan = False
				kiri = False
				atas = False
				bawah = False
				if(self.matrmaze[x][y] == '0') and (x != self.exit[0] or y != self.exit[1]):
					if(self.matrmaze[x- 1][y] == '0'):
						atas = True
					if(self.matrmaze[x][y - 1] == '0'):
						kiri = True
					if(self.matrmaze[x + 1][y] == '0'):
						bawah = True
					if(self.matrmaze[x][y + 1] == '0'):
						kanan = True
					obj = Node(x,y,kanan,kiri,atas,bawah)
					self.edges.append(obj)
		f.close()
	
	def expandinit(self):
		'''
		1 = atas
		2 = bawah
		3 = kiri
		4 = kanan
		'''
		entryx = self.entry[0]
		entryy = self.entry[1]
		if(self.entry[0] == 0):
			entryx = 1
			self.steps.append(2)
		if(self.entry[1] == 0):
			entryy = 1
			self.steps.append(4)
		if(self.entry[0] == self.baris - 1):
			entryx = entry[0] - 1
			self.steps.append(1)
		if(self.entry[1] == self.kolom - 1):
			entryy = entry[1] - 1
			self.steps.append(3)
		self.expanded = [entryx, entryy]
		self.matrmaze[self.entry[0]][self.entry[1]] = '2'
		self.been.append((self.entry[0], self.entry[1]))
		self.expand()

	def expand(self):
		tempb = self.expanded[0]
		tempk = self.expanded[1]
		self.been.append((self.expanded[0], self.expanded[1]))
		if(self.expanded[0] == self.exit[0] and self.expanded[1] == self.exit[1]):
			print("Solution Found")
			self.permasteps = copy.copy(self.steps)
			print(self.permasteps)
			return()
		for x in self.edges:
			if x.absis == self.expanded[0] and x.ordinat == self.expanded[1]:
				if(x.bawah):
					if((tempb+1, tempk) not in self.been):
						self.expanded[0] = self.expanded[0]+1;
						self.steps.append(2)
						#print("bawah")
						self.expand()
						self.steps.pop()
						self.expanded[0] = tempb
						self.expanded[1] = tempk
				if(x.atas):
					if((tempb-1, tempk) not in self.been):
						self.expanded[0] = self.expanded[0]-1
						self.steps.append(1)
						#print("atas")
						self.expand()
						self.steps.pop()
						self.expanded[0] = tempb
						self.expanded[1] = tempk				
				if(x.kanan):
					if((tempb, tempk+1) not in self.been):
						self.expanded[1] = self.expanded[1]+1
						self.steps.append(4)
						#print("kanan")
						self.expand()
						self.steps.pop()
						self.expanded[0] = tempb
						self.expanded[1] = tempk
				if(x.kiri):
					if((tempb, tempk-1) not in self.been):
						self.expanded[1] = self.expanded[1] -1
						self.steps.append(3)
						#print("kiri")
						self.expand()
						self.steps.pop()
						self.expanded[0] = tempb
						self.expanded[1] = tempk
	def printmaze(self):
		for x in self.matrmaze:
			print(''.join(x))

	def printmaze2(self):
		for x in self.matrmaze:
			print(''.join(x))
		#print(self.curweight)

	def travmaze(self):
		self.expanded[0] = self.entry[0]
		self.expanded[1] = self.entry[1]
		for x in self.permasteps:
			if(x == 1):
				self.expanded[0] = self.expanded[0] - 1
				self.matrmaze[self.expanded[0]][self.expanded[1]] = 'X'
			if(x == 2):
				self.expanded[0] = self.expanded[0] + 1
				self.matrmaze[self.expanded[0]][self.expanded[1]] = 'X'
			if(x == 3):
				self.expanded[1] = self.expanded[1] - 1
				self.matrmaze[self.expanded[0]][self.expanded[1]] = 'X'
			if(x == 4):
				self.expanded[1] = self.expanded[1] + 1
				self.matrmaze[self.expanded[0]][self.expanded[1]] = 'X'

	def bintanginit(self):
		'''
		1 = atas
		2 = bawah
		3 = kiri
		4 = kanan
		'''
		entryx = self.entry[0]
		entryy = self.entry[1]
		if(self.entry[0] == 0):
			entryx = 1
			self.steps.append(2)
		if(self.entry[1] == 0):
			entryy = 1
			self.steps.append(4)
		if(self.entry[0] == self.baris - 1):
			entryx = entry[0] - 1
			self.steps.append(1)
		if(self.entry[1] == self.kolom - 1):
			entryy = entry[1] - 1
			self.steps.append(3)
		self.expanded = [entryx, entryy]
		self.matrmaze[self.entry[0]][self.entry[1]] = '2'
		self.been.append((self.entry[0], self.entry[1]))
		self.bintang(1)

	def bintang(self, prevweight):
		tempb = self.expanded[0]
		tempk = self.expanded[1]
		weight = prevweight
		self.been.append((self.expanded[0], self.expanded[1]))
		if(self.expanded[0] == self.exit[0] and self.expanded[1] == self.exit[1]):
			print("Solution Found")
			self.permasteps = copy.copy(self.steps)
			#print(self.permasteps)
			return()
		for x in self.edges:
			if x.absis == self.expanded[0] and x.ordinat == self.expanded[1]:
				wbawah = (weight + self.exit[0] - tempb + self.exit[1] - tempk + 1, 2)
				watas = (weight + self.exit[0] - tempb + self.exit[1] - tempk - 1, 1)
				wkanan = (weight + self.exit[0] - tempb + self.exit[1] - tempk + 1, 4)
				wkiri = (weight + self.exit[0] - tempb + self.exit[1] - tempk - 1, 3)
				listw = [wbawah, watas, wkanan, wkiri]
				listw.sort(key = lambda x: x[0])
				for y in listw:
					if(x.bawah and y[1] == 2):
						if((tempb+1, tempk) not in self.been):
							self.expanded[0] = self.expanded[0]+1;
							self.steps.append(2)
							self.curweight = y[0]
							self.bintang(self.curweight)
							self.steps.pop()
							self.expanded[0] = tempb
							self.expanded[1] = tempk
					if(x.atas and y[1] == 1):
						if((tempb-1, tempk) not in self.been):
							self.expanded[0] = self.expanded[0]-1
							self.steps.append(1)
							self.curweight = y[0]
							self.bintang(self.curweight)
							self.steps.pop()
							self.expanded[0] = tempb
							self.expanded[1] = tempk				
					if(x.kanan and y[1] == 4):
						if((tempb, tempk+1) not in self.been):
							self.expanded[1] = self.expanded[1]+1
							self.steps.append(4)
							self.curweight = y[0]
							self.bintang(self.curweight)
							self.steps.pop()
							self.expanded[0] = tempb
							self.expanded[1] = tempk
					if(x.kiri and y[1] == 3):
						if((tempb, tempk-1) not in self.been):
							self.expanded[1] = self.expanded[1] -1
							self.steps.append(3)
							self.curweight = y[0]
							self.bintang(self.curweight)
							self.steps.pop()
							self.expanded[0] = tempb
							self.expanded[1] = tempk



def main():
	maz = Maze()
	print("SELECT THE PATHFINDING ALGORITHM")
	print("1 : DFS")
	print("2 : A*")
	inp = input()
	if(inp == '1'):
		maz.expandinit()
	else:
		maz.bintanginit()
	'''for x in maz.edges:
		if x.absis == 9 and x.ordinat == 5:
			print("found")
			print(x.atas)
			print(x.bawah)
			print(x.kiri)
			print(x.kanan)
	'''
	maz.travmaze()
	#print(maz.permasteps)
	maz.printmaze()
main()