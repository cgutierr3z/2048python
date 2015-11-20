#!/usr/bin/python2.7
# -*- encoding: utf-8 -*-
import types, random, pygame, os
from img2048 import * #Libreria que contiene las imagenes del juego

'''////////////////////////////////////////////////////////////////////////
								CONTROLADOR
   ////////////////////////////////////////////////////////////////////////
'''
class Board:
	def __init__(self, rows, cols):
		self.board = []
		self.score = 0
		self.rows = rows
		self.cols = cols

	#METODO QUE PONE TODO EL TABLERO EN CERO
	def startBoard(self):
		for i in range(self.rows):
			self.board.append([0]*self.cols)

	# Metodo que retorna una posicion aletoria del board
	def get_random(self):
		nrows = self.rows
		ncols = self.cols
		row_array=[]
		cols_array=[]
		for i in range(nrows):
			for j in range(ncols):
				if self.board[i][j]==0:
					if not i in row_array :
						row_array.append(i)
					if not j in cols_array:
						cols_array.append(j)
		i=row_array[ random.randrange (len(row_array)) ]
		j=cols_array[ random.randrange (len(cols_array)) ]
		return (i,j)

	def fillBoard(self):
		while True:
			pair = self.get_random()
			i = pair[0]
			j = pair[1]
			if self.board[i][j] == 0:
				self.board[i][j] = random.randrange(2,5,2)
				break

	# Determinar si se llego al 2048
	def isSolved(self):
		nrows = self.rows
		ncols = self.cols

		for i in range(nrows):
			for j in range(ncols):
				if self.board[i][j]==2048:
					return True
		#return False

	def isValid(self):
		nrows = self.rows
		ncols = self.cols

		for i in range(nrows):
			for j in range(ncols):
				if self.board[i][j]==0:
					return True
		#return False

	# Movimientos
	def mvRight(self):
		nrows = self.rows
		ncols = self.cols
		
		for i in range(nrows):
			j=ncols-2
			while j>=0:
				for x in range(j,nrows-1):
					if( self.board[i][x] != 0 and self.board[i][x+1] == 0 ):
						self.board[i][x+1]=self.board[i][x]
						self.board[i][x]=0
				j=j-1

	def mvLeft(self):
		nrows = self.rows
		ncols = self.cols
		
		for i in range(nrows):
			for j in range(ncols):
				a=j
				while self.board[i][a-1]==0  and a>0:
					self.board[i][a-1]=self.board[i][a]
					self.board[i][a]=0
					a-=1

	def mvUp(self):
		nrows = self.rows
		ncols = self.cols
		j=1
		y=1
		while j<nrows:
			x=j
			while x>0:
				for y in range(0,nrows):
					if( self.board[x][y] != 0 and  self.board[x-1][y] == 0):
						self.board[x-1][y]=self.board[x][y]
						self.board[x][y]=0
				x=x-1					
			j=j+1		

	def mvDown(self):
		nrows = self.rows
		ncols = self.cols
		
		j=nrows-2
		while j>=0:
			x=j
			while x>=0:
				for y in range(nrows):
					if( self.board[x][y] != 0 and  self.board[x+1][y] == 0):
						self.board[x+1][y]=self.board[x][y]
						self.board[x][y]=0
				x-=1
			j-=1

	# Sumas
	def addRight(self):
		nrows = self.rows
		ncols = self.cols

		for i in range(nrows):
			for x in range(nrows-1,0,-1):
				if( self.board[i][x] == self.board[i][x-1] and  self.board[i][x]!=0):
					self.board[i][x] = self.board[i][x] + self.board[i][x]
					self.board[i][x-1] = 0
					self.score+=10

	def addLeft(self):
		nrows = self.rows
		ncols = self.cols

		for i in range(nrows):
				for x in range(0,ncols-1):
					if( self.board[i][x] == self.board[i][x+1] and self.board[i][x]!=0):
						self.board[i][x]= (self.board[i][x]) * 2
						self.board[i][x+1] = 0
						self.score+=10

	def addUp(self):
		nrows = self.rows
		ncols = self.cols

		for j in range(ncols):
				for i in range(0,nrows-1):
					if( self.board[i][j] == self.board[i+1][j] and self.board[i][j]!=0):
						self.board[i][j] = (self.board[i][j]) * 2
						self.board[i+1][j]=0
						self.score+=10

	def addDown(self):
		nrows = self.rows
		ncols = self.cols

		for j in range(ncols):
				for i in range(nrows-1,0,-1):
					if( self.board[i][j] == self.board[i-1][j] and self.board[i][j]!=0 ):
						self.board[i][j]= self.board[i][j] + self.board[i][j]
						self.board[i-1][j]=0
						self.score+=10


# Por defecto el tablero de juego, va a ser de 4x4
class Canvas2048(Board):
	width, height = 400, 450  # Valores por defecto
	tam = width, height
	screen = pygame.display.set_mode(tam)
	pygame.display.set_caption("2048Game - (Felipe C & Carlos G - Progra IV ISC UTP 2014)")
	
	def fillCanvas(self):
		self.fillBoard()
		drawCanvas(self.screen)
		y = 0
		for i in self.board:
			x = 0
			for j in i:
				drawNum(self.screen, j, (x, y))
				x = x + 1
			y = y + 1
		drawScore(self.screen,str(self.score))
		pygame.display.flip()

	def init(self):
		drawCanvas(self.screen)
		self.startBoard()
		self.fillCanvas()

	def stop(self,result):
		drawFinal(self.screen,result)
		pygame.display.flip()

def main():
	i = Canvas2048(4, 4)
	i.init()

	exit = False
	while not exit:
		if i.isSolved():
			i.stop('YOU WIN :)')
			break
		elif not i.isValid():
			i.stop('YOU LOSE =P')
			break
		else:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						i.mvUp()
						i.addUp()
						i.mvUp()
					elif event.key == pygame.K_DOWN:
						i.mvDown()
						i.addDown()
						i.mvDown()
					elif event.key == pygame.K_RIGHT:
						i.mvRight()
						i.addRight()
						i.mvRight()
					elif event.key == pygame.K_LEFT:
						i.mvLeft()
						i.addLeft()
						i.mvLeft()
					elif event.key == pygame.K_ESCAPE:
						exit = True

					i.fillCanvas()

	#goodBye()


if __name__ == '__main__':
    pygame.init()
    main()
