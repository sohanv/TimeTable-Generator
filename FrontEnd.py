from tkinter import * #importing tkinter
from PIL import ImageTk, Image

#root window
root = Tk()
root.title('Timetable Generator')
root.configure(bg = 'black')
#root.iconbitmap("nameoffile.ico")
#root.attributes('-fullscreen', True)

timetable_img = ImageTk.PhotoImage(Image.open("blank.jpg"))

#functions
def display_timetable(): #function to open a pop-up window
    pop_up = Toplevel()
    pop_up.title('Timetable Generator')
    pop_up.configure(bg = 'black')
    pop_up.grid
    #timetable_img = ImageTk.PhotoImage(Image.open("kumblus.jpg"))
    image_label = Label(pop_up, image = timetable_img)
    image_label.grid(row = 0, column = 0)

#Labels and all that, 'na mean?
daysLabel = Label(root, text = 'Enter number of days')

periodsLabel = Label(root, text = 'Enter number of periods per day')

#Buttons
generate = Button(root, text = 'Generate Timetable', bg = 'green', fg = 'white', command = display_timetable)

#taking input 
daysEntry = Entry(root, text = 'Enter number of days', width = 12, fg = 'white', bg = 'black', bd = 5)

periodsEntry = Entry(root, text = 'Enter number of periods per day', width = 12, fg = 'white', bg = 'black', bd = 5)

#formatting the page
daysLabel.grid(row = 0, column = 0)

daysEntry.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2)

periodsLabel.grid(row = 1, column = 0)

periodsEntry.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 2)

generate.grid(row = 2, column = 0, padx = 20, pady = 10, columnspan = 1)

root.mainloop()
