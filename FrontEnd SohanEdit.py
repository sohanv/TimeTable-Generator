from tkinter import *  #importing tkinter
from PIL import ImageTk, Image
from timetable import timetable_main as tt
from download import download_button

#root window
root = Tk()
root.title('Timetable Generator')
root.configure(bg = 'black')
#root.iconbitmap("ad_cooldude.ico")
#root.attributes('-fullscreen', True)

#functions
def display_timetable(): #function to open a pop-up window
    pop_up = Toplevel()
    pop_up.title('Timetable Generator')
    pop_up.configure(bg = 'black')
    pop_up.grid()

    days = int(daysEntry.get())     # sohan added
    subjects = (subjectsEntry.get()).split(',')
    periods = len(subjects)
    tt(days,periods,subjects)

    global timetable_img
    timetable_img = ImageTk.PhotoImage(Image.open("tt-new.jpg"))
    
    image_label = Label(pop_up, image = timetable_img)
    image_label.grid(row = 0, column = 0)

def display_instructions():
    pop_up2 = Toplevel()
    pop_up2.title('Timetable Generator Instructions')
    pop_up2.configure(bg = 'black')
    pop_up2.grid()
    f = open('Instructions.txt', 'r')
    global text_label
    text_label = Label(pop_up2, text = f.read(), fg = 'white', bg = 'black', font = ('Arial', 12))
    text_label.grid(row = 1, column = 1)
    
#Labels and all that, 'na mean?
daysLabel = Label(root, text = 'Enter number of days:', fg = 'white', bg = 'black', font = ("proxima nova", 12))

#periodsLabel = Label(root, text = 'Enter number of periods per day')

subjectsLabel = Label(root, text = 'Enter the subjects seperated by a comma:', fg = 'white', bg = 'black', font = ("proxima nova", 12)) # sohan added

#Buttons
generate = Button(root, text = 'Generate Timetable', bg = 'green', fg = 'white', font = ("uni sans",12), command = display_timetable)

download = Button(root, text = 'Download TimeTable to Desktop',width = 25,  bg = 'green', fg = 'white', font = ("uni sans",12), command = download_button)

quit = Button(root, text = 'QUIT', width = 25, bg = 'red', fg = 'white', font = ("uni sans",12), command = root.destroy)

instructions = Button(root, text = '       Instructions       ', bg = 'green', fg = 'white', font = ("uni sans",12), command = display_instructions)

#taking input 
daysEntry = Entry(root, text = 'Enter number of days', width = 25, fg = 'black', bg = 'grey', bd = 5, font = ('Arial',12))

#periodsEntry = Entry(root, text = 'Enter number of periods per day', width = 12, fg = 'black', bg = 'grey', bd = 5)

subjectsEntry = Entry(root, text = 'Enter the subjects seperated by a comma', width = 25, fg = 'black', bg = 'grey', bd = 5, font = ('Arial',12)) # sohan added

#formatting the page
daysLabel.grid(row = 0, column = 0)

daysEntry.grid(row = 0, column = 1, padx = 35, pady = 10, columnspan = 3)

#periodsLabel.grid(row = 1, column = 0)

#periodsEntry.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 2)

subjectsLabel.grid(row = 1, column = 0)

subjectsEntry.grid(row = 1, column = 1, padx = 35, pady = 10, columnspan = 3)

instructions.grid(row = 3, column = 0, padx = 20, pady = 20, columnspan = 1)

generate.grid(row = 2, column = 0, padx = 20, pady = 10, columnspan = 1)

download.grid(row = 2, column = 1, padx = 20, pady = 20, columnspan = 1)

quit.grid(row = 3, column = 1, padx = 20, pady = 20, columnspan = 1)

root.mainloop()