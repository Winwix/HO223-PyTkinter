import tkinter as tk
from app_constants import *
from DB_SQLITE3 import init_db, get_data



def run_app():
    # def btn_clicked():
    #     print('gumb "btn_click" je kliknut')
    #     lbl_massage_var.set('gumb "btn_click" je kliknut')

    movies_dict = {}
    list_items = []
    if get_data() is not None:
        for item in  get_data():
            list_items.append(f'{item[0]-item[1]}')

            list_items[f'{item[0]-item[1]}'] = item [0]

    def load_items():
        
        lb_movies_var.set(list_items)


    def lb_selected(event):
        
        # index = lb_movies.curselection()
        index = lb_movies.curselection()
        vrijednost = lb_movies.get(index)
        movie_data = str(vrijednost).split('-')
        index_in_db = movies_dict[f'{movie_data[0]}-{movie_data[1]}']
        lbl_message_var.set(f'{index} - {vrijednost} - {index_in_db}')

    main_window = tk.Tk()
    main_window.title('Python Tkinter DEMO')
    main_window.geometry('600x800')

    lbl_title = tk.Label(main_window,
                         text ='Python Tinkter DEMO Aplikacija',
                         font = HEADER_TEXT)
    lbl_title.pack(pady=PADY)

    frm_header = tk.LabelFrame(main_window,
                               font = BODY_TEXT,
                               text='Zaglavlje')
    frm_header.pack(padx = PADX, pady = PADY)

    btn_load = tk.Button (frm_header,
                          text = 'Ucitaj', font = BODY_TEXT,
                          command = load_items)
    btn_load.grid(row=0, column=0, 
                   padx = PADX, pady = PADY, ipadx = IPADX, ipady = IPADY)

    btn_save = tk.Button (frm_header,
                          text = 'Snimi', font = BODY_TEXT)
    btn_save.grid( row = 0, column = 1,
                  padx = PADX, pady = PADY, ipadx = IPADX, ipady = IPADY)

    btn_cancel = tk.Button (frm_header,
                          text = 'Odustani', font = BODY_TEXT)
    btn_cancel.grid( row = 0, column = 2,
                    padx = PADX, pady = PADY, ipadx = IPADX, ipady = IPADY)



    frm_body = tk.LabelFrame(main_window,
                             font = BODY_TEXT,
                            text='glavni okvir')
    frm_body.pack(padx = PADX, pady = PADY, ipadx = IPADX, ipady = IPADY)

    lb_movies_var = tk.StringVar()
    lb_movies = tk.Listbox(frm_body, font = BODY_TEXT,
                           listvariable= lb_movies_var)
    lb_movies.grid(row = 0, column = 0,
                   sticky = tk.EW,
                   padx = PADX, pady = PADY, ipadx = IPADX, ipady = IPADY)
    lb_movies.bind('<<ListBoxSelect>>', lb_selected)



    lbl_message_var = tk.StringVar()
    lbl_message_var.set('pocetna vrijednost')
    lbl_message = tk.Label(main_window,
                           textvariable=lbl_message_var,
                           font = BODY_TEXT)
    lbl_message.pack()

    main_window.mainloop()
    # btn_click = tk.Button(main_window, 
    #                       text = 'klikni me:',
    #                       command = btn_clicked,
    #                       font = ('segoe UI', 18))
    # btn_click.pack()


    # lbl_massage_var = tk.StringVar()
    # lbl_massage_var.set('Prikaz poruke')
    # lbl_massage = tk.Label(main_window,
    #                    textvariable =lbl_massage_var)
    # lbl_massage.pack()

    # main_window.mainloop()


if __name__ == '__main__':
    init_db()
    run_app()