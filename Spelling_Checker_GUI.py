import tkinter as tk
from textblob import TextBlob

root=tk.Tk()

root.title("spelling checker")
root.geometry("800x550")
root.config(background="#AAF2E9")

def check_spelling():
    word=enter_text.get()
    a=TextBlob(word)
    right=str(a.correct())

    cs=tk.Label(root, text="correct spelling is:",font=("Brush Script MT",25),bg="#F9DE74",fg="#FF0000")
    cs.place(x=100,y=225)
    spell.config(text=right)



heading=tk.Label(root, text="spelling Checker",font=("fantasy",30,"bold"),background="#AAF2E9",foreground="#FF0000")
heading.pack(padx=50,pady=0)

enter_text=tk.Entry(root,justify="center",width=35,font=("Impact",25),background="white",bd=2)
enter_text.pack(pady=10)
enter_text.focus()

button=tk.Button(root, text="Check",font=("Georgia",25),bg="#F2F9F8",fg="red",command=check_spelling)
button.pack()

spell=tk.Label(root,font=("Verdana",25),bg="#0C9CFB",fg="#44FF0C")
spell.place(x=400,y=225)




root.mainloop()