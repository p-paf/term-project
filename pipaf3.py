from tkinter import *
from tkinter import messagebox
import math
import random
import copy

class ColumnFullException(Exception):
    pass

class state:
    def __init__(self, board=[]):
        self.board = copy.deepcopy(board)
    def start(self):
        self.board = [[0,0,0,0] for _ in range(4)]
    def terminal_test(self):
        b = self.board
        for t in [1,2]:
            for r in range(4):
                if (b[r][0]==t and b[r][1]==t and b[r][2]==t):
                    return True, int(2*(1.5-t))
                elif (b[r][3]==t and b[r][1]==t and b[r][2]==t):
                    return True, int(2*(1.5-t))
            for c in range(4):
                if (b[0][c]==t and b[1][c]==t and b[2][c]==t):
                    return True, int(2*(1.5-t))
                elif (b[1][c]==t and b[2][c]==t and b[3][c]==t):
                    return True, int(2*(1.5-t))
            if b[0][1]==t and b[1][2]==t and b[2][3]==t:
                return True, int(2*(1.5-t))
            elif b[0][0]==t and b[1][1]==t and b[2][2]==t:
                return True, int(2*(1.5-t))
            elif b[1][1]==t and b[2][2]==t and b[3][3]==t:
                return True, int(2*(1.5-t))
            elif b[1][0]==t and b[2][1]==t and b[3][2]==t:
                return True, int(2*(1.5-t))
            if b[2][0]==t and b[1][1]==t and b[0][2]==t:
                return True, int(2*(1.5-t))
            elif b[3][0]==t and b[2][1]==t and b[1][2]==t:
                return True, int(2*(1.5-t))
            elif b[2][1]==t and b[1][2]==t and b[0][3]==t:
                return True, int(2*(1.5-t))
            elif b[3][1]==t and b[2][2]==t and b[1][3]==t:
                return True, int(2*(1.5-t))
        flag = 0
        for c in range(4):
            if b[3][c] == 0:
                flag = 1    
        if flag==0:
            return True, 0
        return False, None

    def show(self, frame, images):
        for i in range(4):
            for j in range(4):
                Button(frame, command = lambda col=j: human(col), image=images[(self.board[i][j]-1) % 3]).grid(row=i, column=j)    
            
    def actions(self):
        return filter(lambda z: (self.board[3][z]==0), [0,1,2,3])

def next_state(st, action, turn):
    new = state(st.board)
    if turn == False and new.board[3][action] != 0:
        raise ColumnFullException
    else:
        tag = 1 if turn else 2
        flag = 1
        index = -1
        while flag != 0:
            index += 1
            flag = new.board[index][action]
        new.board[index][action] = tag
    return new

def minimax(st, turn):
    global bottom_frame, imgs
    if st.terminal_test()[0]:
        return st.terminal_test()[1], None
    best = -math.inf if turn else math.inf
    for a in st.actions():
        t = next_state(st, a, turn)
        ut, ac = minimax(t, not turn)
        if (turn) and (ut > best):
            best, act = ut, a
        elif (not turn) and (ut < best):
            best, act = ut, a
    return best, act

def minimax_move():
    global st, bottom_frame, imgs, l, chance
    msgs = ['It was a draw', 'You lost miserably', 'you won']
    if chance == False:
        messagebox.showinfo("Out of Chance", "Please make a human move.")
        return
    chance = False if chance == None else not chance
    ut, act = minimax(st, True)
    st = next_state(st, act, True)
    st.show(bottom_frame, imgs)
    if st.terminal_test()[0]:
        messagebox.showinfo('Game Over', msgs[st.terminal_test()[1]])
        sys.exit()

def human(column):
    msgs = ['It was a draw', 'You lost miserably', 'you won']
    global chance
    if chance == True:
        messagebox.showinfo("Out of Chance", "Please allow machine to move.")
        return
    try:
        global st, bottom_frame, imgs, l
        st = next_state(st, column, False)
        st.show(bottom_frame, imgs)
    except ColumnFullException as e:
        messagebox.showinfo("Column Full", "Please try another column.")
        return
    if chance == None:
        chance = True
    else:
        chance = not chance
    if st.terminal_test()[0]:
        messagebox.showinfo('Game Over', msgs[st.terminal_test()[1]])
        sys.exit()

if __name__ == "__main__":
    chance = None
    st = state()
    st.start()
    w = Tk()
    w.title("Pipaf3")
    imgs = [PhotoImage(file = f) for f in ['green_blob.png', 'blue_blob.png', 'white_blob.png', 'base_line.png']]
    top_frame = Frame(w)
    top_frame.pack(side=TOP)
    bottom_frame = Frame(w)
    bottom_frame.pack(side=TOP)
    b0 = Button(top_frame,text="Minimax Move", command = lambda: minimax_move(), bg="orange", fg="red")
    b0.pack(side=TOP)
    bbase = Label(top_frame, image=imgs[3])
    bbase.pack(side=TOP)
    st.show(bottom_frame, imgs)
    w.mainloop()