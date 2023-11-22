from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Tic-Tac-Toe')
root.iconbitmap('data:image/jpeg;base64,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')
#root.geometry("1200x710")

def b_click(b):
	global clicked, count

	if b["text"] == "" and clicked == True:
		b["text"] = "X"
		clicked = False
		count += 1
		checkifwon()
	elif b["text"] == "" and clicked == False:
		b["text"] = 'O'
		clicked = True
		count += 1
		checkifwon()
	else:
		messagebox.showerror("Tic-Tac-Toe", "Hey that box has already been selected\n Pick another box....." )

def reset():
	global b1, b2, b3,b4,b5,b6,b7,b8,b9
	global clicked, count
	clicked = True
	count = 0
	b1 = Button(root, text="", font= ("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda:b_click(b1))
	b2 = Button(root, text="", font= ("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda:b_click(b2))
	b3 = Button(root, text="", font= ("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda:b_click(b3))

	b4 = Button(root, text="", font= ("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda:b_click(b4))
	b5 = Button(root, text="", font= ("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda:b_click(b5))
	b6 = Button(root, text="", font= ("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda:b_click(b6))

	b7 = Button(root, text="", font= ("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda:b_click(b7))
	b8 = Button(root, text="", font= ("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda:b_click(b8))
	b9 = Button(root, text="", font= ("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda:b_click(b9))


	b1.grid(row=0, column=0)
	b2.grid(row=0, column=1)
	b3.grid(row=0, column=2)

	b4.grid(row=1, column=0)
	b5.grid(row=1, column=1)
	b6.grid(row=1, column=2)

	b7.grid(row=2, column=0)
	b8.grid(row=2, column=1)
	b9.grid(row=2, column=2)

clicked = True
count = 0


def disableallbtns():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)



def checkifwon():
	global winner
	winner = False

	if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
		b1.config(bg='green')
		b2.config(bg='green')
		b3.config(bg='green')
		winner = True
		disableallbtns()
		messagebox.showinfo("Tic-Tac-Toe", "Congrats X wins!!!!")

	elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
		b4.config(bg='green')
		b5.config(bg='green')
		b6.config(bg='green')
		winner = True
		messagebox.showinfo("Tic-Tac-Toe", "Congrats X wins!!!!")
		disableallbtns()

	elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
		b7.config(bg='green')
		b8.config(bg='green')
		b9.config(bg='green')
		winner = True
		messagebox.showinfo("Tic-Tac-Toe", "Congrats! X wins!!!!")
		disableallbtns()

	elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
		b1.config(bg='green')
		b4.config(bg='green')
		b7.config(bg='green')
		winner = True
		messagebox.showinfo("Tic-Tac-Toe", "Congrats! X wins!!!!")
		disableallbtns()
	elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
		b2.config(bg='green')
		b5.config(bg='green')
		b8.config(bg='green')
		winner = True
		messagebox.showinfo("Tic-Tac-Toe", "Congrats! X wins!!!!")
		disableallbtns()
	elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
		b3.config(bg='green')
		b6.config(bg='green')
		b9.config(bg='green')
		winner = True
		messagebox.showinfo("Tic-Tac-Toe", "Congrats! X wins!!!!")
		disableallbtns()
	elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
		b1.config(bg='green')
		b5.config(bg='green')
		b9.config(bg='green')
		winner = True
		messagebox.showinfo("Tic-Tac-Toe", "Congrats! X wins!!!!")
		disableallbtns()
	elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
		b3.config(bg='green')
		b5.config(bg='green')
		b7.config(bg='green')
		winner = True
		messagebox.showinfo("Tic-Tac-Toe", "Congrats! X wins!!!!")
		disableallbtns()
#o wins
	if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
		b1.config(bg='green')
		b2.config(bg='green')
		b3.config(bg='green')
		winner = True
		messagebox.showinfo("Tic-Tac-Toe", "Congrats X wins")
		disableallbtns()

	elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
		b4.config(bg='green')
		b5.config(bg='green')
		b6.config(bg='green')
		winner = True
		messagebox.showinfo("Tic-Tac-Toe", "Congrats O wins")
		disableallbtns()

	elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
		b7.config(bg='green')
		b8.config(bg='green')
		b9.config(bg='green')
		winner = True
		messagebox.showinfo("Tic-Tac-Toe", "Congrats! O wins!!!!")
		disableallbtns()

	elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
		b1.config(bg='green')
		b4.config(bg='green')
		b7.config(bg='green')
		winner = True
		messagebox.showinfo("Tic-Tac-Toe", "Congrats! O wins!!!!")
		disableallbtns()
	elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
		b2.config(bg='green')
		b5.config(bg='green')
		b8.config(bg='green')
		winner = True
		messagebox.showinfo("Tic-Tac-Toe", "Congrats! O wins!!!!")
		disableallbtns()
	elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
		b3.config(bg='green')
		b6.config(bg='green')
		b9.config(bg='green')
		winner = True
		messagebox.showinfo("Tic-Tac-Toe", "Congrats! O wins!!!!")
		disableallbtns()
	elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
		b1.config(bg='green')
		b5.config(bg='green')
		b9.config(bg='green')
		winner = True
		messagebox.showinfo("Tic-Tac-Toe", "Congrats! O wins!!!!")
		disableallbtns()
	elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
		b3.config(bg='green')
		b5.config(bg='green')
		b7.config(bg='green')
		winner = True
		messagebox.showinfo("Tic-Tac-Toe", "Congrats! O wins!!!!")
		disableallbtns()
#########################

menu  =  Menu(root)
root.config(menu=menu)

options_men = Menu(menu, tearoff=False)
menu.add_cascade(label='Options',menu=options_men)
options_men.add_command(label="Reset", command=reset)

reset()

root.mainloop()