import requests
import tkinter as t
rop= t.Tk()
rop.title("الطقس في المدن الإسلامية")
rop.geometry("500x500+300+100")
rop.configure(background="black")
yazi=t.Label(
    text="Weather in Islamic cities",
    fg="red",
    bg="black",
    width=30,
    height=3,
    font="Elephant"
)
yazi.pack()
url = 'http://wttr.in/Cairo?format=%t'
response = requests.get(url)
weather_data = response.text
print("Kahire'de hava sıcaklığı: " + weather_data.strip())
urli = 'http://wttr.in/Ankara?format=%t'
responsem = requests.get(urli)
weather_datam = responsem.text
print("Ankara'da hava sıcaklığı: " + weather_datam.strip())
urliy = 'http://wttr.in/Istanbul?format=%t'
responsemt = requests.get(urliy)
weather_datamt = responsemt.text
print("İstanbul'da hava sıcaklığı: " + weather_datamt.strip())
ur = 'http://wttr.in/Konya?format=%t'
re = requests.get(ur)
we = re.text
print("Konya'da hava sıcaklığı: " + we.strip())
urq = 'http://wttr.in/Alexandria?format=%t'
rem = requests.get(urq)
wem = rem.text
print("İskenderiye'de hava sıcaklığı: " + wem.strip())
urqw = 'http://wttr.in/Refah?format=%t'
remw = requests.get(urqw)
wemw = remw.text
print("Refah'ta hava sıcaklığı: " + wemw.strip())
u = 'http://wttr.in/Islamabad?format=%t'
r = requests.get(u)
w = r.text
print("İslamabad'ta hava sıcaklığı: " + w.strip())
up = 'http://wttr.in/Astana?format=%t'
rp = requests.get(up)
wp = rp.text
print("Nur Sultan'da hava sıcaklığı: " + wp.strip())
upm = 'http://wttr.in/Tyrant?format=%t'
rpm = requests.get(upm)
wpm = rpm.text
print("Tirana'da hava sıcaklığı: " + wpm.strip())
upmc = 'http://wttr.in/Beirut?format=%t'
rpmc = requests.get(upmc)
wpmc = rpmc.text
print("Beyrut'da hava sıcaklığı: " + wpmc.strip())
upmce = 'http://wttr.in/Baku?format=%t'
rpmce = requests.get(upmce)
wpmce = rpmce.text
print("Bakü'de hava sıcaklığı: " + wpmce.strip())
upmcet = 'http://wttr.in/Mekka?format=%t'
rpmcet = requests.get(upmcet)
wpmcet = rpmcet.text
print("Mekke'de hava sıcaklığı: " + wpmcet.strip())
upmcety = 'http://wttr.in/Sarajevo?format=%t'
rpmcety = requests.get(upmcety)
wpmcety = rpmcety.text
print("Saraybosna'da hava sıcaklığı: " + wpmcety.strip())
upmcetyq = 'http://wttr.in/Erzurum?format=%t'
rpmcetyq = requests.get(upmcetyq)
wpmcetyq = rpmcetyq.text
print("Erzurum'da hava sıcaklığı: " + wpmcetyq.strip())
upmcetyqm = 'http://wttr.in/Urumqi?format=%t'
rpmcetyqm = requests.get(upmcetyqm)
wpmcetyqm = rpmcetyqm.text
print("Urumçi'de hava sıcaklığı: " + wpmcetyqm.strip())
upmcetyqmww = 'http://wttr.in/Mansure?format=%t'
rpmcetyqmww = requests.get(upmcetyqmww)
wpmcetyqmww = rpmcetyqmww.text
print("Mansure'de hava sıcaklığı: " + wpmcetyqmww.strip())
def listeye_tikla(event):
    secilen = liste.get(liste.curselection())
    if secilen == "Kahire":
        sonuc_label.config(text="Kahire'de hava sıcaklığı: " + weather_data.strip(),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Ankara":
        sonuc_label.config(text="Ankara'da hava sıcaklığı: " + weather_datam.strip(),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Istanbul":
        sonuc_label.config(text="İstanbul'da hava sıcaklığı: " + weather_datamt.strip(),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Konya":
        sonuc_label.config(text="Konya'da hava sıcaklığı: " + we.strip(),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Alexandria":
        sonuc_label.config(text="İskenderiye'de hava sıcaklığı: " + wem.strip(),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Refah":
        sonuc_label.config(text="Refah'ta hava sıcaklığı: " + wemw.strip(),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Islamabad":
        sonuc_label.config(text="İslamabad'ta hava sıcaklığı: " + w.strip(),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Tyrant":
        sonuc_label.config(text="Nur Sultan'da hava sıcaklığı: " + wp.strip(),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Astana":
        sonuc_label.config(text="Tirana'da hava sıcaklığı: " + wpm.strip(),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Beirut":
        sonuc_label.config(text="Beyrut'da hava sıcaklığı: " + wpmc.strip(),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Baku":
        sonuc_label.config(text="Bakü'de hava sıcaklığı: " + wpmce.strip(),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Mekka":
        sonuc_label.config(text="Mekke'de hava sıcaklığı: " + wpmcet.strip(),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Sarajevo":
        sonuc_label.config(text="Saraybosna'da hava sıcaklığı: " + wpmcety.strip(),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Erzurum":
        sonuc_label.config(text="Erzurum'da hava sıcaklığı: " + wpmcetyq.strip(),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Urumqi":
        sonuc_label.config(text="Urumçi'de hava sıcaklığı: " + wpmcetyqm.strip(),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Mansure":
        sonuc_label.config(text="Mansure'de hava sıcaklığı: " + wpmcetyqmww.strip(),fg="orange",bg="black",font="Tahoma")       
liste=t.Listbox(rop)
liste.pack()
liste.insert(t.END,"Kahire")
liste.insert(t.END,"Ankara")
liste.insert(t.END,"Istanbul")
liste.insert(t.END,"Konya")
liste.insert(t.END,"Alexandria")
liste.insert(t.END,"Refah")
liste.insert(t.END,"Islamabad")
liste.insert(t.END,"Tyrant")
liste.insert(t.END,"Astana")
liste.insert(t.END,"Beirut")
liste.insert(t.END,"Baku")
liste.insert(t.END,"Mekka")
liste.insert(t.END,"Sarajevo")
liste.insert(t.END,"Erzurum")
liste.insert(t.END,"Urumqi")
liste.insert(t.END,"Mansure")
liste.insert(t.END,"")
liste.insert(t.END,"")
liste.insert(t.END,"")
liste.insert(t.END,"")
liste.insert(t.END,"")
liste.insert(t.END,"")
sonuc_label = t.Label(rop, text="",fg="green",bg="orange",font="Impact")
sonuc_label.pack()
liste.bind("<ButtonRelease-1>", listeye_tikla)
rop.mainloop()
###Hava Durumu###
#الطقس في المدن الإسلامية#
############











##################################################3












