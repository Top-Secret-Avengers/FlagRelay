from tkinter import *
from tkinter import messagebox

# Since the tkinter dependencies are strange in virtual environments the 
# setup.py file does not want to work with docker. 
# will need to find a new solution (likely bash) or fix the tk dependency issue
def toggle():
    if showHints.get():
        hintsFrame.pack(fill="both", expand=True)
    else:
        hintsFrame.pack_forget()

def writeAnswers():
    input = answersEntry.get("1.0",END).rstrip('\n')

    if not input:
        messagebox.showwarning("Input error", "No flags entered")
        return
    
    fileName = "answer.txt"
    with open(fileName, 'w') as file:
        file.write(input)

def writeHints():
    if showHints:
        input = hintsEntry.get("1.0",END).rstrip('\n')

        if not input:
            messagebox.showinfo("Hints blank", "continuing without hints")
            return
        
        fileName = "hints.txt"
        with open(fileName, 'w') as file:
            file.write(input)
    else:
        return False
def start():
    writeAnswers()
    writeHints()
    # shut down setup and allow script to continue
    root.destroy()

root = Tk()

root.title("Flag Relay Setup")

root.geometry('600x400')
# create inputs that create/overwrite the answer.txt and hints.txt files

answersLabel = Label(root, text = "Enter each flag on a new line")
answersLabel.pack()

answersEntry = Text(root, height=10, width=40, font=("Arial",10))
answersEntry.pack()


showHints = BooleanVar()
# checkbox
hintsButton = Checkbutton(root, text="Are you using hints?", variable=showHints, command=toggle)
hintsButton.pack()

# hidden until checked
hintsFrame = Frame(root)
hintsLabel = Label(hintsFrame, text = "Enter a comma separated list of hints")
hintsLabel.pack()

hintsEntry = Text(hintsFrame, height=10, width=40, font=("Arial",10))
hintsEntry.pack()

startButton = Button(root, text="start", command=start)
startButton.pack()
# main!
root.mainloop()