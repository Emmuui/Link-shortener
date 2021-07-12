from tkinter import *
import pyshorteners
import pyperclip


root = Tk()
root.title('ShortLink')
root.configure(bg='#BABCA8')
w = 200
h = 200
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
x = (x//2) - (w//2)
y = (y//2) - (h//2)
root.geometry(f'{w}x{h}+{x}+{y}')

link = StringVar()
sortUrl = StringVar()


def short_link():
    sort_url = link.get()
    generate_short_link = pyshorteners.Shortener().tinyurl.short(sort_url)
    sortUrl.set(generate_short_link)


def copy():
    generate_short_link = sortUrl.get()
    pyperclip.copy(generate_short_link)


Label(root, text='Generate your short link').pack(pady=10)
Entry(root, textvariable=link).pack(pady=5)
Button(root, text='generate', command=short_link).pack(pady=5)
Entry(root, textvariable=sortUrl).pack(pady=5)
Button(root, text='copy', command=copy).pack(pady=5)
root.mainloop()
