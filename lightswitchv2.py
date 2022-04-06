import tkinter as tk
window = tk.Tk()
count = 0
a = 0
check = True
    # schijf hier tussen je code
try:
    with open(r"C:\Users\Jeroen\Desktop\Projecten\file-write\actions.log", "x") as file:
        file.writelines("\nNew session.")
except:
    file = open (r"C:\Users\Jeroen\Desktop\Projecten\file-write\actions.log", "a")
    if check:
        file.writelines("\nNew session.")
        check = False
def knop(a):
    global button, count,check,file
    if count == 0:
        file.writelines("\nLicht aan")
        button.config(text='Light on.', bg="white", fg='Black')
        window.config(bg="yellow")
        count += 1
    else:
        file.writelines("\nLicht uit")
        button.config(text='Light off.', bg='white', fg='black')
        window.config(bg="black")
        count -= 1
    file.close()

button = tk.Button(text='light off.', bg="white", fg="black")
window.config(bg='black')
button.pack(pady = 50, padx = 60)
button.bind('<Button>', knop)
# schijf hier tussen je code

window.mainloop()