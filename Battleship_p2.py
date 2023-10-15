#-1: miss, 0: unplayed, 1: ship hit
# yellow, gray, red
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pickle,time
window = Tk()
window.configure(bg='black')
ttk.Separator(window, orient='vertical').place(relx=0.5, rely=0, relwidth=0.009, relheight=1)
o = lambda a:a/1536
p = lambda a:a/888
fonts = lambda a:("Inter ExtraBold", a * -1,'bold')
window.title("PLAYER 2")
Label(window,text='Defence',font=fonts(64),fg='white',bg='black').place(relx=o(100),rely=p(100))
pos={}
turn=2
funccheck=0
found=0
valid=bool
validated=False
def wincon():
    global found
    if found >=17:
        with open('winner.dat','wb') as f:
            pickle.dump(2,f)
            messagebox.showinfo("WON","Congratulations You have succesfully found all your opponent's ships. Well Done")
def wincheck():
    try:
        with open('winner.dat','rb') as f:
                pickle.load(f)
                messagebox.showerror("LOST","Your Opponent has succesfully found all your ships. Better luck next time")
                window.destroy()
        return('L')
    except:pass
for i in 'ABCDEFGHIJ':
    pos[i]=([0 for i in range((10))])
def writepos(pos2):
    with open('p2pos.dat','wb+') as f:
        pickle.dump(pos2,f)
    with open('p2pos.txt','w+') as f:
        f.write(f'{pos2}')
    #print(pos)
writepos(pos)
#defence
#------------------------------------------------------------------------------------------------
c=1
for  j in range(200+20,700+20,50):
    d=65
    for i in range(100,600,50):
        h=f'{chr(d)}{c}'
        exec(f'global {h}')
        exec(f'{h} = Button(window,font=("Inter ExtraBold", 20 * -1,"bold"),text="{chr(d)}{c}")')
        exec(f'{h}.place(relx=o(i),rely=p(j),width=50,height=50)')
        d+=1
    c+=1
#------------------------------------------------------------------------------------------------    
#funtion assignment
def muppet():
    c=1
    for  j in range(200-20,700-50,50):
        d=65
        for i in range(100,600,50):
            h=f'{chr(d)}{c}'
            exec(f'''def sub{h}():
                 global funccheck,validated
                 if validated == False:
                    funccheck +=1
                    #print(funccheck)
                    if funccheck<=17:
                        if pos["{h[0]}"][{h[1:]}-1] != 1:
                            pos["{h[0]}"][{h[1:]}-1] = 1
                            {h}.configure(bg="green")
                            if funccheck==17:
                                writepos(pos)
                        else:funccheck-=1
                    else:
                        validated=True
                    ''')
            exec(f'{h}.configure(command= sub{h})')
            d+=1
        c+=1
muppet()
#------------------------------------------------------------------------------------------------    
#offence
Label(window,text='Offence',font=fonts(64),fg='white',bg='black').place(relx=o(900),rely=p(100))
def changecolor(but):
        global found
        with open('p1pos.dat','rb') as f:
            a=pickle.load(f)
        exec(f'{but}.configure(bg="red")') if a[but[0]][int(but[1:-1])-1] !=0 else exec(f'{but}.configure(bg="dark gray")')
        found+=1 if a[but[0]][int(but[1:-1])-1] !=0 else 0
c=1
for  j in range(200+20,700+20,50):
    d=65
    for i in range(900,1400,50):
        h=f'{chr(d)}{c}2'
        exec(f'global {h}')
        exec(f'{h} = Button(window,font=("Inter ExtraBold", 20 * -1,"bold"),text="{chr(d)}{c}")')
        exec(f'{h}.place(relx=o(i),rely=p(j),width=50,height=50)')
        d+=1
    c+=1
def writeturn(tune):
    with open('player_turn.dat','wb')as f:
        pickle.dump(tune,f)
    with open('player_turn.txt','w')as f:
        f.write(f'{tune}')
def checkturn():
    with open('player_turn.dat','rb')as f:
        return(pickle.load(f))
def muppet2():
    c=1
    for j in range(10):
        d=65
        for i in range(10):
            h=f'{chr(d)}{c}2'
            exec(f'''def sub{h}():
                    if wincheck() != 'L':
                        wincon()
                        if checkturn()==2:
                            changecolor("{h}")
                            writeturn(1)
                        else:
                            messagebox.showerror("OPPONENT'S TURN","Please wait for your turn")
                        ''')
            exec(f'{h}.configure(command= sub{h})')
            d+=1
        c+=1
muppet2()
window.attributes('-fullscreen',True)
window.bind('<Escape>',lambda a: window.destroy())
window.mainloop()
