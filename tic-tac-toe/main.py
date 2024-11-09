import ttkbootstrap as ttk

from view import TttView
from controller import TttController
from model import TttModel

if __name__ == '__main__':
    app = ttk.Window()
    app.title('Tic tac toe')
    view = TttView(master=app)
    view.pack(padx=20, pady=20)
    model = TttModel()
    controller = TttController(view, model)
    app.mainloop()