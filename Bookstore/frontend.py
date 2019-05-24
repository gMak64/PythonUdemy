from tkinter import *
import backend


def get_selected_row(event):
    try:
        global selected_tuple
        index = book_list.curselection()[0]
        selected_tuple = book_list.get(index)
        title_info.delete(0, END)
        title_info.insert(END, selected_tuple[1])
        author_info.delete(0, END)
        author_info.insert(END, selected_tuple[2])
        year_info.delete(0, END)
        year_info.insert(END, selected_tuple[3])
        isbn_info.delete(0, END)
        isbn_info.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    book_list.delete(0, END)
    for item in backend.view():
        book_list.insert(END, item)


def search_command():
    book_list.delete(0, END)
    for item in backend.search(title_text.get(), author_text.get(),
                               int(year_text.get()), int(isbn_text.get())):
        book_list.insert(END, item)


def add_command():
    backend.insert(title_text.get(), author_text.get(),
                   int(year_text.get()), int(isbn_text.get()))
    book_list.delete(0, END)
    book_list.insert(END, title_text.get(), author_text.get(),
                     int(year_text.get()), int(isbn_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])
    book_list.delete(0, END)
    for item in backend.view():
        book_list.insert(END, item)


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(),
                   int(year_text.get()), int(isbn_text.get()))


window = Tk()

title_label = Label(window, text="Title")
title_label.grid(row=0, column=0)

author_label = Label(window, text="Author")
author_label.grid(row=0, column=5)

year_label = Label(window, text="Year")
year_label.grid(row=2, column=0)

isbn_label = Label(window, text="ISBN")
isbn_label.grid(row=2, column=5)

title_text = StringVar()
title_info = Entry(window, textvariable=title_text)
title_info.grid(row=0, column=1, columnspan=4)

author_text = StringVar()
author_info = Entry(window, textvariable=author_text)
author_info.grid(row=0, column=6, columnspan=4)

year_text = StringVar()
year_info = Entry(window, textvariable=year_text)
year_info.grid(row=2, column=1, columnspan=4)

isbn_text = StringVar()
isbn_info = Entry(window, textvariable=isbn_text)
isbn_info.grid(row=2, column=6, columnspan=4)

book_list = Listbox(window, height=6, width=35)
book_list.grid(row=2, column=0, rowspan=9, columnspan=8)

book_scroll = Scrollbar(window)
book_scroll.grid(row=2, column=8, rowspan=9)

book_list.configure(yscrollcommand=book_scroll)
book_scroll.configure(command=book_list.yview)
book_list.bind('<<ListboxSelect>>', get_selected_row)

view_button = Button(window, text="View All", width=13, command=view_command)
view_button.grid(row=3, column=9)

search_button = Button(window, text="Search", width=13, command=search_command)
search_button.grid(row=4, column=9)

add_button = Button(window, text="Add Entry", width=13, command=add_command)
add_button.grid(row=5, column=9)

update_button = Button(window, text="Update Entry", width=13 ,command=update_command)
update_button.grid(row=6, column=9)

delete_button = Button(window, text="Delete Entry", width=13, command=delete_command)
delete_button.grid(row=7, column=9)

close_button = Button(window, text="Close", width=13, command=window.destroy)
close_button.grid(row=8, column=9)

window.mainloop()