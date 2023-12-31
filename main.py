from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(height=250,width=250)





def buton_clicked():

    kilo = entry_kilo.get()
    boy = entry_boy.get()

    if boy == "" or kilo == "":
        label_mesaj.config(text="Hatalı değer girişi")
    else:
        try:
            endeks = float(kilo) / (((float(boy) / 100) * 2))
            label_mesaj_string = sonuc_yaz (endeks)
            label_mesaj.config(text=label_mesaj_string)
        except:
            label_mesaj.config(text="Sadece sayı giriniz")


label_kilo = Label(text="Kilo Giriniz (kg)")
label_kilo.pack()
entry_kilo = Entry(width=20)
entry_kilo.pack()
label_boy = Label(text="Boy Giriniz (cm)")
label_boy.pack()
entry_boy = Entry(width=20)
entry_boy.pack()
hesapla = Button(text="Hesapla", command=buton_clicked)
hesapla.pack()
label_mesaj = Label()
label_mesaj.pack()

def sonuc_yaz(endeks):
     label_mesaj =f"VKi {round(endeks, 2)} = "
     if endeks <= 18.4:
         label_mesaj += "zayıf"
     elif endeks < 24.9:
         label_mesaj += "ideal"
     elif endeks < 30:
         label_mesaj += "kilolu"
     elif endeks < 40.1:
         label_mesaj += "obez"
     elif endeks < 50.1:
         label_mesaj += "morbiz obez"
     else:
         label_mesaj += "süper obez"
     return label_mesaj

window.mainloop()