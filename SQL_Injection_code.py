from tkinter import *
import requests
import top as top

# krijimi i funksionit per testimin e URL

def testVulnerability():
    urlEntered = enterText.get()
    postArgEntered = enterPostArgText.get()

    # thirrja e funskionit per kontrollim te URL

    value = checkIfVulnerable(urlEntered, postArgEntered)

    if value == 1:
        enterText.delete(0, END)
        enterText.insert(0, "Vulnerable")
    else:
        enterText.delete(0, END)
        enterText.insert(0, "Not vulnerable")

# funksioni per gjetjen e Vulnerable files

def checkIfVulnerable(url, postArg):
    # key value pair qe i dergohet URL

    data = {'userid': postArg}

    result = requests.post(url, data)

    # kalkulimi i 'response' nese vonohet me shume se nje 1 sec (eshte vulnerable)

    if float(result.elapsed.total_seconds()) and float(result.elapsed.total_seconds())>1:
        return 1
    else:
        return 0

root = Tk()
root.wm_title("First GUI Window")
root.geometry("400x250")

#shtimi i nje menu

menubar = Menu(root)
file = Menu(menubar, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as...")
file.add_command(label="Close")
file.add_separator()
file.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file)
edit = Menu(menubar, tearoff=0)
edit.add_command(label="Undo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Select All")
menubar.add_cascade(label="Edit", menu=edit)
help = Menu(menubar, tearoff=0)
help.add_command(label="About")
menubar.add_cascade(label="Help", menu=help)
root.config(menu=menubar)

#label 1 per shtypjen e linkut
enterURL = Label(root, text="Shtyp URL per testim: ", fg="#222831")

enterURL.grid(row=0, column=0)

enterText = Entry(root)
enterText.config(width=30, bg="#DDDDDD", fg="#30475E")
enterText.grid(row=0, column=1, pady=10, padx=5)

# label 2 per shtypjen e post argumentit
enterPostArg = Label(root, text="Shtyp post argumentin: ", fg="#222831")

enterPostArg.grid(row=1, column=0)

enterPostArgText = Entry(root)
enterPostArgText.config(width=30, bg= "#DDDDDD", fg = "#30475E")
enterPostArgText.grid(row=1, column=1, pady=10, padx=5)

checkIfVunlerable = Button(root, text="Testo", command=testVulnerability, fg="#F05454")
checkIfVunlerable.grid(row=2, column=1, pady=10, padx=5)

root.mainloop()
