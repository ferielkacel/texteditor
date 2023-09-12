from tkinter import *
import os
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

window = Tk()
window.config(bg="white")
window.geometry("400x400")

def fonter(*args):
    textarea.config(font=(fontname.get(), fontsize.get()))

def change_color():

  color = colorchooser.askcolor(title="choose your color")
  textarea.config(fg=color[1])


def about():
    showinfo("About this program", "mother is taylor wsift")

def new():
    window.title("Untitled")
    textarea.delete(1.0, END)


def opene():

    file = askopenfilename(file=[("All Files", "*.*"),
                                 ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            textarea.delete(1.0, END)

            file = open(file, "r")

            textarea.insert(1.0, file.read())

        except Exception:
            print("couldn't read file")

        finally:
            file.close()
def save():

    file = asksaveasfilename(file=[("All file","*.*"),
                             ("textdocument",".tx")])

    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file,"w")
            file.write(textarea.get(1.0,END))

        except:

            print("couldnt save")


def copy():
    textarea.event_generate("<<copy>>")

def cut():
     textarea.event_generate("<<cut>>")

def paste():
     textarea.event_generate("<<paste>>")

frame = Frame(window,width=400,height=400,bg="white")
frame.grid()





window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))


file = None
fontname = StringVar(window)
fontname.set("ariel")

fontsize = StringVar(window)
fontsize.set("25")

textarea = Text(window,font=(fontname.get(),fontsize.get()))

button = Button(window,text="color",command=change_color)
button.grid(row=10,column=0)



font_box = OptionMenu(window, fontname, *font.families(), command=fonter)
font_box.grid(row=10, column=1)

size_box = Spinbox(window, from_=1, to=100, textvariable=fontsize, command=fonter)
size_box.grid(row=10, column=2)

window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
textarea.grid(sticky=N + W + E + S)
main_bar = Menu(window)
window.config(menu=main_bar)

filemen=Menu(main_bar,tearoff=0)
main_bar.add_cascade(label="File", menu=filemen)

filemen.add_command(label="new",command=new)
filemen.add_command(label="open",command=opene)
filemen.add_command(label="save",command=save)



editmenu = Menu(main_bar,tearoff=0)
main_bar.add_cascade(label="edit", menu=editmenu)

editmenu.add_command(label="copy",command=copy)
editmenu.add_command(label="cut",command=cut)
editmenu.add_command(label="paste",command=paste)


aboutmenu = Menu(main_bar,tearoff=0)
main_bar.add_cascade(label="help", menu=aboutmenu)

aboutmenu.add_command(label="about",command=about)








window.mainloop()
