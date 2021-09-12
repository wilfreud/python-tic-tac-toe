from tkinter import *
import os

def screenMSG(fileName, *args,): # Main function for popup PARAMS: *args=PlayerName filename=__file__
    show = Tk()
    show.title("")
    show.geometry("200x100")
    show.resizable(False, False)
    show.eval('tk::PlaceWindow . center')

    def bunttonFunctionExit(): # action for exiting on button click
        exit()
    def buttonFunctionRestart(): # To relaunch the main program
        # import subprocess
        # filePath = os.path.realpath(fileName)
        # subprocess.run(['python', fileName], shell=True)
        os.system(f"python {fileName}")

    def showMessage(msgParam): # for displaying text (WIN case or TIE case)
        mess = Label(show, text=f"{msgParam}", height=2)
        mess.pack()

    def showButton(write_text, action, setSide): # Exits the program on button click 
        ok_button = Button(show, text=write_text, command=action, width=10, relief=RAISED, height=3)
        ok_button.pack(side=setSide)

    def exitOrRestart():
        showButton("RESTART", lambda:[buttonFunctionRestart(), show.destroy()], LEFT) # Restart the program and destroys the windows
        showButton("EXIT" ,lambda: [bunttonFunctionExit(), show.destroy()], RIGHT)  # Exit the program and destroy the window

    if len(args) == 1:
        showMessage(args[0]+" WON")
        exitOrRestart()
    elif len(args) == 0:
        showMessage("TIE!")
        exitOrRestart()
    
    show.mainloop()