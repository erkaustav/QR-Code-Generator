from tkinter import *
import qrcode
import resizeimage.resizeimage
from PIL import Image, ImageTk
from resizeimage import resizeimage
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("800x500+200+50")
        self.root.title("QR Code Generator   ||  Developed By Ksuatav")
        self.root.resizable(False,False)

        title= Label(self.root,text="QR CODE GENERATOR",font=("times new roman",20),bg='#053246',fg='white').place(x=0,y=0,relwidth=1)

#       =========link details=======
#         ======variebles======
        self.var_link= StringVar()
        lnk_Frame=Frame(self.root,bd=2,relief=RIDGE)
        lnk_Frame.place(x=50,y=120,width=380,height=250)
        lnk_title = Label(lnk_Frame,text="Link Details",font=("goudy old style", 15),bg='#043256',fg='white').place(x=0, y=0, relwidth=1)

        lbl_lnk_title = Label(lnk_Frame, text="Link", font=("times new roman", 11,'bold'), bg='white').place(x=20, y=60)

        txt_lnk_title = Entry(lnk_Frame, font=("times new roman", 11, 'bold'),textvariable=self.var_link, bg='lightyellow').place(x=150,y=60)

        # =========button========
        # generate button
        btn_generator=Button(lnk_Frame,text='QR Generate',command=self.generate,font=('times new roman',15,'bold'),bg='#2196f3',fg='white').place(x=30,y=150)
#         cancel button
        btn_generator = Button(lnk_Frame, text='Clear',command=self.clear, font=('times new roman', 15, 'bold'), bg='grey',fg='white').place(x=250, y=150)

        self.msg='Generate Your QR Code'
        self.lbl_msg=Label(lnk_Frame, text=self.msg, font=("times new roman", 15), bg='white', fg='green')
        self.lbl_msg.place(x=0, y=200,relwidth=1)

        # == == == == =qr details == == == =
        qr_Frame = Frame(self.root, bd=2, relief=RIDGE)
        qr_Frame.place(x=500, y=120, width=250, height=250)
        qr_title = Label(qr_Frame, text="QR", font=("goudy old style", 15), bg='#043256', fg='white').place(x=0, y=0, relwidth=1)

        self.qr_code=Label(qr_Frame,text='No QR Code \nAvailable',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=50,width=180,height=180)

    def clear(self):
        self.var_link.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate (self):
        if self.var_link.get()=='':
            self.msg='URL Not Found'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"URL : {self.var_link.get()}")
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("url_qr"+'.png')
            # ====image update====
            self.image=ImageTk.PhotoImage(file="url_qr"+'.png')
            self.qr_code.config(image=self.image)

            # ====updating notification=====
            self.msg='QR Generated Successfully!'
            self.lbl_msg.config(text=self.msg, fg='green')
     



root=Tk()
obj= Qr_Generator(root)
root.mainloop()