from tkinter import *

root = Tk()
root.title('CHATBOT')
def send():
    msg = 'You : '+ e.get()
    txt.insert(END,'\n'+msg)
    if e.get() == 'hello' or e.get()=='hi':
        txt.insert(END,'\n'+'ROBOT : '+"Hi, Darliing, how are you?")
    elif e.get() == 'how are you Baby?' or e.get()=='how are you?':
        txt.insert(END,'\n'+'ROBOT : '+"Fine Baby, and you!!")
    elif e.get() == 'thank you' or e.get()=='me too, thank you':
        txt.insert(END,'\n'+'ROBOT : '+"Okaaay, So how was your day?")
    elif e.get() == 'commands' or e.get()=='Commands':
        txt.insert(END,'\n'+'COMMANDS <<" '+'hello/hi/how are you Baby?/how are you?/thank you/me too, thank you/'
                                            +'commands/Commands/good/good, and you?/bad/bad day/idk/nothing ">>')
    elif e.get() == 'good' or e.get()=='good, and you?':
        txt.insert(END,'\n'+'ROBOT : '+"me too, So goood")
    elif e.get() == 'bad' or e.get()=='bad day':
        txt.insert(END,'\n'+'ROBOT : '+"Oh, i feel sad for you, tell ma what's happend??")
    elif e.get() == 'idk' or e.get()=='nothing':
        txt.insert(END,'\n'+'ROBOT : '+"Okay, i really understand you")
    else:
        txt.insert(END,'\n'+'ROBOT : '+"Wellll, I really didn't understand you,"
                                       +" because i am not programming yet to answer that question,"
                                        +" i feel sorry for you ;("
                                         +", please check the possible commands by taping 'commands' "
                                          +"in the messages bar :)")
    e.delete(0,END)

txt = Text(root)
l = Label(root,text='My name is ROBOT, Talk to me',fg='yellow',bg='blue')
e = Entry(root,width=100)
send = Button(root,text='send',fg='white',bg='blue',command=send)

l.grid(row=0,column=0,columnspan=2,pady=10)
txt.grid(row= 1,column=0,columnspan=2)

e.grid(row=2,column=0)
send.grid(row=2,column=1)
root.mainloop()