from tkinter import *
from ITEMS import *
import time
import random

window = Tk()
window.title("Rock & Paper & Scissors Animated")
WIDTH = 600
HEIGHT = 600

canvas = Canvas(window,width=WIDTH,height=HEIGHT,bg="#585d66")
canvas.pack()

rock_image = PhotoImage(file = "Practise_Projects\\RPS\\rock.png")
paper_image = PhotoImage(file = "Practise_Projects\\RPS\\paper.png")
scissors_image = PhotoImage(file = "Practise_Projects\\RPS\\scissors.png")

rock_items = []
paper_items = []
scissors_items = []



for _ in range(3):
    rock_items.append(Item(canvas,random.randint(5,8),random.randint(5,8),rock_image))
    paper_items.append(Item(canvas,random.randint(5,8),random.randint(5,8),paper_image))
    scissors_items.append(Item(canvas,random.randint(5,8),random.randint(5,8),scissors_image))

while True:
    for rock in rock_items:
        rock.move()
    for paper in paper_items:
        paper.move()
    for scissors in scissors_items:
        scissors.move()
    for i in range(0,len(rock_items)):
        for j in range(0,len(paper_items)):
            for k in range(0,len(scissors_items)):
                if ((((rock_items[i].get_coordinates())[1]+ 16) > ((paper_items[j].get_coordinates())[1]+ 16)
                    and ((rock_items[i].get_coordinates())[1]+ 16) < (((paper_items[j].get_coordinates())[1]+ 16) + 16))
                    or ((((rock_items[i].get_coordinates())[1]+ 16) + 16) > ((paper_items[j].get_coordinates())[1]+ 16)
                    and (((rock_items[i].get_coordinates())[1]+ 16) + 16) < (((paper_items[j].get_coordinates())[1]+ 16) + 16))):
                    if ((((rock_items[i].get_coordinates())[0]+ 16) > ((paper_items[j].get_coordinates())[0]+ 16)
                    and ((rock_items[i].get_coordinates())[0]+ 16) < (((paper_items[j].get_coordinates())[0]+ 16) + 16))
                    or ((((rock_items[i].get_coordinates())[0]+ 16) + 16) > ((paper_items[j].get_coordinates())[0]+ 16)
                    and (((rock_items[i].get_coordinates())[0]+ 16) + 16) < (((paper_items[j].get_coordinates())[0]+ 16) + 16))):
                        rock_items[i].stop()
                if ((((rock_items[i].get_coordinates())[1]+ 16) > ((scissors_items[k].get_coordinates())[1]+ 16)
                    and ((rock_items[i].get_coordinates())[1]+ 16) < (((scissors_items[k].get_coordinates())[1]+ 16) + 16))
                    or ((((rock_items[i].get_coordinates())[1]+ 16) + 16) > ((scissors_items[k].get_coordinates())[1]+ 16)
                    and (((rock_items[i].get_coordinates())[1]+ 16) + 16) < (((scissors_items[k].get_coordinates())[1]+ 16) + 16))):
                    if ((((rock_items[i].get_coordinates())[0]+ 16) > ((scissors_items[k].get_coordinates())[0]+ 16)
                    and ((rock_items[i].get_coordinates())[0]+ 16) < (((scissors_items[k].get_coordinates())[0]+ 16) + 16))
                    or ((((rock_items[i].get_coordinates())[0]+ 16) + 16) > ((scissors_items[k].get_coordinates())[0]+ 16)
                    and (((rock_items[i].get_coordinates())[0]+ 16) + 16) < (((scissors_items[k].get_coordinates())[0]+ 16) + 16))):
                        scissors_items[k].stop()    
                if ((((paper_items[j].get_coordinates())[1]+ 16) > ((scissors_items[k].get_coordinates())[1]+ 16)
                    and ((paper_items[j].get_coordinates())[1]+ 16) < (((scissors_items[k].get_coordinates())[1]+ 16) + 16))
                    or ((((paper_items[j].get_coordinates())[1]+ 16) + 16) > ((scissors_items[k].get_coordinates())[1]+ 16)
                    and (((paper_items[j].get_coordinates())[1]+ 16) + 16) < (((scissors_items[k].get_coordinates())[1]+ 16) + 16))):
                    if ((((paper_items[j].get_coordinates())[0]+ 16) > ((scissors_items[k].get_coordinates())[0]+ 16)
                    and ((paper_items[j].get_coordinates())[0]+ 16) < (((scissors_items[k].get_coordinates())[0]+ 16) + 16))
                    or ((((paper_items[j].get_coordinates())[0]+ 16) + 16) > ((scissors_items[k].get_coordinates())[0]+ 16)
                    and (((paper_items[j].get_coordinates())[0]+ 16) + 16) < (((scissors_items[k].get_coordinates())[0]+ 16) + 16))):
                        paper_items[j].stop()
    window.update()
    time.sleep(0.01)
winow.mainloop()