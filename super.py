from pygame.locals import *
import os
import pygame
import random
import pygameMenu
from pygameMenu.locals import *

class player1:
    def __init__(self,x,y,width,height,vel):
        self.x = x
        self.vel = vel
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0

    def draw(self,win):
        pass
    def collide(self,rect):
        pass

class background1(object):
    def __init__(self, x, y, vel, index):
        self.x = x
        self.y = y
        self.index = index
        self.vel = vel

    def draw(self, win):
        if self.x < -800:
            self.x = 800