from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow


class chatbot:
    def __init__(self,root):
        self.root=root             #root taiyar kiya hai
        self.root.title("CHATBOT")  #root ka name diya hai
        self.root.geometry("730x620+0+0")  #window ki hight width x axis y axis diya hai
        self.root.bind("<Return>",self.enter_fun)


# title banana hai

        main_frame=Frame(self.root,bd=4,bg="powder blue",width=730)  # frame baba rahe hai self.root ke andar 
        main_frame.pack()  #pack karne se window hamari responsive ho jati hai



        img_chat=Image.open("chatbot image.jpg") #image provide kar rahe hai
        img_chat=img_chat.resize((200,80),Image.ANTIALIAS)# image ko risize kar raha hai
        self.photoimage=ImageTk.PhotoImage(img_chat)  #iske andar cahtbot wali image ko dalna hai



        # ab image ko label ki madat se dalna hai

        Title_label=Label(main_frame,bd=4,relief=RAISED,anchor="nw",width=730,compound=LEFT,image=self.photoimage,text="CHAT ME",font=("arial",40,"bold"),fg="red",bg="black")#main_frame me label banayenge
        Title_label.pack(side=TOP)



        #ab scrollbar aur text frame banayenge


        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)  # ttk ke andar thode stylish hote hai scrollbar ye sab main frame ke andar hoga
        self.text=Text(main_frame,width=60,height=18,bd=4,relief=RAISED,font=("arial",20),fg="black",bg="white",yscrollcommand=self.scroll_y.set)#scroll ko connect karne ke liye command data hai
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        # botton banana hai aur entry box AUE SEND BUTTON BANANA HAI

        btn_frame=Frame(self.root,bd=4,bg="white",width=730,height=40)
        btn_frame.pack()

        # label banana hai footer ki


        label_1=Label(btn_frame,text="type something",font=("arial",14,"bold"),fg="green",bg="white")
        label_1.grid(row=0,column=0,padx=5,sticky=W)


        # entry box bana rahe hai
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=("times new roman",14,"bold"))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        #button banayen ge


        self.send=Button(btn_frame,text="send",font=("arial",16,"bold"),command=self.send,width=8,bg="green")
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        # clear button

        self.clear=Button(btn_frame,text="clear chat",font=("arial",16,"bold"),command=self.clear,width=8,bg="blue")
        self.clear.grid(row=0,column=3,padx=5,sticky=W)


        self.msg=""
        self.label_2=Label(btn_frame,text=self.msg,font=("arial",10,"bold"),fg="red",bg="white")
        self.label_2.grid(row=1,column=1,padx=3,sticky=W)
        


        



        #### function declearation
    def enter_fun(self,event):
        self.send.invoke()
        self.entry.set("")

    def clear(self):
        self.text.delete("1.0" , END)
        self.entry.set("")

    def send(self):
      if (self.entry.get()!=""):   
            send="\t\t\t\t\t"+"you:  "+self.entry.get()
            self.text.insert(END,"\n\n"+send)
            self.text.yview(END)
            


            if (self.entry.get()==""):
                self.msg="please enter some input"
                self.label_2.config(text=self.msg,fg="red")



            if (self.entry.get()=="hi"):
                self.text.insert(END,"\n\n"+"Bot:Hello")


            elif (self.entry.get()=="Hello"):
                self.text.insert(END,"\n\n"+"Bot:Hi")
       
            

            elif (self.entry.get()=="how are you"):
                self.text.insert(END,"\n\n"+"Bot:fine and you")    
            


            elif (self.entry.get()=="i am good"):
                self.text.insert(END,"\n\n"+"Bot:i hope you enjoy using me")    
            

            elif (self.entry.get()=="yes i enjoy"):
                self.text.insert(END,"\n\n"+"Bot:you know python")    
            

            elif (self.entry.get()=="ya python is dynamic language"):
                self.text.insert(END,"\n\n"+"Bot:you understand python")


            elif (self.entry.get()=="ya i understude"):
                self.text.insert(END,"\n\n"+"Bot:ok bye")
               


            elif (self.entry.get()=="ya bye tc "):
                self.text.insert(END,"\n\n"+"Bot:you too")


            else:
                self.text.insert(END,"\n\n"+"Bot:i did't get it")
        
      else:
          self.msg="please enter some input"
          self.label_2.config(text=self.msg,fg="red")

                    
                    


            
                   
                        
        


        

        
         
         









if __name__ == '__main__':
    root=Tk()
    shivam=chatbot(root) #class ka object banaya hai shivam name se
    root.mainloop()#mainloop ka use hai window open ho aur mere close karne par hi close ho
    
