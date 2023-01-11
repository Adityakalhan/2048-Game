from tkinter import Frame,Label,CENTER
import constants as c
import logic
class Game2048(Frame) : #frame allows us to make a box like thing in which we can place all of our widgets
    def __init__(self) :
        Frame.__init__(self) #the frame is created
        self.grid() #helps in making all the widgets in the form of a grid
        self.master.title('2048')
        self.master.bind("<Key>",self.key_down) #whenever a key is pressed in the frame, the key_down function will be implemented
        #a map for our key binds and the functions :
        self.commands = {c.KEY_UP :logic.up_move,c.KEY_DOWN :logic.down_move,c.KEY_LEFT:logic.left_move,c.KEY_RIGHT : logic.right_move}

        self.grid_cells = [] #ie initially the grid is empty
        self.init_grid() #add the grid cells
        self.init_matrix() #Start the game and add 2s
        self.update_grid_cells() #initially all grid cells were 0, we need to change the colors etc for the grid. For changing the UI.

        self.mainloop() #for running the program


    def init_grid(self) :
        background = Frame(self,bg = c.background_color_game,width=c.size,height = c.size) #creating a frame, inside another frame
        background.grid() #visualise the background as a grid
        for i in range(c.grid_len) :
            grid_row = []
            for j in range(c.grid_len) :
                cell = Frame(background,bg = c.background_color_cell_empty,width = c.size/c.grid_len,height = c.size/c.grid_len) #another frame inside our background

                cell.grid(row = i,column = j,padx=c.padding) #adding the cells inside the grid
                #adding a label to the cells
                t = Label(master = cell,text = "",bg = c.background_color_cell_empty,justify=CENTER,font = c.FONT,width=5,height = 2) #used to denote a text box
                #the cells will remain the same, but the labels will be changing
                #labels cover the cells entirely
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    #we now need to add the matrix to our UI
    def init_matrix(self) : #creation of the matrix
        self.matrix = logic.start_game() # our initial matrix (4x4 of all 0)
        logic.add_new_2(self.matrix)
        logic.add_new_2(self.matrix)

    #for reflecting change in UI
    def update_grid_cells(self) :
        for i in range(c.grid_len) :
            for j in range(c.grid_len) :

                new_number = self.matrix[i][j]
                if new_number == 0 :
                    self.grid_cells[i][j].configure(text = " ",bg = c.background_color_cell_empty)
                else :
                    self.grid_cells[i][j].configure(text = str(new_number),bg = c.BACKGROUND_COLOR_DICT[new_number],fg = c.CELL_COLOR_DICT[new_number])
                    #fg means the color of the text that will be there inside the cell
        self.update_idletasks() #part of Frames Library, will wait for all the colours to get changed

    def key_down(self,event) : #event =w,s,a,d

        key = repr(event.char) #event.char will give us the key pressed, repr will give us the prinatable part, eg = repr('w') = w
        if key in self.commands :
            self.matrix,changed = self.commands[repr(event.char)](self.matrix) #calling the function corresponding to the event and passing matrix as arguement
            if changed :
                logic.add_new_2(self.matrix)
                self.update_grid_cells()
                changed = False

                if logic.get_current_state(self.matrix) == "Won" :
                    self.grid_cells[1][1].configure(text = "YOU",bg = c.background_color_cell_empty)
                    self.grid_cells[1][2].configure(text = "WON!",bg = c.background_color_cell_empty)

                if logic.get_current_state(self.matrix) == "Lost" :
                    self.grid_cells[1][1].configure(text = "YOU",bg = c.background_color_cell_empty)
                    self.grid_cells[1][2].configure(text = "LOST:(",bg = c.background_color_cell_empty)

                    


gameGrid = Game2048()
