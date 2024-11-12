from view import TttView
from model import TttModel
import numpy as np

class TttController:
    def __init__(self, view: TttView, model: TttModel) -> None:
        self.view = view
        self.model = model
        
        for idx, cell in np.ndenumerate(self.view.cells):
            cell.config(command=lambda x=idx[1], y=idx[0]: self.on_click(x, y))
        
        self.view.lbl_player.config(textvariable=model.str_player)
    
    
    def on_click(self, x: int, y: int):
        """Controls player alternations"""
        print(f'Current position: {x}.{y}!')
        
        #update player
        print('Current Player:', self.model.str_player.get())
        self.model.player = (self.model.player + 1) % 2
        
        self.view.update_cell(y, x, self.model.player)
        
        self.model.grid[y, x] = 1 if self.model.player == 1 else -1
        
        if self.check_winning(x, y):
            for idx, val in np.ndenumerate(self.model.grid):
                if val == 0:
                    self.view.update_cell(*idx, 2)
            self.view.end_message(self.model.str_player.get())

    
    
    def check_winning(self, x: int, y: int):
        grid = self.model.grid
        
        row = abs(np.sum(grid[y, :]))
        column = abs(np.sum(grid[:, x]))
        main_diag = abs(np.sum(np.diag(grid, x - y)))
        anti_diag = abs(np.sum(np.diag(np.fliplr(grid), (grid.shape[1] - x - 1) - y)))
        
        return any(line == 3 for line in (row, column, main_diag, anti_diag))
        
        