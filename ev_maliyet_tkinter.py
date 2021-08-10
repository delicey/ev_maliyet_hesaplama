from tkinter import *
from tkinter import messagebox
import tkinter as tk

#
cimento_kg = 35
kum_kg = 8
boya_kg = 6
ıslak_zemin_m2 = 500
iscilik = 700

def sonucGoster(sonuc):
    #print(metrekare.get())
    #print(int(metrekare.get()))
    messagebox.showinfo("Sonuç",sonuc)



def hesapYap():

    cimento_bedeli=(int(metrekare.get()))*3*cimento_kg
    kum_bedeli=(int(metrekare.get()))*10*kum_kg
    boya_bedeli=(int(metrekare.get()))*boya_kg
    ıslak_zemin_bedeli=(int(metrekare.get()))/15*ıslak_zemin_m2
    iscilik_bedeli=(int(metrekare.get())/10)*iscilik




    son="""
{} bölgesinde inşa edilecek net {:.0f} metrekare ve {} kalitedeki evinizin maliyeti:
 
Çimento bedeli: {:.2f} TL
Kum bedeli: {:.2f} TL
Boya bedeli: {:.2f} TL
Islak Zemin Bedeli: {:.2f} TL
İşçilik Bedeli: {:.2f} TL
Toplam: {:.2f} TL""".format(muhit5,((int(metrekare.get()))/100)*90,kalite5,cimento_bedeli,kum_bedeli,boya_bedeli,ıslak_zemin_bedeli,iscilik_bedeli,cimento_bedeli+kum_bedeli+boya_bedeli+ıslak_zemin_bedeli+iscilik_bedeli)
    sonucGoster(son)

#
def muhitSec():
    global cimento_kg
    global kum_kg
    global boya_kg
    global ıslak_zemin_m2
    global iscilik
    global muhit5

    if m.get()==1:
        cimento_kg += (cimento_kg / 4)
        kum_kg += (kum_kg / 4)
        boya_kg += (boya_kg / 4)
        ıslak_zemin_m2 += (ıslak_zemin_m2 / 4)
        iscilik += (iscilik / 4)
        muhit5="Bağlıca"
    elif m.get()==3:
        cimento_kg += (cimento_kg / 5)
        kum_kg += (kum_kg / 5)
        boya_kg += (boya_kg / 5)
        ıslak_zemin_m2 += (ıslak_zemin_m2 / 5)
        iscilik += (iscilik / 5)
        muhit5="Yapracık"
    elif m.get()==4:
        cimento_kg -= (cimento_kg / 5)
        kum_kg -= (kum_kg / 5)
        boya_kg -= (boya_kg / 5)
        ıslak_zemin_m2 -= (ıslak_zemin_m2 / 5)
        iscilik -= (iscilik / 5)
        muhit5="Yenimahalle"
    else:
        muhit5="Eryaman"
def kaliteSec():
    global cimento_kg
    global kum_kg
    global boya_kg
    global ıslak_zemin_m2
    global iscilik
    global kalite5

    if k.get()==1:
        cimento_kg += (cimento_kg / 5)
        kum_kg += (kum_kg / 5)
        boya_kg += (boya_kg / 5)
        ıslak_zemin_m2 += (ıslak_zemin_m2 / 5)
        iscilik += (iscilik / 5)
        kalite5="yüksek"

    elif k.get()==3:
        cimento_kg -= (cimento_kg / 5)
        kum_kg -= (kum_kg / 5)
        boya_kg -= (boya_kg / 5)
        ıslak_zemin_m2 -= (ıslak_zemin_m2 / 5)
        iscilik -= (iscilik / 5)
        kalite5="ekonomik"
    else:
        kalite5="orta"


###

pencere=tk.Tk()
pencere.title("Ev Maliyeti Hesaplama Programı")
pencere.geometry("600x600+370+80")

###
baslik=tk.Label(text="Developer Ceysun", font="Calibri 20 bold italic", fg="yellow",bg="#000000")
baslik.pack()

soru1=Label(text="1) Ankara'da inşa etmek istediğiniz ev için bir muhit seçiniz",font="Verdana 10 bold",fg="#FF0000")
soru2=Label(text="2) İnşaat için kullanılacak malzemenin kalitesini seçiniz",font="Verdana 10 bold",fg="#FF0000")
soru3=Label(text="3) İnşa edeceğiniz evin brüt metrekaresini giriniz",font="Verdana 10 bold",fg="#FF0000")
soru3_aciklama=Label(text="(Not: Evinizin net metrekaresi brüt değerden %10 düşük olarak hesaplanacaktır.)",font="Verdana 8 bold italic",fg="#000000")
metrekare_aciklama=Label(text="metrekare",font="Verdana 8")
soru1.place(x=20,y=60)
soru2.place(x=20,y=140)
soru3.place(x=20,y=220)
metrekare_aciklama.place(x=80,y=280)
soru3_aciklama.place(x=20,y=240)


m=IntVar()

muhit1=Radiobutton(text="Bağlıca", variable=m, value=1,command=muhitSec)
muhit2=Radiobutton(text="Eryaman", variable=m, value=2,command=muhitSec)
muhit3=Radiobutton(text="Yapracık", variable=m, value=3,command=muhitSec)
muhit4=Radiobutton(text="Yenimahalle", variable=m, value=4,command=muhitSec)
muhit1.place(x=20, y=100)
muhit2.place(x=150, y=100)
muhit3.place(x=280, y=100)
muhit4.place(x=410, y=100)

k=IntVar()
kalite1=Radiobutton(text="Yüksek", variable=k, value=1,command=kaliteSec)
kalite2=Radiobutton(text="Orta", variable=k, value=2,command=kaliteSec)
kalite3=Radiobutton(text="Ekonomik", variable=k, value=3,command=kaliteSec)
kalite1.place(x=20, y=180)
kalite2.place(x=150, y=180)
kalite3.place(x=280, y=180)
###

metrekare=tk.Entry(width=8)
metrekare.place(x=20,y=280)
metrekare2=metrekare.get()

hesapla=Button(text="HESAPLA",font="Verdana 16 bold",fg="#0000FF",bg="pink",command=hesapYap)
hesapla.place(x=240,y=450)



pencere.mainloop()