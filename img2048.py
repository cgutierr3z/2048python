#!/usr/bin/python2.7
# -*- encoding: utf-8 -*-

'''////////////////////////////////////////////////////////////////////////
							VISTA
   ////////////////////////////////////////////////////////////////////////
'''

import pygame

pygame.init()

b = pygame.image.load("imgs/block.jpg")
b1 = pygame.image.load("imgs/block1.jpg")
b2 = pygame.image.load("imgs/block2.jpg")
b3 = pygame.image.load("imgs/block3.jpg")
b4 = pygame.image.load("imgs/block4.jpg")
b5 = pygame.image.load("imgs/block5.jpg")
b6 = pygame.image.load("imgs/block6.jpg")
b7 = pygame.image.load("imgs/block7.jpg")
b8 = pygame.image.load("imgs/block8.jpg")
b9 = pygame.image.load("imgs/block9.jpg")
b10 = pygame.image.load("imgs/block10.jpg")
b11 = pygame.image.load("imgs/block11.jpg")

num = pygame.font.SysFont("Arial", 56)
num.set_bold(True)
n0 = num.render("", True, (0,0,0))
n2 = num.render("2", True, (0,0,0))
n4 = num.render("4", True, (70, 59, 45))
n8 = num.render("8", True, (75, 57, 35))

num2 = pygame.font.SysFont("Arial", 48)
num2.set_bold(True)
n16 = num2.render("16", True, (151, 71, 28))
n32 = num2.render("32", True, (184, 66, 3))
n64 = num2.render("64", True, (231, 67, 17))

num3 = pygame.font.SysFont("Arial", 40)
num3.set_bold(True)
n128 = num3.render("128", True, (214, 32, 0))
n256 = num3.render("256", True, (177, 112,0))
n512 = num3.render("512", True, (193, 196, 0))

num4 = pygame.font.SysFont("Arial", 34)
num4.set_bold(True)
n1024 = num4.render("1024", True, (121, 196,0))
n2048 = num4.render("2048", True, (46, 156, 1))

txt = pygame.font.SysFont("Arial", 30)
txt.set_bold(True)
scr = txt.render("SCORE = ", True, (255,255,255))

def drawScore(screen,str):
	text = txt.render(str, True, (255, 255, 255),(0,0,0))
	screen.blit(scr, (10,405))
	screen.blit(text, (176,405))

def drawFinal(screen,str):
	res = pygame.font.SysFont("Arial", 56)
	text = res.render(str, True, (255, 255, 255), (159, 182, 205))
	textRect = text.get_rect()
	textRect.centerx = screen.get_rect().centerx
	textRect.centery = screen.get_rect().centery
	screen.blit(text, textRect)

def drawCanvas(screen):
	seq = [0,100,200,300]
	for i in seq:
		for j in seq:
			screen.blit(b,(i, j))

def coord(position, size):
	return ((((100-size[0])/2) + 100*position[0]), ( ((100-size[1])/2) + 100*position[1]))

def coord2(position):
	return (100*position[0], 100*position[1])

def drawNum(screen, elem, pos):
	if elem == 0:
		screen.blit(b, coord2(pos))
		screen.blit(n0, coord(pos,num.size("")))
	if elem == 2:
		screen.blit(b1, coord2(pos))
		screen.blit(n2, coord(pos,num.size("2")))
	if elem == 4:
		screen.blit(b2, coord2(pos))
		screen.blit(n4, coord(pos,num.size("4")))
	if elem == 8:
		screen.blit(b3, coord2(pos))
		screen.blit(n8, coord(pos,num.size("8")))
	if elem == 16:
		screen.blit(b4, coord2(pos))
		screen.blit(n16, coord(pos,num2.size("16")))
	if elem == 32:
		screen.blit(b5, coord2(pos))
		screen.blit(n32, coord(pos,num2.size("32")))
	if elem == 64:
		screen.blit(b6, coord2(pos))
		screen.blit(n64, coord(pos,num2.size("64")))
	if elem == 128:
		screen.blit(b7, coord2(pos))
		screen.blit(n128, coord(pos,num3.size("128")))
	if elem == 256:
		screen.blit(b8, coord2(pos))
		screen.blit(n256, coord(pos,num3.size("256")))
	if elem == 512:
		screen.blit(b9, coord2(pos))
		screen.blit(n521, coord(pos,num3.size("512")))
	if elem == 1028:
		screen.blit(b10, coord2(pos))
		screen.blit(n1028, coord(pos,num4.size("1024")))
	if elem == 2048:
		screen.blit(b11, coord2(pos))
		screen.blit(n2048, coord(pos,num4.size("2048")))
	
	