from tkinter import *
from tkinter import messagebox


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
    return False

def start():
    writeAnswers()
    writeHints()

    # shut down setup and allow script to continue

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