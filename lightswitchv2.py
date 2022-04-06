import tkinter as tk
window = tk.Tk()
count = 0
a = 0
check = True
    # schijf hier tussen je code
switchbutton = tk.Button(text='light off.', bg="white", fg="black",command=lambda: [knop(a)])
window.config(bg='black')
switchbutton.pack(pady = 50, padx = 60)

def knop(a):
    global switchbutton, count,check,file
    try:
        file = open(r"actions.log","a")
        if check:
            file.writelines("\nNew session.")
            check = False
    except:
        with open(r"actions.log", "x") as file:
            file.writelines("New session.")
    if count == 0:
        file.writelines("\nLicht aan")
        switchbutton.config(text='Light on.', bg="white", fg='Black')
        window.config(bg="yellow")
        count += 1
    else:
        file.writelines("\nLicht uit")
        switchbutton.config(text='Light off.', bg='white', fg='black')
        window.config(bg="black")
        count -= 1
    file.close()


# schijf hier tussen je code

window.mainloop()