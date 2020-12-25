#%%
from tkinter import *
from tkinter import ttk
import winsound 

root = Tk()

content = ttk.Frame(root)

s = ttk.Style()

#Button functionality
def red():
    s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
    ttk.Frame(root, width=200, height=200, style='Danger.TFrame')

def green():
    s.configure('Danger.TFrame', background='green', borderwidth=5, relief='raised')
    ttk.Frame(root, width=200, height=200, style='Danger.TFrame')

def orange():
    s.configure('Danger.TFrame', background='orange', borderwidth=5, relief='raised')
    ttk.Frame(root, width=200, height=200, style='Danger.TFrame')

#//am = StringVar()
#//am_entry = ttk.Entry(root, width=7, textvariable=am)
#//am_entry.grid(column=2, row=1, sticky=(W, E))
#//ttk.Label(root, text="Aantal Mensen:").grid(column=3, row=1, sticky=W)

#White begin block
s.configure('Danger.TFrame', background='white', borderwidth=50, relief='raised')
ttk.Frame(root, width=1000, height=500, style='Danger.TFrame').grid()

#spinbox = StringVar()
#s = ttk.Spinbox(root, from_=1.0, to=100.0, textvariable=spinbox).grid(column=4, row=1, sticky=W)
#ttk.Label(root, text="Aantal Mensen:").grid(column=3, row=1, sticky=W)
s = ttk.Spinbox(root, from_=1.0, to=100.0, textvariable=spinbox)
s.grid(column=4, row=1, sticky=W)
print(s.get())


#Buttons
button = ttk.Button(root, text='red', command=red).grid(column=3, row=3, sticky=W)
button = ttk.Button(root, text='green', command=green).grid(column=4, row=3, sticky=W)
button = ttk.Button(root, text='orange', command=orange).grid(column=5, row=3, sticky=W)

#Terminal functionality
def calculate(*args):
    try:
        x = input('Aantal mensen aanwezig:')
        if x <= '3':
            s.configure('Danger.TFrame', background='green', borderwidth=5, relief='raised')
            ttk.Frame(root, width=200, height=200, style='Danger.TFrame')
            #winsound.PlaySound('dotto.wav', winsound.SND_FILENAME)
            print("green")
        elif x >= "5":
            s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
            ttk.Frame(root, width=200, height=200, style='Danger.TFrame')
            print ("red")
        else:
            s.configure('Danger.TFrame', background='orange', borderwidth=5, relief='raised')
            ttk.Frame(root, width=200, height=200, style='Danger.TFrame')
            print("orange")
    except:
        print("error")
        
ttk.Button(root, text="Calculate", command=calculate).grid(column=2, row=3, sticky=W)

#feet_entry.focus()
root.bind("<Return>", calculate)
root.mainloop()


#TODO meer zoals de foto
#TODO comment toevoegen voor uitleg

# %%
