from tkinter import *
from math import *



class Calculadora:
    def __init__(self, toplevel):
        toplevel.title('Calculadora')
        toplevel.geometry("300x200")

        self.frame1 = Frame(toplevel)
        self.frame1.pack()

        self.frame2 = Frame(toplevel)
        self.frame2.pack()
        
        self.frame3 = Frame(toplevel)
        self.frame3.pack()

        self.frame4 = Frame(toplevel, pady=12)
        self.frame4.pack()

        self.frame5 = Frame(toplevel)
        self.frame5.pack()

        self.frame6 = Frame(toplevel, pady=12)
        self.frame6.pack()

        Label(self.frame1,text='', fg='black',
        font=('Verdana','10'), height=1).pack()
        fonte1=('Verdana','10')

        somar=Button(self.frame4,font=fonte1,text='+',command=self.somar)
        somar.pack(side=LEFT)
        
        subtrair=Button(self.frame4,font=fonte1,text='-',command=self.subtrair)
        subtrair.pack(side=LEFT)

        multiplicar=Button(self.frame4,font=fonte1,text='*',command=self.multiplicar)
        multiplicar.pack(side=LEFT)

        dividir=Button(self.frame4,font=fonte1,text='/',command=self.dividir)
        dividir.pack(side=LEFT)

        raiz=Button(self.frame4,font=fonte1,text='raiz',command=self.raiz)
        raiz.pack(side=LEFT)

        limpar=Button(self.frame4,font=fonte1,text='Limpar',command=self.limpar)
        limpar.pack(side=LEFT)

        sair=Button(self.frame4,font=fonte1,text='Sair',command=self.sair)
        sair.pack(side=LEFT)

        Label(self.frame2,text='Valor1: ',font=fonte1,width=8).pack(side=LEFT)
        self.valor1=Entry(self.frame2,width=10,font=fonte1)
        self.valor1.focus_force()
        self.valor1.pack(side=LEFT)

        Label(self.frame3,text='Valor2: ', font=fonte1, width=8).pack(side=LEFT)
        self.valor2=Entry(self.frame3,width=10,font=fonte1)
        self.valor2.pack(side=LEFT)

        Label(self.frame5,text=' = ', font=fonte1, width=8).pack(side=LEFT)
        self.msg=Label(self.frame5, width=10,font=fonte1)
        self.msg.pack(side=LEFT)

    def somar(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)

        r = valor1+valor2
        r = float(r)
        self.msg['text'] = '%.2f'%(r)

    def subtrair(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        r = valor1-valor2
        r = float(c)

        self.msg['text'] = '%.2f' %(r)

    def multiplicar(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        r = valor1*valor2
        r = float(r)
        self.msg['text'] = '%.2f' %(r)

    def dividir(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        r = valor1/valor2
        r = float(r)
        self.msg['text'] = '%.2f' %(r)

    def raiz(self):
        try:
            valor1 = self.valor1.get()
            valor1 = float(valor1)
            r = sqrt(valor1)
            r = float(r)
            self.msg['text'] = '%.2f' %(r)

        except:
            valor2 = self.valor2.get()
            valor2 = float(valor2)
            r = sqrt(valor2)
            r = float(r)
            self.msg['text'] = '%.2f' %(r)

    def limpar(self):
        pass

    def sair(self):
        app.destroy()


app = Tk()
Calculadora(app)
app.mainloop()




    











