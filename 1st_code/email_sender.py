import smtplib
from tkinter import *

bg = '#f1c159'
fg = '#2b2b2b'
sender = ''
password = 'Sender_password'


def send_mail(reciver, message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender, password)
    s.sendmail(sender, reciver, password)
    s.quit()


root = Tk()
root.geometry('500x400')
root.configure(bg=bg)
root.title('Mail Sender - Pratik_Khanna')

Label(root, text='Email Sender:', font=('', 40), fg=fg, bg=bg).place(x=120, y=10)
Label(root, text='Send To:', font=('', 20), fg=fg, bg=bg).place(x=30, y=70)
Label(root, text='Message:', font=('', 20), fg=fg, bg=bg).place(x=25, y=210)

rec_name = Entry(root, font=('', 17), width=30)
rec_name.place(x=120, y=70)

msg = Text(root, height=10, width=30, font=('', 17))
msg.place(x=120, y=110)

Button(root, text=' Send ', font=('', 20), fg=fg,
       command=lambda:send_mail(rec_name.get(), msg.get('1.0', END))).place(x=120, y=330)

root.mainloop()
