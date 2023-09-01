import time
import tkinter as tk
from tkinter import Canvas, Frame, BOTH

tic_board = [['?','?','?'],
         ['?','?','?'],
         ['?','?','?'],]
click = 0

class Application(tk.Frame):
    global canvas
   
    def draw_board( self ):
        canvas.create_line(175, 75, 175, 375, width = 7)
        canvas.create_line(325, 75, 325, 375, width = 7)
        canvas.create_line(25, 275, 475, 275, width = 7)
        canvas.create_line(25, 175, 475, 175, width = 7)
           
    def __init__(self, master):
        global canvas
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        self.draw_board( )
        canvas.pack(fill=BOTH, expand=1)  
        canvas.update()

def mouse_click_to_grid(x,y):
    row = abs(y-75)//100 
    col = (x-25)//150
    return row,col
    
def current_player():
    global click
    if click%2 == 0:
        click +=1
        return 'X'
    else:
        click +=1
        return 'O'       

def print_board(row, col, char):
    if char == 'X':
        canvas.create_oval(35 + 150*col,85 + row*100, 165 + 150*col, 165 + row*100, fill = '#FFFF14')
    elif char == 'O':
        canvas.create_polygon(35+150*col,85+100*row ,165+150*col,85+100*row, 165+150*col,165+100*row, 35+150*col,165+100*row , fill = '#0000CE')
        
def update_board(row,col):
    global tic_board
    char = current_player()
    tic_board [row][col] = char
    return char

def check_all():
    r = check_rows()
    c = check_cols()
    d = check_diags()
    if r==True or c==True or d==True:
        return True
    else:
        return False
       
def check_rows():
    global tic_board
    char = 'O'
    count = 0
    for i in range (2):
        for j in range (3):
            for k in range (3):
                if tic_board[j][k] == char:
                    count+=1
            if count == 3:
                return True
            else:
                count = 0
        char = 'X'
    return False

def check_cols():
    global tic_board
    char = 'O'
    count = 0
    for i in range (2):
        for j in range (3):
            for k in range (3):
                if tic_board[k][j] == char:
                    count+=1
            if count == 3:
                return True
            else:
                count = 0
        char = 'X'      
    return False

def check_diags():
    global tic_board
    char = 'O'
    count = 0
    for i in range(2):
        if tic_board[0][0] == tic_board[1][1] and tic_board[1][1] == tic_board[2][2] and tic_board[1][1]==char:
            return True
        elif tic_board[0][2] == tic_board[1][1] and tic_board[1][1] == tic_board[2][0] and tic_board[1][1]==char:
            return True
        char = 'X'

def mouseClick(event):
    global click
    end = check_all()
    if 25<event.x<475 and 75<event.y<375:
        row, col = mouse_click_to_grid(event.x,event.y)
        if click <10 and end == False:
            char = update_board(row,col)
            print_board(row, col, char)
            end = check_all()
            if end == True:
                winner = [2,1]
                canvas.create_text(250,55, text = 'Player '+ str(winner[click%2] )+' Wins', font=('Times','20', 'bold'))
 
app_frame = tk.Tk()
app_frame.geometry('500x400')
app = Application(master=app_frame)
canvas.bind('<Button>', mouseClick )
app.mainloop()

