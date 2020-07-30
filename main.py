from tkinter import *
import tkinter.messagebox
import gym
import gym_tictactoe
import copy
from tkinter import messagebox
import os

###################### Utilities ######################
def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def minimax(env, isMax, alpha, beta):
    state = env.state_vector
    flag = sum([1 for s in state if s == 0])
    if flag == 0:
        return 0
    
    if isMax:
        max_ev = -10000
        for i, state_ in enumerate(state):
            if state_ == 0:
                env_f = copy.deepcopy(env)
                state, reward, done, infos = env_f.step(i, 1)
                if done:
                    env_f = copy.deepcopy(env)
                    return reward
                max_ev = max(max_ev, minimax(env_f, ~isMax, alpha, beta)) 
                env_f = copy.deepcopy(env)
                
                alpha = max(alpha, max_ev)
                if beta <= alpha:
                    break
        return max_ev 
    
    if ~isMax:
        min_ev = 10000
        for i, state_ in enumerate(state):
            if state_ == 0:
                env_f = copy.deepcopy(env)
                state, reward, done, infos = env_f.step(i, -1)
                if done:
                    env_f = copy.deepcopy(env)
                    return -reward
                min_ev = min(min_ev, minimax(env_f, ~isMax, alpha, beta))
                env_f = copy.deepcopy(env)
                
                beta = min(beta, min_ev)
                if beta <= alpha:
                    break
        return min_ev 

def bestaction(env, state):
    best_action = -10000
    best_reward = -10000
    for i, state_ in enumerate(state):
        if state_ == 0:
            env_f = copy.deepcopy(env)
            state, reward, done, infos = env_f.step(i, 1)
            #print(i, reward, minimax(env_f, False))
            if done:
                reward = reward 
            else:
                reward = reward + minimax(env_f, False, -100000, 10000)
            
            if reward > best_reward:
                best_action = i
                best_reward = reward
            env_f = copy.deepcopy(env)
            
    return best_action#, best_reward

def AI_Move(action):
	if action == 1:
		btnClick(button1, 1)
	
	if action == 2:
		btnClick(button2, 2)
	
	if action == 3:
		btnClick(button3, 3)

	if action == 4:
		btnClick(button4, 4)

	if action == 5:
		btnClick(button5, 5)

	if action == 6:
		btnClick(button6, 6)

	if action == 7:
		btnClick(button7, 7)

	if action == 8:
		btnClick(button8, 8)

	if action == 9:
		btnClick(button9, 9)

def btnClick(buttons, button_id):
	global bclick, flag, player2_name, player1_name, playerAI, playerA
	if buttons["text"] == " " and bclick == True:
		buttons["text"] = "X"
		bclick = False
		state, reward, done, infos = env.step(button_id - 1, -1)
		
		flag += 1
		
		if done:
			if reward != 10:
				#print(reward)
				messagebox.Result("Result", "Human wins!!!")
				disableButton()
				restart_program()
		
		if flag == 9:
			messagebox.Result("Result", "Tie !!!")
			disableButton()
			restart_program()

		if flag < 9:
			#print(bestaction(env, state))	
			AI_Move(bestaction(env, state)+1)
		#print(state)

	elif buttons["text"] == " " and bclick == False:
		buttons["text"] = "O"
		bclick = True
		state, reward, done, infos = env.step(button_id - 1, 1)
		flag += 1

		if done:
			if reward != 10:
				messagebox.Result("Result", "AI wins!!!")
				disableButton()
				restart_program()

		if flag == 9:
			messagebox.Result("Result", "Tie!!!")
			disableButton()
			restart_program()
	else:
		tkinter.messagebox.Result("Tic-Tac-Toe", "Button already Clicked!")

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
###########################################################

env = gym.make('TicTacToe-v1', symbols=[-1, 1], board_size=3, win_size=3) 
state = env.reset()

tk = Tk()
tk.title("Tic Tac Toe")

playerA = StringVar()
playerAI = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player1_name.insert(0, "Human")
player1_name.config(state='disabled')
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.insert(0, "AI")
player2_name.config(state='disabled')
player2_name.grid(row=2, column=1, columnspan=8)

bclick = True
flag = 0

buttons = StringVar()
label = Label( tk, text="Player 1:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)

label = Label( tk, text="Player 2:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)

button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button1, 1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2, 2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3, 3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4, 4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5, 5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6, 6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7, 7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8, 8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9, 9))
button9.grid(row=5, column=2)

tk.mainloop()
