from tkinter import *


main = Tk()
main.geometry("1000x800")
main.title("Mailer")
photo = PhotoImage(file="Logo.png")
main.iconphoto(False,photo)

#user stettings 
from User import User
u = User(main)
butt1 = Button(main,text="User Settings",height=10,width=50,font=("Roman",13,"bold"),bg="#f59207",fg="#db3c18",command=u.user_db)
butt1.pack(pady=20)

#Send Mail


from mail_send import mail_send
m = mail_send(main)

butt2 = Button(main,text="Send Mail",height=10,width=50,font=("Roman",13,"bold"),bg = "#10b328",fg="#056e25",command=m.send_mails)
butt2.pack(pady=20)

#Read mail
from mail_read import mail_read
m = mail_read(main)
butt3 = Button(main,text="Read",height=10,width=50,font=("Roman",13,"bold") ,bg = "#0dd6c2",fg="#0e078f",command=m.mail_reads)
butt3.pack(pady=20)

main.mainloop()
