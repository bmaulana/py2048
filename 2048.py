from random import randint

class Board:
	
	def __init__(self):
		self.table = [[0] * 4 for _ in range(4)]
		self.score = 0
		self.won = False

	def display(self):
		print("Score: {0}" .format(self.score))
		for row in self.table:
			print(row)

	def zeroExists(self):
		for row in self.table:
			for cell in row:
				if cell == 0:
					return True

	def insert(self):	
		if self.zeroExists():
			col = randint(0,3)
			row = randint(0,3)
			if self.table[row][col] == 0:
				self.table[row][col] = 2
			else:
				self.insert()

	def isMoveValid(self,move):
		if move == 'W' or move == 'w':
			return self.checkMoveUp()
		elif move == 'A' or move == 'a':
			return self.checkMoveLeft()
		elif move == 'S' or move == 's':
			return self.checkMoveDown()
		elif move == 'D' or move == 'd':
			return self.checkMoveRight()

	def moveBoard(self,dir):
		if move == 'W' or move == 'w':
			self.moveUp()
		elif move == 'A' or move == 'a':
			self.moveLeft()
		elif move == 'S' or move == 's':
			self.moveDown()
		elif move == 'D' or move == 'd':
			self.moveRight()

	def checkMoveUp(self):
		for row in range(1,4):
			for col in range(4):
				if self.table[row][col] != 0 and (self.table[row-1][col] == 0 or self.table[row-1][col] == self.table[row][col]):
					return True

	def moveUp(self):
		for col in range(4):
			n = 0
			for row in range(4):
				m = row
				while m > n:
					if self.table[m-1][col] == 0:
						self.table[m-1][col] = self.table[m][col]
						self.table[m][col] = 0
					elif self.table[m-1][col] == self.table[m][col]:
						self.table[m-1][col] *= 2
						self.table[m][col] = 0
						self.score += self.table[m-1][col]
						n += 1
						break
					m -= 1

	def checkMoveLeft(self):
		for row in range(4):
			for col in range(1,4):
				if self.table[row][col] != 0 and (self.table[row][col-1] == 0 or self.table[row][col-1] == self.table[row][col]):
					return True

	def moveLeft(self):
		for row in range(4):
			n = 0
			for col in range(4):
				m = col
				while m > n:
					if self.table[row][m-1] == 0:
						self.table[row][m-1] = self.table[row][m]
						self.table[row][m] = 0
					elif self.table[row][m-1] == self.table[row][m]:
						self.table[row][m-1] *= 2
						self.table[row][m] = 0
						self.score += self.table[row][m-1]
						n += 1
						break
					m -= 1

	def checkMoveDown(self):
		for row in range(3):
			for col in range(4):
				if self.table[row][col] != 0 and (self.table[row+1][col] == 0 or self.table[row+1][col] == self.table[row][col]):
					return True

	def moveDown(self):
		for col in range(4):
			n = 3
			for row in [3,2,1,0]:
				m = row
				while m < n:
					if self.table[m+1][col] == 0:
						self.table[m+1][col] = self.table[m][col]
						self.table[m][col] = 0
					elif self.table[m+1][col] == self.table[m][col]:
						self.table[m+1][col] *= 2
						self.table[m][col] = 0
						self.score += self.table[m+1][col]
						n -= 1
						break
					m += 1

	def checkMoveRight(self):
		for row in range(4):
			for col in range(3):
				if self.table[row][col] != 0 and (self.table[row][col+1] == 0 or self.table[row][col+1] == self.table[row][col]):
					return True

	def moveRight(self):
		for row in range(4):
			n = 3
			for col in [3,2,1,0]:
				m = col
				while m < n:
					if self.table[row][m+1] == 0:
						self.table[row][m+1] = self.table[row][m]
						self.table[row][m] = 0
					elif self.table[row][m+1] == self.table[row][m]:
						self.table[row][m+1] *= 2
						self.table[row][m] = 0
						self.score += self.table[row][m+1]
						n -= 1
						break
					m += 1

	def win(self):
		for row in self.table:
			for cell in row:
				if cell == 2048:
					self.won = True
					return True

	def lose(self):
		if not self.zeroExists() and not self.checkMoveUp() and not self.checkMoveLeft() and not self.checkMoveDown() and not self.checkMoveRight():
			return True

b1 = Board()
b1.insert()
b1.insert()
print("Controls: W = Up, A = Left, S = Down, D = Right")

while(1):
	b1.display()
	move = input("Make a move (W/A/S/D):")
	if b1.isMoveValid(move):
		b1.moveBoard(move)

		if not b1.won and b1.win():
			print("You win!")
			b1.display()
			end = input("Type 'end' to end game. Or to continue just press Enter:")
			if end == "end":
				break

		b1.insert()

		if b1.lose():
			b1.display()
			print("Game Over")
			end = input("Press Enter to end")
			print(end)
			break

	else:
		print("Invalid Move!")
