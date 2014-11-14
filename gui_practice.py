#practice with gui
#call to modules
import Tkinter

#create a GUI window
root = Tkinter.Tk()
#title
root.title("Example Window")
#size
root.geometry("300x300")

#format for displaying the title
nameLabel = Tkinter.Label(root, text="", font=('Helvetica', 30))
nameLabel.pack()

#add a button
samplebutton = Tkinter.Button(text="Click")
samplebutton.pack()

#start the GUI
root.mainloop()