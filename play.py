import random

from tkinter import Tk, Label, Button, PhotoImage, messagebox, TOP, Frame
from state import State, ColumnFullException, WrongTurnException, FilledTileException

def render_board(game, frame, imgs):
    pick_img = {
        0: imgs[2],
        State.HUMAN: imgs[1],
        State.COMPUTER: imgs[0]
    }

    for row in range(5):
        for col in range(5):
            if row == 4 or col == 4:
                Button(frame, command = lambda col=row: dance(row), image=random.choice(imgs[0:3])).grid(row=row, column=col)    
            else:
                Button(frame, command = lambda row = row, col = col: human_move(game, frame, imgs, row, col), image=pick_img[game.board.check(row, col)]).grid(row=row, column=col)    

def dance(row):
    messagebox.showinfo('Just dance', 'Just dance at ' + str(row))
    return


def ai_move(game, frame, imgs):
    try:
        # changes game board state
        game.ai_choice()
    except WrongTurnException as e:
        messagebox.showwarning('Warning', 'Let the human play')

    # renders changed state
    render_board(game, frame, imgs)

    if game.win():
        messagebox.showinfo('GG', 'Computer wins')

def human_move(game, frame, imgs, row, col):
    try:
        # changes the board values
        game.human_choice(row, col)
    except ColumnFullException as e:
        messagebox.showwarning('Warning', 'Can\'t choose this column')
    except WrongTurnException as e:
        messagebox.showwarning('Warning', 'Let the computer play')
    except FilledTileException as e:
        messagebox.showwarning('Warning', 'This tile is already filled')

    # renders the board again with the changed values
    render_board(game, frame, imgs)

    if game.win():
        messagebox.showinfo('GG', 'Human wins')

if __name__ == "__main__":
    game = State.new()

    # create tkinter window
    win = Tk()
    win.title("PPAF - Align 3 game")
    imgs = [PhotoImage(file = f) for f in ['green_blob.png', 'blue_blob.png', 'white_blob.png', 'base_line.png']]

    # align frames
    top_frame = Frame(win)
    top_frame.pack(side=TOP)
    bottom_frame = Frame(win)
    bottom_frame.pack(side=TOP)

    # add buttons
    b0 = Button(top_frame,text="Minimax Move", command = lambda: ai_move(game, bottom_frame, imgs), bg="orange", fg="red")
    b0.pack(side=TOP)
    bbase = Label(top_frame, image=imgs[3])
    bbase.pack(side=TOP)

    render_board(game, bottom_frame, imgs)
    win.mainloop()
