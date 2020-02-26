from tkinter import *
from tkinter.messagebox import showinfo

from tagcounter.utils.siteprocessing import save_site_info, show_site_info
"""
Примерное содрежание GUI окна программы:
Вверху поле для ввода сайта внизу кнопки "Загрузить", "Показать из базы".
Ниже тестовое поле где выводятся теги и их количество ниже строка статуса
"""


def run_window():
    window = Tk()
    window.title('TagCounter')
    window.geometry("330x450")

    label = Label(window, text='Enter site name or synonym:')
    label.pack()
    label.place(bordermode=OUTSIDE, height=20, width=150, x=10, y=10)

    entry_site = Entry(window, text='Enter site name or synonym:')
    entry_site.pack()
    entry_site.place(bordermode=OUTSIDE, height=20, width=300, x=10, y=30)

    tag_info = Text(window)
    tag_info.pack()
    tag_info.place(bordermode=OUTSIDE, height=330, width=300, x=10, y=100)

    def get_tag_info():
        site = entry_site.get()
        if site:
            site_dict = save_site_info(site)
            showinfo(title='Info', message='Site: {} \n Information is saved successfully!'.format(site_dict['site']))
        else:
            showinfo(title='Warning', message='Please, enter site name!')

    def view_tag_info():
        site = entry_site.get()
        if site:
            site_dict = show_site_info(site)
            tag_info.delete('1.0', END)
            tag_info.insert('1.0', site_dict['tags'])
        else:
            showinfo(title='Warning', message='Please, enter site name!')

    button_get = Button(window, text='Load', command=get_tag_info, width=10)
    button_get.pack()
    button_get.place(bordermode=OUTSIDE, x=10, y=60)
    button_view = Button(window, text='Show', command=view_tag_info, width=10)
    button_view.pack()
    button_view.place(bordermode=OUTSIDE, x=110, y=60)

    window.mainloop()


