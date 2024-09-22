from tkinter import *  #importing tkinter
from PIL import ImageTk, Image
from timetable import timetable_main as tt
from download import download_button
import os.path

#root window
root = Tk()
root.title('Timetable Generator')
root.configure(bg = 'black')

#functions
def display_timetable(): #function to open a pop-up window

    days = int(daysEntry.get())     # recieves values entered by user in the GUI
    subjects = (subjectsEntry.get()).split(',')
    periods = len(subjects)

    if days > 7:
        display_error()
    else:
        pop_up = Toplevel()     # pop-up window for timetable
        pop_up.title('Timetable Generator')
        pop_up.configure(bg = 'black')
        pop_up.grid()

        tt(days,periods,subjects)

        global timetable_img
        timetable_img = ImageTk.PhotoImage(Image.open("tt-new.jpg"))
            
        image_label = Label(pop_up, image = timetable_img)
        image_label.grid(row = 0, column = 0)

def display_instructions():   #pop-up window for displaying instructions
    pop_up2 = Toplevel()
    pop_up2.title('Timetable Generator Instructions')
    pop_up2.configure(bg = 'black')
    pop_up2.grid()
    f1 = open('Instructions.txt', 'r')
    global text_label
    text_label = Label(pop_up2, text = f1.read(), fg = 'white', bg = 'black', font = ('Arial', 12))
    text_label.grid(row = 1, column = 1)

def display_error():    # pop-up window to display error
    pop_up3 = Toplevel()
    pop_up3.title('Error Message!')
    pop_up3.configure(bg = "black")
    pop_up3.grid()
    f2 = open('error.txt','r')
    global text_label2
    text_label2 = Label(pop_up3, text = f2.read(), fg = "white", bg = "black", font = ('Arial', 12))
    text_label2.grid(row = 1, column = 1)
    
#Labels definitions
daysLabel = Label(root, text = 'Enter number of days:', fg = 'white', bg = 'black', font = ("proxima nova", 12))

subjectsLabel = Label(root, text = 'Enter the subjects seperated by a comma:', fg = 'white', bg = 'black', font = ("proxima nova", 12)) # sohan added

#Buttons
generate = Button(root, text = 'Generate Timetable', width = 25, bg = 'green', fg = 'white', font = ("uni sans",12), command = display_timetable)

download = Button(root, text = 'Download TimeTable to Desktop',width = 25,  bg = 'green', fg = 'white', font = ("uni sans",12), command = download_button)

quit = Button(root, text = 'QUIT', width = 25, bg = 'red', fg = 'white', font = ("uni sans",12), command = root.destroy)

instructions = Button(root, text = 'Instructions', width = 25, bg = 'green', fg = 'white', font = ("uni sans",12), command = display_instructions)

#taking input 
daysEntry = Entry(root, text = 'Enter number of days', width = 25, fg = 'black', bg = 'grey', bd = 5, font = ('Arial',12))

subjectsEntry = Entry(root, text = 'Enter the subjects seperated by a comma', width = 25, fg = 'black', bg = 'grey', bd = 5, font = ('Arial',12)) # sohan added

#formatting the page
daysLabel.grid(row = 0, column = 0)

daysEntry.grid(row = 0, column = 1, padx = 35, pady = 10, columnspan = 1)

subjectsLabel.grid(row = 1, column = 0)

subjectsEntry.grid(row = 1, column = 1, padx = 35, pady = 10, columnspan = 1)

instructions.grid(row = 3, column = 0, padx = 20, pady = 20, columnspan = 1)

generate.grid(row = 2, column = 0, padx = 20, pady = 20, columnspan = 1)

download.grid(row = 2, column = 1, padx = 20, pady = 20, columnspan = 1)

quit.grid(row = 3, column = 1, padx = 20, pady = 20, columnspan = 1)

root.mainloop()
