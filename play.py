from tkinter import Tk, Label, Button, PhotoImage, messagebox, TOP, Frame

from state import State, ColumnFullException, WrongTurnException

def render_board(game, frame, imgs):
    pick_img = {
        0: imgs[2],
        State.HUMAN: imgs[1],
        State.COMPUTER: imgs[0]
    }

    for i in range(4):
        for j in range(4):
            Button(frame, command = lambda col=j: human_move(game, frame, imgs, col), image=pick_img[game.board.check(i, j)]).grid(row=i, column=j)    

def ai_move(game, frame, imgs):
    try:
        game.ai_choice()
    except WrongTurnException as e:
        messagebox.showwarning('Warning', 'Let the human play')

    render_board(game, frame, imgs)

    if game.win():
        messagebox.showinfo('GG', 'Computer wins')

def human_move(game, frame, imgs, col):
    try:
        game.human_choice(col)
    except ColumnFullException as e:
        messagebox.showwarning('Warning', 'Can\'t choose this column')
    except WrongTurnException as e:
        messagebox.showwarning('Warning', 'Let the computer play')

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
