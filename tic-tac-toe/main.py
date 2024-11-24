import ttkbootstrap as ttk
from mvc.view import TttView
from mvc.controller import TttController
from mvc.model import TttModel

if __name__ == '__main__':
    app = ttk.Window()
    app.configure(background='#ADD8E6')
    app.title('Tic tac toe')
    app.minsize(450, 450)

    model = TttModel()
    view = TttView(master=app, model=model)
    view.pack(padx=20, pady=20)
    controller = TttController(view, model)
    app.mainloop()