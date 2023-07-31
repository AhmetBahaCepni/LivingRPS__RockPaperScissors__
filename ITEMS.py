from email.mime import image
from tkinter import *
import random

WIDTH = 600
HEIGHT = 600



class Item:
    def __init__(self,canvas,xVelocity,yVelocity,image_type):
        self.canvas = canvas
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.image = canvas.create_image(random.randint(25,(WIDTH-25)),random.randint(25,(HEIGHT-25)),image=image_type)

    def move(self):
        coordinates = [(self.canvas.coords(self.image)[0]-16),(self.canvas.coords(self.image)[1]-16),(self.canvas.coords(self.image)[0]+16),(self.canvas.coords(self.image)[1]+16)]
        if(coordinates[2]>=(self.canvas.winfo_width())or coordinates[0]<0):
            self.xVelocity = -self.xVelocity
        if(coordinates[3]>=(self.canvas.winfo_height())or coordinates[1]<0):
            self.yVelocity = -self.yVelocity

        
            
        self.canvas.move(self.image,self.xVelocity,self.yVelocity)

    def stop(self):

        self.xVelocity = 0
        self.yVelocity = 0
        self.canvas.move(self.image,-1000,-1000)

    def get_coordinates(self):

        coordinates = [(self.canvas.coords(self.image)[0]-16),(self.canvas.coords(self.image)[1]-16),(self.canvas.coords(self.image)[0]+16),(self.canvas.coords(self.image)[1]+16)]
        return coordinates

