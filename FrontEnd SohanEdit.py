from tkinter import * #importing tkinter
from PIL import ImageTk, Image
from timetable import timetable_main as tt

#root window
root = Tk()
root.title('Timetable Generator')
root.configure(bg = 'black')
root.iconbitmap("ad_cooldude.ico")
#root.attributes('-fullscreen', True)

#functions
def display_timetable(): #function to open a pop-up window
    pop_up = Toplevel()
    pop_up.title('Timetable Generator')
    pop_up.configure(bg = 'black')
    pop_up.grid

    days = int(daysEntry.get())     # sohan added
    periods = int(periodsEntry.get())
    subjects = (subjectsEntry.get()).split(',')
    tt(days,periods,subjects)

    global timetable_img
    timetable_img = ImageTk.PhotoImage(Image.open("tt-new.jpg"))
    
    image_label = Label(pop_up, image = timetable_img)
    image_label.grid(row = 0, column = 0)

#Labels and all that, 'na mean?
daysLabel = Label(root, text = 'Enter number of days')

periodsLabel = Label(root, text = 'Enter number of periods per day')

subjectsLabel = Label(root, text = 'Enter the subjects seperated by a comma') # sohan added

#Buttons
generate = Button(root, text = 'Generate Timetable', bg = 'green', fg = 'white', command = display_timetable)

quit = Button(root, text = 'QUIT', bg = 'red', fg = 'white', command = root.destroy)

#taking input 
daysEntry = Entry(root, text = 'Enter number of days', width = 12, fg = 'black', bg = 'grey', bd = 5)

periodsEntry = Entry(root, text = 'Enter number of periods per day', width = 12, fg = 'black', bg = 'grey', bd = 5)

subjectsEntry = Entry(root, text = 'Enter the subjects seperated by a comma', width = 12, fg = 'black', bg = 'grey', bd = 5) # sohan added

#formatting the page
daysLabel.grid(row = 0, column = 0)

daysEntry.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2)

periodsLabel.grid(row = 1, column = 0)

periodsEntry.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 2)

subjectsLabel.grid(row = 2, column = 0)

subjectsEntry.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan = 2)

generate.grid(row = 3, column = 0, padx = 20, pady = 10, columnspan = 1)

quit.grid(row = 3, column = 1, padx = 20, pady = 20, columnspan = 1)

root.mainloop()
