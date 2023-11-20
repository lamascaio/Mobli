from tkinter import *
import webbrowser

janela = Tk()
janela.title("MOBLI")

img = PhotoImage(file="mobli2.png")
imagem = Label(janela, image=img, width=500, height=170).pack()

texto = Label(janela, text="LOGIN:", bg="black", fg="white", font='Arial 25 bold italic', width=10,)
texto.place(x=20, y=300)

entrada = Entry(janela, width=40)
entrada.place(x=200, y=300, height=35)

texto1 = Label(janela, text="SENHA:", bg="black", fg="white", font='Arial 25 bold italic', width=10,)
texto1.place(x=20, y=380)

entrada1 = Entry(janela, width=40)
entrada1.place(x=200, y=380, height=35)

login = "Caio"
senha = "123"

def entrar():
    if entrada.get() == login and entrada1.get() == senha:
        texto6 = Label(janela, text="Login efetuado com sucesso!", bg="black", fg="green", font='Arial 14', width=30)
        texto6.place(x=155, y=500)
        
        janela1 = Tk()
        janela1.title("MOBLI")
        
        #img1 = PhotoImage(file="mobli3.png")
        #imagem1 = Label(janela1, image=img1, width=500, height=170).pack()
        
        texto2 = Label(janela1, text="  Veja a sua localização!  ", bg="black", fg="white", font='Arial 25 bold italic', width=18,)
        texto2.place(x=80, y=100)
        
        def loc():
            webbrowser.open('https://maps.app.goo.gl/ezcrbHeTBSMCpo6J8')
            
        botao1 = Button(janela1, command=loc, text="Ver localização", width=14, height=2)
        botao1.place(x=200, y=150)
        
        texto3 = Label(janela1, text="Coloque sua localização aqui:", bg="black", fg="white", font='Arial 15')
        texto3.place(x=130, y=200)
        
        entrada3 = Entry(janela1, width=40)
        entrada3.place(x=130, y=250, height=30)
        
        def enviar():
            print(entrada3.get())
            
            texto5 = Label(janela1, text="Enviado com sucesso!", bg="black", fg="green", font='Arial 15')
            texto5.place(x=150, y=350)
            
        botao2 = Button(janela1, command=enviar, text="Enviar", width=14, height=2)
        botao2.place(x=200, y=300)
        
        janela1.config(bg="black")
        janela1.geometry("500x800")
        janela1.mainloop()
        
    else:  texto7 = Label(janela, text="Login ou senha errado!", bg="black", fg="red", font='Arial 14', width=30)
    texto7.place(x=155, y=500)

botao = Button(janela, command=entrar, text="ENTRAR", width=14, height=2)
botao.place(x=260, y=450)

janela.config(bg="black")
janela.geometry("500x800")
janela.mainloop()