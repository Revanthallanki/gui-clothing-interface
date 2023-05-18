from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import urllib.request


def message():
    messagebox.showinfo("confirmation","Your Order Confirmed Successfully")
def lastwindow():
    rootla=Toplevel(root)
    rootla.geometry('500x400')
    label1=Label(rootla,text="Full Name:",font=("times to roman",10)).place(x=30,y=20)
    entry1=Entry(rootla,width=30).place(x=200,y=20)

    label2=Label(rootla,text="Phone Number:",font=("times to roman",10)).place(x=30,y=50)
    entry2=Entry(rootla,width=30).place(x=200,y=50)

    label3 = Label(rootla, text="Pincode:", font=("times to roman", 10)).place(x=30, y=80)
    entry3 = Entry(rootla, width=30).place(x=200, y=80)

    label4 = Label(rootla, text="State:", font=("times to roman", 10)).place(x=30, y=110)
    entry4 = Entry(rootla, width=30).place(x=200, y=110)

    label5 = Label(rootla, text="City:", font=("times to roman", 10)).place(x=30, y=140)
    entry5 = Entry(rootla, width=30).place(x=200, y=140)

    label6 = Label(rootla, text="Area,Colony:", font=("times to roman", 10)).place(x=30, y=170)
    entry6 = Entry(rootla, width=30).place(x=200, y=170)

    button=Button(rootla,text="Book Order",width=50,height=2,font=("times to roman",12),command=message).place(x=20,y=330)


    rootla.mainloop()


#  FOR SHIRTS COLLECTIONS
def for_shirts():
    root1=Toplevel(root)
    root1.title("men's shirts collections")
    root1.config(bg="black")
    w,h=root1.winfo_screenwidth(),root1.winfo_screenheight()
    root1.geometry('%dx%d+0+0' % (w,h))

    # FOR FIRST SHIRT

    url = "https://tse1.mm.bing.net/th?id=OIP.4Gg91OenxtQy-RZL14XGXgHaJ3&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    first= Image.open("kis.jpg")
    refirst = first.resize((205, 275))


    firstphoto = ImageTk.PhotoImage(refirst)

    firstbut = Button(root1, image=firstphoto, borderwidth=5,command=lastwindow)
    firstbut.place(x=10, y=10)

    firstlab = Button(root1, text="WRANGLER\nCollar Neck Causual Shirt\n496/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    firstlab.place(x=20, y=300)

    # FOR SECOND SHIRT

    url = "https://tse1.mm.bing.net/th?id=OIP.oeu5HMUS7vIFDwYHix45EgHaJ4&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    second = Image.open("kis.jpg")
    resecond = second.resize((205, 275))

    secondphoto = ImageTk.PhotoImage(resecond)

    secondbut = Button(root1, image= secondphoto, borderwidth=5,command=lastwindow)
    secondbut.place(x=260, y=10)

    secondlab = Button(root1,text="BLACKBERRYS\nMens Formal Full Sleeve\n1549/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    secondlab.place(x=270, y=300)

    # FOR THIRD SHIRT

    url = "https://tse3.mm.bing.net/th?id=OIP.Z7R1taOTHt8dtpa-AEBrwAHaKL&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    third = Image.open("kis.jpg")
    rethird = third.resize((205, 275))

    thirdphoto = ImageTk.PhotoImage(rethird)

    thirdbut = Button(root1, image=thirdphoto, borderwidth=5,command=lastwindow)
    thirdbut.place(x=510, y=10)

    thirdlab = Button(root1, text="RARE RABBIT\nGreen Printed T-Shirt\n1350/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    thirdlab.place(x=520, y=300)

    #FOR FOURTH SHIRT

    url = "https://tse1.mm.bing.net/th?id=OIP.URVQIMH57Dp41xuTLJYmkQHaKX&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    four = Image.open("kis.jpg")
    refour = four.resize((205, 275))

    fourphoto = ImageTk.PhotoImage(refour)

    fourbut = Button(root1, image=fourphoto, borderwidth=5,command=lastwindow)
    fourbut.place(x=760, y=10)

    fourlab = Button(root1, text="LEVI'S\nBarstow Western Shirt\n2379/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    fourlab.place(x=770, y=300)

    # FOR FIFTH SHIRT

    url = "https://tse3.mm.bing.net/th?id=OIP.eqhZXtFAukIGJNnjlHjCMQHaJY&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    fifth = Image.open("kis.jpg")
    refifth = fifth.resize((205, 275))

    fifthphoto = ImageTk.PhotoImage(refifth)

    fifthbut = Button(root1, image=fifthphoto, borderwidth=5,command=lastwindow)
    fifthbut.place(x=1010, y=10)

    fifthlab = Button(root1, text="AU NOIR\nItalian Fashion Sleeve Shirt\n956/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    fifthlab.place(x=1020, y=300)

    # FOR SIXTH SHIRT

    url = "https://tse3.mm.bing.net/th?id=OIP.tQ97TvdIvRYqoC4E9xdU9AHaLH&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    sixth = Image.open("kis.jpg")
    resixth =sixth.resize((205, 275))

    sixthphoto = ImageTk.PhotoImage(resixth)

    sixthbut = Button(root1, image=sixthphoto, borderwidth=5,command=lastwindow)
    sixthbut.place(x=1260, y=10)

    sixthlab = Button(root1, text="TOMMY JEANS\nBlocked Rugby Sweat Shirt\n1496/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    sixthlab.place(x=1270, y=300)

    # FOR SEVENTH SHIRT

    url = "https://tse2.mm.bing.net/th?id=OIP.VTNAvUPvZCf5ddUQyl_UGADrEs&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    seven = Image.open("kis.jpg")
    reseven = seven.resize((205, 275))

    sevenphoto = ImageTk.PhotoImage(reseven)

    sevenbut = Button(root1, image=sevenphoto, borderwidth=5,command=lastwindow)
    sevenbut.place(x=10, y=400)

    sevenlab = Button(root1, text="JACK & JONES\nPrint Round Neck T-Shirt\n520/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    sevenlab.place(x=20, y=690)

    # FOR EIGHT SHIRT

    url = "https://tse4.mm.bing.net/th?id=OIP.Rwupk2UwYrvzvJal1k35hAHaII&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    eight = Image.open("kis.jpg")
    reeight = eight.resize((205, 275))

    eightphoto = ImageTk.PhotoImage(reeight)

    eightbut = Button(root1, image=eightphoto, borderwidth=5,command=lastwindow)
    eightbut.place(x=260, y=400)

    eightlab = Button(root1, text="NCDIMS\nHandsome Blue Business Suit\n5490/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    eightlab.place(x=270, y=690)

    # FOR NINE SHIRT

    url = "https://tse1.mm.bing.net/th?id=OIP.bkFOmpSihknl8poTa1sNgAHaLw&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    nine = Image.open("kis.jpg")
    renine = nine.resize((205, 275))

    ninephoto = ImageTk.PhotoImage(renine)

    ninebut = Button(root1, image=ninephoto, borderwidth=5,command=lastwindow)
    ninebut.place(x=510, y=400)

    ninelab = Button(root1, text="ROADSTAR\nGreen Pure Cotton Shirt\n670/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    ninelab.place(x=520, y=690)

    # FOR TENTH SHIRT

    url = "https://tse4.mm.bing.net/th?id=OIP.2Q8Ws_pEVbc9wYBdNI7z5wAAAA&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    ten = Image.open("kis.jpg")
    reten = ten.resize((205, 275))

    tenphoto = ImageTk.PhotoImage(reten)

    tenbut = Button(root1, image=tenphoto, borderwidth=5,command=lastwindow)
    tenbut.place(x=760, y=400)

    tenlab = Button(root1, text="PAUL STREET\nSlim Fit Printed Casual Shirt\n890/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    tenlab.place(x=770, y=690)

    # FOR ELEVEN SHIRT

    url = "https://tse1.mm.bing.net/th?id=OIP.3j43HjeDzIxEkdoJ_AO3VAHaKH&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    eleven = Image.open("kis.jpg")
    reeleven = eleven.resize((205, 275))

    elevenphoto = ImageTk.PhotoImage(reeleven)

    elevenbut = Button(root1, image=elevenphoto, borderwidth=5,command=lastwindow)
    elevenbut.place(x=1010, y=400)

    elevenlab = Button(root1, text="UTTAM\nRegular Fit Causual Shirt\n1375/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    elevenlab.place(x=1020, y=690)

    # FOR TWELVE SHIRT

    url = "https://tse3.mm.bing.net/th?id=OIP.0U2uD9D2jTx2oWkIDfYm0AHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    twelve = Image.open("kis.jpg")
    retwelve = twelve.resize((205, 275))

    twelvephoto = ImageTk.PhotoImage(retwelve)

    twelvebut = Button(root1, image=twelvephoto, borderwidth=5,command=lastwindow)
    twelvebut.place(x=1260, y=400)

    twelvelab = Button(root1, text="RITSHA\nSlim Fit Striped Shirt\n496/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    twelvelab.place(x=1270, y=690)

    root1.mainloop()

#FOR LADIES COLLECTIONS

def for_ladies():

    root2=Toplevel(root)
    root2.title("ladies collections")
    root2.config(bg="black")
    w,h=root2.winfo_screenwidth(),root2.winfo_screenheight()
    root2.geometry('%dx%d+0+0' % (w,h))

    # FOR FIRST DRESS FOR GIRL


    url = "https://tse4.explicit.bing.net/th?id=OIP.nQ524jbrMPzPto8Ltcm56wHaLH&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    ladfirst= Image.open("kis.jpg")
    reladfirst = ladfirst.resize((205, 275))

    ladfirstphoto = ImageTk.PhotoImage(reladfirst)

    ladfirstbut = Button(root2, image=ladfirstphoto, borderwidth=5,command=lastwindow)
    ladfirstbut.place(x=10, y=10)

    ladfirstlab = Button(root2, text="SELECTION INC\nCream Color Salwar Suit\n1496/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    ladfirstlab.place(x=20, y=300)

    # FOR SECOND DRESS FOR GIRL

    url =   "https://tse2.mm.bing.net/th?id=OIP.AVT2ze1kfW-L3xahKlo4KgHaJH&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    ladsecond = Image.open("kis.jpg")
    reladsecond = ladsecond.resize((205, 275))

    ladsecondphoto = ImageTk.PhotoImage(reladsecond)

    ladsecondbut = Button(root2, image= ladsecondphoto, borderwidth=5,command=lastwindow)
    ladsecondbut.place(x=260, y=10)

    ladsecondlab = Button(root2, text="GEMGRACE\nRoyal Blue Embroidered Dress\n2239/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    ladsecondlab.place(x=270, y=300)

    # FOR THIRD DRESS FOR GIRL

    url = "https://tse3.mm.bing.net/th?id=OIP.Q8Tnc-aA_yovkIU1IlSdmAHaJ3&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    ladthird = Image.open("kis.jpg")
    reladthird = ladthird.resize((205, 275))

    ladthirdphoto = ImageTk.PhotoImage(reladthird)

    ladthirdbut = Button(root2, image=ladthirdphoto, borderwidth=5,command=lastwindow)
    ladthirdbut.place(x=510, y=10)

    ladthirdlab = Button(root2, text="ZIPEER\nClassy Lace Top Evening Gown\n2996/-",bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    ladthirdlab.place(x=520, y=300)

    # FOR FOURTH DRESS FOR GIRL

    url = "https://tse1.mm.bing.net/th?id=OIP.xxJ7IpaUo7cUuoPXE0ed4AHaJ4&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    ladfour = Image.open("kis.jpg")
    reladfour = ladfour.resize((205, 275))

    ladfourphoto = ImageTk.PhotoImage(reladfour)

    ladfourbut = Button(root2, image=ladfourphoto, borderwidth=5,command=lastwindow)
    ladfourbut.place(x=760, y=10)

    ladfourthlab = Button(root2, text="UTSAV FASHIONS\nEmbroidered Art Silk Lehanga\n5496/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    ladfourthlab.place(x=770, y=300)

    # FOR FIFTH DRESS FOR GIRL

    url = "https://tse2.mm.bing.net/th?id=OIP.9GsI6zT_zzuqvFHUTWKTtgHaLo&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    ladfifth = Image.open("kis.jpg")
    reladfifth = ladfifth.resize((205, 275))

    ladfifthphoto = ImageTk.PhotoImage(reladfifth)

    ladfifthbut = Button(root2, image=ladfifthphoto, borderwidth=5,command=lastwindow)
    ladfifthbut.place(x=1010, y=10)

    ladfifthlab = Button(root2, text="SHEIN\nOff Shoulder Sweater Tan\n1549/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    ladfifthlab.place(x=1020, y=300)

    # FOR SIXTH DRESS FOR GIRL

    url = "https://tse3.mm.bing.net/th?id=OIP.MLKgan1Wkp9xfK8fujq4aAHaKW&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    ladsixth = Image.open("kis.jpg")
    reladsixth = ladsixth.resize((205, 275))

    ladsixthphoto = ImageTk.PhotoImage(reladsixth)

    ladsixthbut = Button(root2, image=ladsixthphoto, borderwidth=5,command=lastwindow)
    ladsixthbut.place(x=1260, y=10)

    ladsixthlab = Button(root2, text="VVINE\nWomen Black Solid Shirt Dress\n1499/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    ladsixthlab.place(x=1270, y=300)

    # FOR SEVENTH DRESS FOR GIRL

    url = "https://tse2.mm.bing.net/th?id=OIP.bLEUGAXRH-j7FuELnTta2QHaFx&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    ladseven = Image.open("kis.jpg")
    reladseven = ladseven.resize((205, 275))

    ladsevenphoto = ImageTk.PhotoImage(reladseven)

    ladsevenbut = Button(root2, image=ladsevenphoto, borderwidth=5,command=lastwindow)
    ladsevenbut.place(x=10, y=400)

    ladseventhlab = Button(root2, text="FLATTER\nKanchipuram Art Silk Saree\n5999/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    ladseventhlab.place(x=20, y=690)

    # FOR EIGHT DRESS FOR GIRL

    url = "https://tse3.mm.bing.net/th?id=OIP.Uyo32mwBQjQNHxiTt1OJ4gHaJ_&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    ladeight = Image.open("kis.jpg")
    reladeight = ladeight.resize((205, 275))

    ladeightphoto = ImageTk.PhotoImage(reladeight)

    ladeightbut = Button(root2, image=ladeightphoto, borderwidth=5,command=lastwindow)
    ladeightbut.place(x=260, y=400)

    ladeightlab = Button(root2, text="CLUBE\nWinter Long Sleeve Dress\n949/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    ladeightlab.place(x=270, y=690)

    # FOR NINE DRESS FOR GIRL

    url = "https://tse4.mm.bing.net/th?id=OIP.nmwfA28bnMMPVn_jaefcRQHaKU&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    ladnine = Image.open("kis.jpg")
    reladnine = ladnine.resize((205, 275))

    ladninephoto = ImageTk.PhotoImage(reladnine)

    ladninebut = Button(root2, image=ladninephoto, borderwidth=5,command=lastwindow)
    ladninebut.place(x=510, y=400)

    ladninelab = Button(root2, text="FLORENCE\nWomen's Chiffon Dress Material\n549/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    ladninelab.place(x=520, y=690)

    # FOR TENTH DRESS FOR GIRL

    url = "https://tse1.mm.bing.net/th?id=OIP.rPQ3Tfzy6VwlwJSXdUm0bAHaLH&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    ladten = Image.open("kis.jpg")
    reladten = ladten.resize((205, 275))

    ladtenphoto = ImageTk.PhotoImage(reladten)

    ladtenbut = Button(root2, image=ladtenphoto, borderwidth=5,command=lastwindow)
    ladtenbut.place(x=760, y=400)

    ladtenlab = Button(root2, text="PINAFORE\nSquare Neck Pinafore Dress\n2996/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    ladtenlab.place(x=770, y=690)

    # FOR ELEVEN DRESS FOR GIRL

    url =  "https://tse1.mm.bing.net/th?id=OIP.SQX5hgExZesvKUEQGwDj5wHaJ4&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    ladeleven = Image.open("kis.jpg")
    reladeleven = ladeleven.resize((205, 275))

    ladelevenphoto = ImageTk.PhotoImage(reladeleven)

    ladelevenbut = Button(root2, image=ladelevenphoto, borderwidth=5,command=lastwindow)
    ladelevenbut.place(x=1010, y=400)

    ladelevenlab = Button(root2, text="RIZYA\nCasual Sleeveless Women Maroon Top\n1240/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    ladelevenlab.place(x=1020, y=690)

    # FOR TWELVE DRESS FOR GIRL

    url = "https://tse4.mm.bing.net/th?id=OIP.pjwHtoNqZFz9omwU5FjTlwHaJ4&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    ladtwelve = Image.open("kis.jpg")
    reladtwelve = ladtwelve.resize((205, 275))

    ladtwelvephoto = ImageTk.PhotoImage(reladtwelve)

    ladtwelvebut = Button(root2, image=ladtwelvephoto, borderwidth=5,command=lastwindow)
    ladtwelvebut.place(x=1260, y=400)

    ladtwelvelab = Button(root2, text="DRESSHEAD\nSleeveless Floral Print Dress\n890/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    ladtwelvelab.place(x=1270, y=690)

    root2.mainloop()

#FOR KIDS COLLECTIONS

def for_kids():
    root3=Toplevel(root)
    root3.title("kid's collections")
    root3.config(bg="black")
    w,h=root3.winfo_screenwidth(),root3.winfo_screenheight()
    root3.geometry('%dx%d+0+0' % (w,h))


    # FOR FIRST KID DRESS


    url = "https://tse4.mm.bing.net/th?id=OIP.9f8OS_4FIm6cZFO4Ng3-CAHaJQ&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    kidfirst= Image.open("kis.jpg")
    rekidfirst = kidfirst.resize((205, 275))

    kidfirstphoto = ImageTk.PhotoImage(rekidfirst)

    kidfirstbut = Button(root3, image=kidfirstphoto, borderwidth=5,command=lastwindow)
    kidfirstbut.place(x=10, y=10)

    kidfirstlab = Button(root3, text="LUXURY\nSummer Girl Dress \n390/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    kidfirstlab.place(x=20, y=300)


    # FOR SECOND KID DRESS

    url = "https://tse2.mm.bing.net/th?id=OIP.Zn_v-L1A5OW8WKXhYa_grwHaIw&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    kidsecond = Image.open("kis.jpg")
    rekidsecond = kidsecond.resize((205, 275))

    kidsecondphoto = ImageTk.PhotoImage(rekidsecond)

    kidsecondbut = Button(root3, image= kidsecondphoto, borderwidth=5,command=lastwindow)
    kidsecondbut.place(x=260, y=10)

    kidsecondlab = Button(root3, text="WHITE BUTTON\nBaby's Cotton Lehenga Choli\n1590/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    kidsecondlab.place(x=270, y=300)

    # FOR THIRD KID DRESS

    url = "https://tse4.mm.bing.net/th?id=OIP.PJ06Nx_sMw9RqhSnmWSWowHaJC&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    kidthird = Image.open("kis.jpg")
    rekidthird = kidthird.resize((205, 275))

    kidthirdphoto = ImageTk.PhotoImage(rekidthird)

    kidthirdbut = Button(root3, image=kidthirdphoto, borderwidth=5,command=lastwindow)
    kidthirdbut.place(x=510, y=10)

    kidfirstlab = Button(root3, text="APKPURE\nBoys Brown Leather Jacket\n990/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    kidfirstlab.place(x=520, y=300)

    # FOR FOURTH KID DRESS

    url = "https://tse2.mm.bing.net/th?id=OIP.Mn6sYDgu53iIbW7OlllTogHaLH&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    kidfour = Image.open("kis.jpg")
    rekidfour = kidfour.resize((205, 275))

    kidfourphoto = ImageTk.PhotoImage(rekidfour)

    kidfourbut = Button(root3, image=kidfourphoto, borderwidth=5,command=lastwindow)
    kidfourbut.place(x=760, y=10)

    kidfirstlab = Button(root3, text="SURATSALE\nClassy Peach & Grey Kidswear\n4800/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    kidfirstlab.place(x=770, y=300)

    # FOR FIFTH KID DRESS

    url =  "https://tse4.mm.bing.net/th?id=OIP.IPcA_aBP3vcWK8fq02ErqwHaJQ&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    kidfifth = Image.open("kis.jpg")
    rekidfifth = kidfifth.resize((205, 275))

    kidfifthphoto = ImageTk.PhotoImage(rekidfifth)

    kidfifthbut = Button(root3, image=kidfifthphoto, borderwidth=5,command=lastwindow)
    kidfifthbut.place(x=1010, y=10)

    kidfirstlab = Button(root3, text="BLOOMINGDALE'S\nPink Cashmere V-Neck Sweater\n799/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    kidfirstlab.place(x=1020, y=300)

    # FOR SIXTH  KID DRESS

    url = "https://tse4.mm.bing.net/th?id=OIP.qDvNlqvlXlEksxSybzM72wHaLH&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    kidsixth = Image.open("kis.jpg")
    rekidsixth =kidsixth.resize((205, 275))

    kidsixthphoto = ImageTk.PhotoImage(rekidsixth)

    kidsixthbut = Button(root3, image=kidsixthphoto, borderwidth=5,command=lastwindow)
    kidsixthbut.place(x=1260, y=10)

    kidfirstlab = Button(root3, text="NYKAA FASHION\nBabby Girl Kurtha Design\n1200/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    kidfirstlab.place(x=1270, y=300)

    # FOR SEVENTH KID DRESS

    url = "https://tse3.mm.bing.net/th?id=OIP.4dUfzmKC38brtLbgH0AsiQHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    kidseven = Image.open("kis.jpg")
    rekidseven = kidseven.resize((205, 275))

    kidsevenphoto = ImageTk.PhotoImage(rekidseven)

    kidsevenbut = Button(root3, image=kidsevenphoto, borderwidth=5,command=lastwindow)
    kidsevenbut.place(x=10, y=400)

    kidfirstlab = Button(root3, text="KBSPEER\nGirls Princess Dress\n2199/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    kidfirstlab.place(x=20, y=690)

    # FOR EIGHT KID DRESS

    url = "https://tse3.mm.bing.net/th?id=OIP.U21IhRb7tshREJw3q9J1TAHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    kideight = Image.open("kis.jpg")
    rekideight = kideight.resize((205, 275))

    kideightphoto = ImageTk.PhotoImage(rekideight)

    kideightbut = Button(root3, image=kideightphoto, borderwidth=5,command=lastwindow)
    kideightbut.place(x=260, y=400)

    kidfirstlab = Button(root3, text="WEIXU\nQuality Summer White Dress\n490/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    kidfirstlab.place(x=270, y=690)

    # FOR NINE KID DRESS

    url = "https://tse2.mm.bing.net/th?id=OIP.SR5EwRUKAquJmLn-N2vlEAAAAA&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    kidnine = Image.open("kis.jpg")
    rekidnine = kidnine.resize((205, 275))

    kidninephoto = ImageTk.PhotoImage(rekidnine)

    kidninebut = Button(root3, image=kidninephoto, borderwidth=5,command=lastwindow)
    kidninebut.place(x=510, y=400)

    kidfirstlab = Button(root3, text="FASHION EVEN\nBaby Girls Wedding Frock\n1999/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    kidfirstlab.place(x=520, y=690)

    # FOR TENTH KID DRESS

    url = "https://tse3.mm.bing.net/th?id=OIP.9V1D_7q4R5vGDxsG3wZl8AHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    kidten = Image.open("kis.jpg")
    rekidten = kidten.resize((205, 275))

    kidtenphoto = ImageTk.PhotoImage(rekidten)

    kidtenbut = Button(root3, image=kidtenphoto, borderwidth=5,command=lastwindow)
    kidtenbut.place(x=760, y=400)

    kidfirstlab = Button(root3, text="ALI FASHION\nPink Crystal Princess Dress\n820/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    kidfirstlab.place(x=770, y=690)

    # FOR ELEVEN KID DRESS

    url = "https://tse3.mm.bing.net/th?id=OIP.xSvgy8-HazDZwtay_NJ5awAAAA&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    kideleven = Image.open("kis.jpg")
    rekideleven = kideleven.resize((205, 275))

    kidelevenphoto = ImageTk.PhotoImage(rekideleven)

    kidelevenbut = Button(root3, image=kidelevenphoto, borderwidth=5,command=lastwindow)
    kidelevenbut.place(x=1010, y=400)

    kidfirstlab = Button(root3, text="BENIM\nBoys Party Wear Dress\n1550/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    kidfirstlab.place(x=1020, y=690)

    # FOR TWELVE KID DRESS

    url = "https://tse3.mm.bing.net/th?id=OIP.JP1geAR6QQ4N0ZZhlyUoFAHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    kidtwelve = Image.open("kis.jpg")
    rekidtwelve = kidtwelve.resize((205, 275))

    kidtwelvephoto = ImageTk.PhotoImage(rekidtwelve)

    kidtwelvebut = Button(root3, image=kidtwelvephoto, borderwidth=5,command=lastwindow)
    kidtwelvebut.place(x=1260, y=400)

    kidfirstlab = Button(root3, text="MIRRAW\nEmbroidery net silk Dress\n1790-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    kidfirstlab.place(x=1270, y=690)

    root3.mainloop()

#FOR ACCESRIOES COLLECTIONS

def for_acc():
    root4=Toplevel(root)
    root4.title("accesrioes collections")
    root4.config(bg="black")
    w,h=root4.winfo_screenwidth(),root4.winfo_screenheight()
    root4.geometry('%dx%d+0+0' % (w,h))


    # FOR FIRST ACCESROIES

    url = "https://tse1.mm.bing.net/th?id=OIP.32sWvnVmrzuLUCb0FVqAjgHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    accfirst= Image.open("kis.jpg")
    reaccfirst = accfirst.resize((205, 275))

    accfirstphoto = ImageTk.PhotoImage(reaccfirst)

    accfirstbut = Button(root4, image=accfirstphoto, borderwidth=5,command=lastwindow)
    accfirstbut.place(x=10, y=10)

    accfirstlab = Button(root4, text="BOULT\nUnisex Smart Watch SW12\n7780/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=20, y=300)

    # FOR SECOND ACCESROIES

    url = "https://tse2.mm.bing.net/th?id=OIP.NL2Kjxhj6wBJBVUySw5nEgHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    accsecond = Image.open("kis.jpg")
    reaccsecond = accsecond.resize((205, 275))

    accsecondphoto = ImageTk.PhotoImage(reaccsecond)

    accsecondbut = Button(root4, image= accsecondphoto, borderwidth=5,command=lastwindow)
    accsecondbut.place(x=260, y=10)

    accfirstlab = Button(root4, text="ZHOUYUMEIMEI\nLatest Silver Braclets For Girls\n2100/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=270, y=300)

    # FOR THIRD ACCESROIES

    url =  "https://tse2.mm.bing.net/th?id=OIP.10ncyl3u70bysmr28Te2zwHaE8&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    accthird = Image.open("kis.jpg")
    reaccthird = accthird.resize((205, 275))

    accthirdphoto = ImageTk.PhotoImage(reaccthird)

    accthirdbut = Button(root4, image=accthirdphoto, borderwidth=5,command=lastwindow)
    accthirdbut.place(x=510, y=10)

    accfirstlab = Button(root4, text="GEAR PATROL\nSummer Fragrances For Men\n800/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=521, y=300)

    # FOR FOURTH ACCESROIES

    url = "https://tse1.explicit.bing.net/th?id=OIP.CP17ZQQYmIGljeOhCsNtPQHaF7&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    accfour = Image.open("kis.jpg")
    reaccfour = accfour.resize((205, 275))

    accfourphoto = ImageTk.PhotoImage(reaccfour)

    accfourbut = Button(root4, image=accfourphoto, borderwidth=5,command=lastwindow)
    accfourbut.place(x=760, y=10)

    accfirstlab = Button(root4, text="NIKE\n Orange Adjustable Cap\n650/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=770, y=300)

    # FOR FIFTH ACCESROIES

    url = "https://tse2.mm.bing.net/th?id=OIP.EgRXnkunQDzq6TmQHUSoKgHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    accfifth = Image.open("kis.jpg")
    reaccfifth = accfifth.resize((205, 275))

    accfifthphoto = ImageTk.PhotoImage(reaccfifth)

    accfifthbut = Button(root4, image=accfifthphoto, borderwidth=5,command=lastwindow)
    accfifthbut.place(x=1010, y=10)

    accfirstlab = Button(root4, text="IKANT\nMen Canvas Casual Wallet \n490/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=1020, y=300)

    # FOR SIXTH ACCESROIES

    url = "https://tse3.mm.bing.net/th?id=OIP.pwnZAfLwAGwNJEO_p_HlNQHaFR&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    accsixth = Image.open("kis.jpg")
    reaccsixth =accsixth.resize((205, 275))

    accsixthphoto = ImageTk.PhotoImage(reaccsixth)

    accsixthbut = Button(root4, image=accsixthphoto, borderwidth=5,command=lastwindow)
    accsixthbut.place(x=1260, y=10)

    accfirstlab = Button(root4, text="AUGRAV\nWedding Gold Ring Set\n44200/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=1270, y=300)

    # FOR SEVENTH ACCESROIES

    url = "https://tse4.mm.bing.net/th?id=OIP.4d9BJS3-aO66j1emq2mtfgHaJ4&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    accseven = Image.open("kis.jpg")
    reaccseven = accseven.resize((205, 275))

    accsevenphoto = ImageTk.PhotoImage(reaccseven)

    accsevenbut = Button(root4, image=accsevenphoto, borderwidth=5,command=lastwindow)
    accsevenbut.place(x=10, y=400)

    accfirstlab = Button(root4, text="RAY-BAN\nSun Glasses Rb3483\n4990/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=20, y=690)

    # FOR EIGHT ACCESROIES

    url = "https://tse3.mm.bing.net/th?id=OIP.fZ9mSCYZbMjohyAu0u9GfQHaGx&pid=Api&P=0"


    urllib.request.urlretrieve(url, 'kis.jpg')

    acceight = Image.open("kis.jpg")
    reacceight = acceight.resize((205, 275))

    acceightphoto = ImageTk.PhotoImage(reacceight)

    acceightbut = Button(root4, image=acceightphoto, borderwidth=5,command=lastwindow)
    acceightbut.place(x=260, y=400)

    accfirstlab = Button(root4, text="LUULLA\nModern Jewellry Earrings\n599/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=270, y=690)

    # FOR NINE ACCESROIES

    url = "https://tse2.mm.bing.net/th?id=OIP.8_bV6PQbGdj22pecMUAYNQHaIA&pid=Api&P=0"

    urllib.request.urlretrieve(url, 'kis.jpg')

    accnine = Image.open("kis.jpg")
    reaccnine = accnine.resize((205, 275))

    accninephoto = ImageTk.PhotoImage(reaccnine)

    accninebut = Button(root4, image=accninephoto, borderwidth=5,command=lastwindow)
    accninebut.place(x=510, y=400)

    accfirstlab = Button(root4, text="CHERRY\nCoppola Calf Leather Bag\n3700/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=520, y=690)

    # FOR TENTH ACCESROIES

    url = "https://tse2.mm.bing.net/th?id=OIP.6Nf_l2E37COMCfxWwC46QgHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    accten = Image.open("kis.jpg")
    reaccten = accten.resize((205, 275))

    acctenphoto = ImageTk.PhotoImage(reaccten)

    acctenbut = Button(root4, image=acctenphoto, borderwidth=5,command=lastwindow)
    acctenbut.place(x=760, y=400)

    accfirstlab = Button(root4, text="CARTIER\nYellow Link Chain Necklace\n3990/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=770, y=690)

    # FOR ELEVEN ACCESROIES

    url = "https://tse4.mm.bing.net/th?id=OIP.8Kd6IntFs5OcFRlfBREHWgHaE8&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    acceleven = Image.open("kis.jpg")
    reacceleven = acceleven.resize((205, 275))

    accelevenphoto = ImageTk.PhotoImage(reacceleven)

    accelevenbut = Button(root4, image=accelevenphoto, borderwidth=5,command=lastwindow)
    accelevenbut.place(x=1010, y=400)

    accfirstlab = Button(root4, text="SQUAD15\nMens Black Leather Belt\n300/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=1020, y=690)

    # FOR TWELVE ACCESROIES

    url = "https://tse3.mm.bing.net/th?id=OIP.et63ZQ_nWSrZzRGoF1Py_wHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    twelve = Image.open("kis.jpg")
    reacctwelve = twelve.resize((205, 275))

    acctwelvephoto = ImageTk.PhotoImage(reacctwelve)

    acctwelvebut = Button(root4, image=acctwelvephoto, borderwidth=5,command=lastwindow)
    acctwelvebut.place(x=1260, y=400)

    accfirstlab = Button(root4, text="FALCONETTI\nTulip Pink Umbrella\n240/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=1270, y=690)

    root4.mainloop()

#  FOR FOOTWEAR  COLLECTION

def for_footwear():
    root5=Toplevel(root)
    root5.title("footware collections")
    root5.config(bg="black")
    w,h=root5.winfo_screenwidth(),root5.winfo_screenheight()
    root5.geometry('%dx%d+0+0' % (w,h))

    # FOR FIRST FOOTWEAR

    url = "https://tse2.mm.bing.net/th?id=OIP.hkt7UFfcEhf0PqV-A834awHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    footfirst= Image.open("kis.jpg")
    refootfirst = footfirst.resize((205, 275))

    footfirstphoto = ImageTk.PhotoImage(refootfirst)

    footfirstbut = Button(root5, image=footfirstphoto, borderwidth=5,command=lastwindow)
    footfirstbut.place(x=10, y=10)

    accfirstlab = Button(root5, text="POLOR FOX\nCasual Chukka Boots\n2100/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=20, y=300)

    # FOR SECOND FOOTWEAR

    url = "https://tse4.mm.bing.net/th?id=OIP.KgKsMz5bj9imqZbQdl9HTAAAAA&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    footsecond = Image.open("kis.jpg")
    refootsecond = footsecond.resize((205, 275))

    footsecondphoto = ImageTk.PhotoImage(refootsecond)

    footsecondbut = Button(root5, image= footsecondphoto, borderwidth=5,command=lastwindow)
    footsecondbut.place(x=260, y=10)

    accfirstlab = Button(root5, text="JACK DIAMOND\nCanvas Sneakers For Men\n800/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=270, y=300)

    # FOR THIRD FOOTWEAR

    url = "https://tse2.mm.bing.net/th?id=OIP.EDsrNGizp7NmFPvyXJcrLwHaF7&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    footthird = Image.open("kis.jpg")
    refootthird = footthird.resize((205, 275))

    footthirdphoto = ImageTk.PhotoImage(refootthird)

    footthirdbut = Button(root5, image=footthirdphoto, borderwidth=5,command=lastwindow)
    footthirdbut.place(x=510, y=10)

    accfirstlab = Button(root5, text="DRIPSA\nBaby Blue Canvas For Women\n1200/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=520, y=300)

    # FOR FOURTH FOOTWEAR

    url = "https://tse1.mm.bing.net/th?id=OIP.kRE6bGP1taW8UMm6XXsJqwHaJQ&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    footfour = Image.open("kis.jpg")
    refootfour = footfour.resize((205, 275))

    footfourphoto = ImageTk.PhotoImage(refootfour)

    footfourbut = Button(root5, image=footfourphoto, borderwidth=5,command=lastwindow)
    footfourbut.place(x=760, y=10)

    accfirstlab = Button(root5, text="SPERRY\nLace Up Sneaker For Men\n700/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=770, y=300)

    # FOR FIFTH FOOTWEAR

    url = "https://tse2.mm.bing.net/th?id=OIP.Cgvd8f9E03k8CsEOeuN8iAHaEo&pid=Api&P=0"

    urllib.request.urlretrieve(url, 'kis.jpg')

    footfifth = Image.open("kis.jpg")
    refootfifth = footfifth.resize((205, 275))

    footfifthphoto = ImageTk.PhotoImage(refootfifth)

    footfifthbut = Button(root5, image=footfifthphoto, borderwidth=5,command=lastwindow)
    footfifthbut.place(x=1010, y=10)

    accfirstlab = Button(root5, text="CROCS\nWhite Crocband Crocs\n1590/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=1020, y=300)

    # FOR SIXTH FOOTWEAR

    url = "https://tse4.mm.bing.net/th?id=OIP.lPWQwivDznXDKlrsYEMHPgHaFN&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    footsixth = Image.open("kis.jpg")
    refootsixth = footsixth.resize((205, 275))

    footsixthphoto = ImageTk.PhotoImage(refootsixth)

    footsixthbut = Button(root5, image=footsixthphoto, borderwidth=5,command=lastwindow)
    footsixthbut.place(x=1260, y=10)

    accfirstlab = Button(root5, text="PNGIMG\nTransparent Flip-Flop\n450/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=1270, y=300)

    # FOR SEVENTH FOOTWEAR

    url = "https://tse2.mm.bing.net/th?id=OIP.m3ODu9vqr8KUv6m7Mq1erQHaE8&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    footseven = Image.open("kis.jpg")
    refootseven = footseven.resize((205, 275))

    footsevenphoto = ImageTk.PhotoImage(refootseven)

    footsevenbut = Button(root5, image=footsevenphoto, borderwidth=5,command=lastwindow)
    footsevenbut.place(x=10, y=400)

    accfirstlab = Button(root5, text="HPYEBEAST\nGray Color Sneakers For Men\n2090/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=20, y=690)

    # FOR EIGHT FOOTWEAR

    url = "https://tse1.mm.bing.net/th?id=OIP.0e6QanURpmajoPnuOw-vKQHaEU&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    footeight = Image.open("kis.jpg")
    refooteight = footeight.resize((205, 275))

    footeightphoto = ImageTk.PhotoImage(refooteight)

    footeightbut = Button(root5, image=footeightphoto, borderwidth=5,command=lastwindow)
    footeightbut.place(x=260, y=400)

    accfirstlab = Button(root5, text="BARETRAPS\nNalani Slide Sandals\n770/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=270, y=690)

    # FOR NINE FOOTWEAR

    url = "https://tse3.mm.bing.net/th?id=OIP.XErcQh85uu3lZoxolH8nFAHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    footnine = Image.open("kis.jpg")
    refootnine = footnine.resize((205, 275))

    footninephoto = ImageTk.PhotoImage(refootnine)

    footninebut = Button(root5, image=footninephoto, borderwidth=5,command=lastwindow)
    footninebut.place(x=510, y=400)

    accfirstlab = Button(root5, text="POSEBAY\nBelgian Oxfords Shoes\n1400/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=520, y=690)

    # FOR TENTH FOOTWEAR

    url = "https://tse2.mm.bing.net/th?id=OIP.WlH-R07ARD1aZgGEzg88BAHaFk&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    footten = Image.open("kis.jpg")
    refootten = footten.resize((205, 275))

    foottenphoto = ImageTk.PhotoImage(refootten)

    foottenbut = Button(root5, image=foottenphoto, borderwidth=5,command=lastwindow)
    foottenbut.place(x=760, y=400)

    accfirstlab = Button(root5, text="PUMA\nCool Cat Black Sliders\n1600/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=770, y=690)

    # FOR ELEVEN FOOTWEAR

    url = "https://tse4.mm.bing.net/th?id=OIP.H5pG9ddpWKC6cNa9rv2a5wHaFj&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    footeleven = Image.open("kis.jpg")
    refooteleven = footeleven.resize((205, 275))

    footelevenphoto = ImageTk.PhotoImage(refooteleven)

    footelevenbut = Button(root5, image=footelevenphoto, borderwidth=5,command=lastwindow)
    footelevenbut.place(x=1010, y=400)

    accfirstlab = Button(root5, text="NIKE\nAir Force White Sneakers\n7700/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=1020, y=690)

    # FOR TWELVE FOOTWEAR

    url = "https://tse1.mm.bing.net/th?id=OIP.JaUS_xjIAx3kqxfDkwBpzQHaFM&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    foottwelve = Image.open("kis.jpg")
    refoottwelve = foottwelve.resize((205, 275))

    foottwelvephoto = ImageTk.PhotoImage(refoottwelve)

    foottwelvebut = Button(root5, image=foottwelvephoto, borderwidth=5,command=lastwindow)
    foottwelvebut.place(x=1260, y=400)

    accfirstlab = Button(root5, text="PUMA\nMulitycolor Causal Shoe \n12800/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    accfirstlab.place(x=1270, y=690)

    root5.mainloop()

#  FOR GADGETS COLLECTION

def for_gadgets():
    root6=Toplevel(root)
    root6.title("gadgets collections")
    root6.config(bg="black")
    w,h=root6.winfo_screenwidth(),root6.winfo_screenheight()
    root6.geometry('%dx%d+0+0' % (w,h))

    # FOR FIRST SHIRT

    url = "https://tse2.mm.bing.net/th?id=OIP.PBQMNDMgfS2FvTWIrIE1FAHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    gadfirst= Image.open("kis.jpg")
    regadfirst = gadfirst.resize((205, 275))

    gadfirstphoto = ImageTk.PhotoImage(regadfirst)

    gadfirstbut = Button(root6, image=gadfirstphoto, borderwidth=5,command=lastwindow)
    gadfirstbut.place(x=10, y=10)

    gadfirstlab = Button(root6, text="SAMSUNG\nSamsung Galaxy Tab E-T560\n45000/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    gadfirstlab.place(x=20, y=300)

    # FOR SECOND SHIRT

    url = "https://tse4.mm.bing.net/th?id=OIP.yAKpaqbLDIhoseCUIbuoaQHaEK&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    gadsecond = Image.open("kis.jpg")
    regadsecond = gadsecond.resize((205, 275))

    gadsecondphoto = ImageTk.PhotoImage(regadsecond)

    gadsecondbut = Button(root6, image= gadsecondphoto, borderwidth=5,command=lastwindow)
    gadsecondbut.place(x=260, y=10)

    gadfirstlab = Button(root6, text="NIKON\nD3000 DSLR Camera Body\n60000/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    gadfirstlab.place(x=270, y=300)

    # FOR THIRD SHIRT

    url = "https://tse2.mm.bing.net/th?id=OIP.FZALWTKsnabFFJhYzW157QHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    gadthird = Image.open("kis.jpg")
    regadthird = gadthird.resize((205, 275))

    gadthirdphoto = ImageTk.PhotoImage(regadthird)

    gadthirdbut = Button(root6, image=gadthirdphoto, borderwidth=5,command=lastwindow)
    gadthirdbut.place(x=510, y=10)

    gadfirstlab = Button(root6, text="BEATS\nStudio 2.0 Wired Over Headphone\n5500/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    gadfirstlab.place(x=520, y=300)

    # FOR FOURTH SHIRT

    url = "https://tse4.mm.bing.net/th?id=OIP.ynX0U4lSCuephRDY7Th01AHaLH&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    gadfour = Image.open("kis.jpg")
    regadfour = gadfour.resize((205, 275))

    gadfourphoto = ImageTk.PhotoImage(regadfour)

    gadfourbut = Button(root6, image=gadfourphoto, borderwidth=5,command=lastwindow)
    gadfourbut.place(x=760, y=10)

    gadfirstlab = Button(root6, text="SPENDESK\nVintage Microphone With Clipping\n8000/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    gadfirstlab.place(x=770, y=300)

    # FOR FIFTH SHIRT

    url = "https://tse4.mm.bing.net/th?id=OIP.bkcdnUi00TczorI-L_li7gHaHX&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    gadfifth = Image.open("kis.jpg")
    regadfifth = gadfifth.resize((205, 275))

    gadfifthphoto = ImageTk.PhotoImage(regadfifth)

    gadfifthbut = Button(root6, image=gadfifthphoto, borderwidth=5,command=lastwindow)
    gadfifthbut.place(x=1010, y=10)

    gadfirstlab = Button(root6, text="ORPAT\nOrpat Beep Alaram Clock\n420/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    gadfirstlab.place(x=1020, y=300)

    # FOR SIXTH SHIRT

    url = "https://tse3.mm.bing.net/th?id=OIP.NnKB0ettYpIK7-4bsuTlKwHaE9&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    gadsixth = Image.open("kis.jpg")
    regadsixth = gadsixth.resize((205, 275))

    gadsixthphoto = ImageTk.PhotoImage(regadsixth)

    gadsixthbut = Button(root6, image= gadsixthphoto, borderwidth=5,command=lastwindow)
    gadsixthbut.place(x=1260, y=10)

    gadfirstlab = Button(root6, text="CASIO\nCasion Scientific Calculator\n900/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    gadfirstlab.place(x=1270, y=300)

    # FOR SEVENTH SHIRT

    url =  "https://tse4.mm.bing.net/th?id=OIP.FyI_4pz5yGlzVPvvUehIWAHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    gadseven = Image.open("kis.jpg")
    regadseven = gadseven.resize((205, 275))

    gadsevenphoto = ImageTk.PhotoImage(regadseven)

    gadsevenbut = Button(root6, image= gadsevenphoto, borderwidth=5,command=lastwindow)
    gadsevenbut.place(x=10, y=400)

    gadfirstlab = Button(root6, text="SONY\nSony Bluetooth Speaker E2\n1200/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    gadfirstlab.place(x=20, y=690)

    # FOR EIGHT SHIRT

    url = "https://tse3.mm.bing.net/th?id=OIP.OWcN2hWXmdlOnL4iUYRRpAHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    gadeight = Image.open("kis.jpg")
    regadeight = gadeight.resize((205, 275))

    gadeightphoto = ImageTk.PhotoImage(regadeight)

    gadeightbut = Button(root6, image= gadeightphoto, borderwidth=5,command=lastwindow)
    gadeightbut.place(x=260, y=400)

    gadfirstlab = Button(root6, text="APPLE\nIphone 13 Pro Max Pencil\n10200/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    gadfirstlab.place(x=270, y=690)

    # FOR NINE SHIRT

    url = "https://tse4.mm.bing.net/th?id=OIP.wCU3cZoRo8IWgwJ4D24_uwHaE5&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    gadnine = Image.open("kis.jpg")
    regadnine = gadnine.resize((205, 275))

    gadninephoto = ImageTk.PhotoImage(regadnine)

    gadninebut = Button(root6, image= gadninephoto, borderwidth=5,command=lastwindow)
    gadninebut.place(x=510, y=400)

    gadfirstlab = Button(root6, text="MARS GAMING\nMM318 RGB Gaming Mouse\n1500/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    gadfirstlab.place(x=520, y=690)

    # FOR TENTH SHIRT

    url = "https://tse1.mm.bing.net/th?id=OIP.qyOdCy5ehRPUc04Tqw9K4AHaE8&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    gadten = Image.open("kis.jpg")
    regadten = gadten.resize((205, 275))

    gadtenphoto = ImageTk.PhotoImage(regadten)

    gadtenbut = Button(root6, image=gadtenphoto, borderwidth=5,command=lastwindow)
    gadtenbut.place(x=760, y=400)

    gadfirstlab = Button(root6, text="WESTERN DIGITAL\n40Gb 720RPM Hard Drive\n6000/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    gadfirstlab.place(x=770, y=690)

    # FOR ELEVEN eleven SHIRT

    url = "https://tse2.mm.bing.net/th?id=OIP.d-77G7hmOGkHDQ__PP8CwgHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    gadeleven = Image.open("kis.jpg")
    regadeleven = gadeleven.resize((205, 275))

    gadelevenphoto = ImageTk.PhotoImage(regadeleven)

    gadelevenbut = Button(root6, image=gadelevenphoto, borderwidth=5,command=lastwindow)
    gadelevenbut.place(x=1010, y=400)

    gadfirstlab = Button(root6, text="SAMSUNG\nGalaxy Active2 Watch\n12500/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    gadfirstlab.place(x=1020, y=690)

    # FOR TWELVE twelve SHIRT

    url = "https://tse2.mm.bing.net/th?id=OIP.1zsCnp9Y4_xvW66K3jZergHaHo&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    gadtwelve = Image.open("kis.jpg")
    regadtwelve = gadtwelve.resize((205, 275))

    gadtwelvephoto = ImageTk.PhotoImage(regadtwelve)

    gadtwelvebut = Button(root6, image=gadtwelvephoto, borderwidth=5,command=lastwindow)
    gadtwelvebut.place(x=1260, y=400)

    gadfirstlab = Button(root6, text="KANBKAM\nWebcam HD 1080p Web Camera\n2100/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    gadfirstlab.place(x=1270, y=690)

    root6.mainloop()

#  FOR BEAUTY PRODUCT COLLECTION

def for_bea():
    root7=Toplevel(root)
    root7.title("beauty products collections")
    root7.config(bg="black")
    w,h=root7.winfo_screenwidth(),root7.winfo_screenheight()
    root7.geometry('%dx%d+0+0' % (w,h))

    # FOR FIRST BEAUTY PRODUCT

    url = "https://tse1.mm.bing.net/th?id=OIP.oFBftV3HAxPlXzT24gcqZQHaF0&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    beafirst= Image.open("kis.jpg")
    rebeafirst = beafirst.resize((205, 275))

    beafirstphoto = ImageTk.PhotoImage(rebeafirst)

    beafirstbut = Button(root7, image=beafirstphoto, borderwidth=5,command=lastwindow)
    beafirstbut.place(x=10, y=10)

    beafirstlab = Button(root7, text="LOTUS\nSafe Sun Cream SPF 50\n600/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    beafirstlab.place(x=20, y=300)

    # FOR SECOND BEAUTY PRODUCT

    url = "https://tse2.mm.bing.net/th?id=OIP.aZd3lvDiBcquAVdepIREhgHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    beasecond = Image.open("kis.jpg")
    rebeasecond = beasecond.resize((205, 275))

    beasecondphoto = ImageTk.PhotoImage(rebeasecond)

    beasecondbut = Button(root7, image= beasecondphoto, borderwidth=5,command=lastwindow)
    beasecondbut.place(x=260, y=10)

    beafirstlab = Button(root7, text="PONDS\nPonds Purity Face Wash \n250/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    beafirstlab.place(x=270, y=300)


    # FOR THIRD BEAUTY PRODUCT

    url = "https://tse2.mm.bing.net/th?id=OIP.cmOUXfAH-9DJyjkthnwc1AAAAA&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    beathird = Image.open("kis.jpg")
    rebeathird = beathird.resize((205, 275))

    beathirdphoto = ImageTk.PhotoImage(rebeathird)

    beathirdbut = Button(root7, image=beathirdphoto, borderwidth=5,command=lastwindow)
    beathirdbut.place(x=510, y=10)

    beafirstlab = Button(root7, text="FOGG\nFresh Aromatic Perfume\n200/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    beafirstlab.place(x=520, y=300)

    # FOR FOURTH BEAUTY PRODUCT

    url = "https://tse2.mm.bing.net/th?id=OIP.wV3veydII2AtsoETk1CQRAHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    beafour = Image.open("kis.jpg")
    rebeafour = beafour.resize((205, 275))

    beafourphoto = ImageTk.PhotoImage(rebeafour)

    beafourbut = Button(root7, image=beafourphoto, borderwidth=5,command=lastwindow)
    beafourbut.place(x=760, y=10)

    beafirstlab = Button(root7, text="FIT ME\nMate Poreless Foundation\n800/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    beafirstlab.place(x=770, y=300)

    # FOR FIFTH BEAUTY PRODUCT

    url = "https://tse1.mm.bing.net/th?id=OIP.Am6o_wdreamnsnSHmLl6CQD6D5&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    beafifth = Image.open("kis.jpg")
    rebeafifth = beafifth.resize((205, 275))

    beafifthphoto = ImageTk.PhotoImage(rebeafifth)

    beafifthbut = Button(root7, image=beafifthphoto, borderwidth=5,command=lastwindow)
    beafifthbut.place(x=1010, y=10)

    beafirstlab = Button(root7, text="AVRIL\nBio Black Eyeliner\n400/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    beafirstlab.place(x=1020, y=300)

    # FOR SIXTH BEAUTY PRODUCT

    url = "https://tse3.mm.bing.net/th?id=OIP.HV5Hk0r44tXy_cdyiRHqAAHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    beasixth = Image.open("kis.jpg")
    rebeasixth =beasixth.resize((205, 275))

    beasixthphoto = ImageTk.PhotoImage(rebeasixth)

    beasixthbut = Button(root7, image=beasixthphoto, borderwidth=5,command=lastwindow)
    beasixthbut.place(x=1260, y=10)

    beafirstlab = Button(root7, text="GARNIER\n\Skin Active BB Cream\n500/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    beafirstlab.place(x=1270, y=300)

    # FOR SEVENTH BEAUTY PRODUCT

    url = "https://tse3.mm.bing.net/th?id=OIP.tUf8xeIrtviHnENaTEV5wwHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    beaseven = Image.open("kis.jpg")
    rebeaseven = beaseven.resize((205, 275))

    beasevenphoto = ImageTk.PhotoImage(rebeaseven)

    beasevenbut = Button(root7, image=beasevenphoto, borderwidth=5,command=lastwindow)
    beasevenbut.place(x=10, y=400)

    beafirstlab = Button(root7, text="MARCELLE\nFace Powder Poudre Faciale\n1200/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    beafirstlab.place(x=20, y=690)

    # FOR EIGHT BEAUTY PRODUCT

    url = "https://tse1.mm.bing.net/th?id=OIP.7z99O54P8mtzJzs2LdQTsgAAAA&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    beaeight = Image.open("kis.jpg")
    rebeaeight = beaeight.resize((205, 275))

    beaeightphoto = ImageTk.PhotoImage(rebeaeight)

    beaeightbut = Button(root7, image=beaeightphoto, borderwidth=5,command=lastwindow)
    beaeightbut.place(x=260, y=400)

    beafirstlab = Button(root7, text="RADHA BEAUTY\nGlow Vitamin C Moisturizer\n600/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    beafirstlab.place(x=270, y=690)

    # FOR NINE BEAUTY PRODUCT

    url = "https://tse3.mm.bing.net/th?id=OIP.FFQGgGIr0WifgT4esMusRAHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    beanine = Image.open("kis.jpg")
    rebeanine = beanine.resize((205, 275))

    beaninephoto = ImageTk.PhotoImage(rebeanine)

    beaninebut = Button(root7, image=beaninephoto, borderwidth=5,command=lastwindow)
    beaninebut.place(x=510, y=400)

    beafirstlab = Button(root7, text="STACHE\nBeard Oil For Men\n1100/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    beafirstlab.place(x=520, y=690)

    # FOR TENTH BEAUTY PRODUCT

    url = "https://tse4.mm.bing.net/th?id=OIP.qHj4T-zkAeKlWTnXs-5urgHaEK&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    beaten = Image.open("kis.jpg")
    rebeaten = beaten.resize((205, 275))

    beatenphoto = ImageTk.PhotoImage(rebeaten)

    beatenbut = Button(root7, image=beatenphoto, borderwidth=5,command=lastwindow)
    beatenbut.place(x=760, y=400)

    beafirstlab = Button(root7, text="LILLYAMOR\nMultipurpose Red Stick\n400/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    beafirstlab.place(x=770, y=690)

    # FOR ELEVEN BEAUTY PRODUCT

    url = "https://tse4.mm.bing.net/th?id=OIP.KfkXvv2taFxWJfNygcpwhAHaKf&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    beaeleven = Image.open("kis.jpg")
    rebeaeleven = beaeleven.resize((205, 275))

    beaelevenphoto = ImageTk.PhotoImage(rebeaeleven)

    beaelevenbut = Button(root7, image=beaelevenphoto, borderwidth=5,command=lastwindow)
    beaelevenbut.place(x=1010, y=400)

    beafirstlab = Button(root7, text="USDA ORGANIC\nLemon Grass Body Wash\n800/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    beafirstlab.place(x=1020, y=690)

    # FOR TWELVE BEAUTY PRODUCT

    url = "https://tse3.mm.bing.net/th?id=OIP.iXWYgDifC2mXrXX8wMqZowHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    beatwelve = Image.open("kis.jpg")
    rebeatwelve = beatwelve.resize((205, 275))

    beatwelvephoto = ImageTk.PhotoImage(rebeatwelve)

    beatwelvebut = Button(root7, image=beatwelvephoto, borderwidth=5,command=lastwindow)
    beatwelvebut.place(x=1260, y=400)

    beafirstlab = Button(root7, text="LANCOME\nLancome Blush Subtil\n990/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    beafirstlab.place(x=1270, y=690)

    root7.mainloop()

#  FOR HOME APPLIANCES COLLECTION

def for_home():
    root8=Toplevel(root)
    root8.title("home appliances collections")
    root8.config(bg="black")
    w,h=root8.winfo_screenwidth(),root8.winfo_screenheight()
    root8.geometry('%dx%d+0+0' % (w,h))

    # FOR FIRST HOME APPLIANCE

    url = "https://tse4.mm.bing.net/th?id=OIP.w-H76683BHxWVCGS5rQNDwAAAA&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    homefirst= Image.open("kis.jpg")
    rehomefirst = homefirst.resize((205, 275))

    homefirstphoto = ImageTk.PhotoImage(rehomefirst)

    homefirstbut = Button(root8, image=homefirstphoto, borderwidth=5,command=lastwindow)
    homefirstbut.place(x=10, y=10)

    homefirstlab = Button(root8, text="LG\nDirect Cool Refrigerator\n16000/-", bg="black", fg="white", font=("BOLD", 12),borderwidth=0,command=lastwindow)
    homefirstlab.place(x=20, y=300)


    # FOR SECOND HOME APPLIANCE

    url = "https://tse3.mm.bing.net/th?id=OIP.iKW-i07jm5uwn6VBlno9WgHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    homesecond = Image.open("kis.jpg")
    rehomesecond = homesecond.resize((205, 275))

    homesecondphoto = ImageTk.PhotoImage(rehomesecond)

    homesecondbut = Button(root8, image= homesecondphoto, borderwidth=5,command=lastwindow)
    homesecondbut.place(x=260, y=10)

    homefirstlab = Button(root8, text="BABAJ\n20 L Solo Microwave Oven\n6000/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    homefirstlab.place(x=270, y=300)


    # FOR THIRD HOME APPLIANCE

    url = "https://tse1.mm.bing.net/th?id=OIP.itZdCdjIfncC6tsrzw0WHAHaJ4&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    homethird = Image.open("kis.jpg")
    rehomethird = homethird.resize((205, 275))

    homethirdphoto = ImageTk.PhotoImage(rehomethird)

    homethirdbut = Button(root8, image=homethirdphoto, borderwidth=5,command=lastwindow)
    homethirdbut.place(x=510, y=10)

    homefirstlab = Button(root8, text="BAKEWALA\nArtisan Mini Stand Mixer\n5500/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    homefirstlab.place(x=520, y=300)

    # FOR FOURTH HOME APPLIANCE

    url =  "https://tse3.mm.bing.net/th?id=OIP.xkt0037Td7UA52bK2icoAwHaFT&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    homefour = Image.open("kis.jpg")
    rehomefour = homefour.resize((205, 275))


    homefourphoto = ImageTk.PhotoImage(rehomefour)

    homefourbut = Button(root8, image=homefourphoto, borderwidth=5,command=lastwindow)
    homefourbut.place(x=760, y=10)

    homefirstlab = Button(root8, text="PRESTAGE\nDeluxe Presure Cooker\n2200/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    homefirstlab.place(x=770, y=300)

    # FOR FIFTH HOME APPLIANCE

    url = "https://tse1.mm.bing.net/th?id=OIP.azugieZifXjYqtyuBfh8ogHaE8&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    homefifth = Image.open("kis.jpg")
    rehomefifth = homefifth.resize((205, 275))

    homefifthphoto = ImageTk.PhotoImage(rehomefifth)

    homefifthbut = Button(root8, image= homefifthphoto, borderwidth=5,command=lastwindow)
    homefifthbut.place(x=1010, y=10)

    homefirstlab = Button(root8, text="WHIRLPOOL\n7 KG Automatic Washing Machine\n24000/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    homefirstlab.place(x=1020, y=300)

    # FOR SIXTH HOME APPLIANCE

    url = "https://tse3.mm.bing.net/th?id=OIP.h7nE5DQvAf0FMpg6MCngxgHaFj&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    homesixth = Image.open("kis.jpg")
    rehomesixth = homesixth.resize((205, 275))

    homesixthphoto = ImageTk.PhotoImage(rehomesixth)

    homesixthbut = Button(root8, image=homesixthphoto, borderwidth=5,command=lastwindow)
    homesixthbut.place(x=1260, y=10)

    homefirstlab = Button(root8, text="GREEN CHEF\nThree Burners Gas Stove\n19000/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    homefirstlab.place(x=1270, y=300)

    # FOR SEVENTH HOME APPLIANCE

    url =  "https://tse2.mm.bing.net/th?id=OIP.oBOjv604pzDgbqC0ru1iTAHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    homeseven = Image.open("kis.jpg")
    rehomeseven = homeseven.resize((205, 275))

    homesevenphoto = ImageTk.PhotoImage(rehomeseven)

    homesevenbut = Button(root8, image=homesevenphoto, borderwidth=5,command=lastwindow)
    homesevenbut.place(x=10, y=400)

    homefirstlab = Button(root8, text="EUREKA\nQuick Clean Vacuum Cleaner\n3200/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    homefirstlab.place(x=20, y=690)

    # FOR EIGHT HOME APPLIANCE

    url = "https://tse3.mm.bing.net/th?id=OIP.SGN79a0BODmkwYrAcmUTuAHaE8&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    homeeight = Image.open("kis.jpg")
    rehomeeight = homeeight.resize((205, 275))

    homeeightphoto = ImageTk.PhotoImage(rehomeeight)

    homeeightbut = Button(root8, image=homeeightphoto, borderwidth=5,command=lastwindow)
    homeeightbut.place(x=260, y=400)

    homefirstlab = Button(root8, text="MORPHY\nSix Cups Coffe Maker\n1550/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    homefirstlab.place(x=270, y=690)

    # FOR NINE HOME APPLIANCE

    url = "https://tse3.mm.bing.net/th?id=OIP.-tXE6HzF4qmCMl-e9f2FeAHaG-&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    homenine = Image.open("kis.jpg")
    rehomenine = homenine.resize((205, 275))

    homeninephoto = ImageTk.PhotoImage(rehomenine)

    homeninebut = Button(root8, image=homeninephoto, borderwidth=5,command=lastwindow)
    homeninebut.place(x=510, y=400)

    homefirstlab = Button(root8, text="BOSCh\nFree Standing Dish Washer\n40940/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    homefirstlab.place(x=520, y=690)

    # FOR TENTH HOME APPLIANCE

    url = "https://tse4.mm.bing.net/th?id=OIP.FnpGdXNKDtmdwnUF3ikyBgHaF8&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    hometen = Image.open("kis.jpg")
    rehometen = hometen.resize((205, 275))

    hometenphoto = ImageTk.PhotoImage(rehometen)

    hometenbut = Button(root8, image=hometenphoto, borderwidth=5,command=lastwindow)
    hometenbut.place(x=760, y=400)

    homefirstlab = Button(root8, text="HAVELLS\nGlace Plus 1000W Iron Box\n670/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    homefirstlab.place(x=770, y=690)

    # FOR ELEVEN HOME APPLIANCE

    url = "https://tse3.mm.bing.net/th?id=OIP.LXGlhx_cW-wELXJUtDRxuwHaIr&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    homeeleven = Image.open("kis.jpg")
    rehomeeleven = homeeleven.resize((205, 275))

    homeelevenphoto = ImageTk.PhotoImage(rehomeeleven)

    homeelevenbut = Button(root8, image=homeelevenphoto, borderwidth=5,command=lastwindow)
    homeelevenbut.place(x=1010, y=400)

    homefirstlab = Button(root8, text="LUDDITE\n    Electric Mini Hot Pot\n800/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    homefirstlab.place(x=1020, y=690)

    # FOR TWELVE HOME APPLIANCE

    url = "https://tse2.mm.bing.net/th?id=OIP.rejiqO45fq4l3t6P-w003AHaE8&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    hometwelve = Image.open("kis.jpg")
    rehometwelve = hometwelve.resize((205, 275))

    hometwelvephoto = ImageTk.PhotoImage(rehometwelve)

    hometwelvebut = Button(root8, image=hometwelvephoto, borderwidth=5,command=lastwindow)
    hometwelvebut.place(x=1260, y=400)

    homefirstlab = Button(root8, text="HARSH\n    Atta & Bread Maker\n6200/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    homefirstlab.place(x=1270, y=690)

    root8.mainloop()

#  FOR JEWELLERY COLLECTION

def for_jewellery():
    root9=Toplevel(root)
    root9.title("jewellery collections")
    root9.config(bg="black")
    w,h=root9.winfo_screenwidth(),root9.winfo_screenheight()
    root9.geometry('%dx%d+0+0' % (w,h))

    # FOR FIRST JEWELLERY

    url = "https://tse4.mm.bing.net/th?id=OIP.AuHJmVcSZwaESSzHj9hfEgHaG0&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    jewfirst= Image.open("kis.jpg")
    rejewfirst = jewfirst.resize((205, 275))

    jewfirstphoto = ImageTk.PhotoImage(rejewfirst)

    jewfirstbut = Button(root9, image=jewfirstphoto, borderwidth=5,command=lastwindow)
    jewfirstbut.place(x=10, y=10)

    jewfirstlab = Button(root9, text="VINISA FASHONS\nBrass Gold Plated Bangles\n879/-", bg="black", fg="white",font=("BOLD", 12), borderwidth=0,command=lastwindow)
    jewfirstlab.place(x=20, y=300)

    # FOR SECOND JEWELLERY

    url = "https://tse4.mm.bing.net/th?id=OIP.n8xxJhI-OyZ3fSqssM55OwHaFj&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    jewsecond = Image.open("kis.jpg")
    rejewsecond = jewsecond.resize((205, 275))

    jewsecondphoto = ImageTk.PhotoImage(rejewsecond)

    jewsecondbut = Button(root9, image= jewsecondphoto, borderwidth=5,command=lastwindow)
    jewsecondbut.place(x=260, y=10)

    jewfirstlab = Button(root9, text="CHARLI\nFancy Micro Gold Plated Chain\n790/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    jewfirstlab.place(x=270, y=300)


    # FOR THIRD JEWELLERY

    url = "https://tse4.mm.bing.net/th?id=OIP.1ZRC7WsnMn2Dhh8ai8gjaAHaGD&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    jewthird = Image.open("kis.jpg")
    rejewthird = jewthird.resize((205, 275))

    jewthirdphoto = ImageTk.PhotoImage(rejewthird)

    jewthirdbut = Button(root9, image=jewthirdphoto, borderwidth=5,command=lastwindow)
    jewthirdbut.place(x=510, y=10)

    jewfirstlab = Button(root9, text="DIVASTRI\nGold Plated Alloy Earrings\n520/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    jewfirstlab.place(x=520, y=300)

    # FOR FOURTH JEWELLERY

    url = "https://tse1.mm.bing.net/th?id=OIP.90udEVveAvhLV6W1iTylfAHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    jewfour = Image.open("kis.jpg")
    rejewfour = jewfour.resize((205, 275))

    jewfourphoto = ImageTk.PhotoImage(rejewfour)

    jewfourbut = Button(root9, image=jewfourphoto, borderwidth=5,command=lastwindow)
    jewfourbut.place(x=760, y=10)

    jewfirstlab = Button(root9, text="SADNYA\nAlloy Gold Plated Bracelet\n400/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    jewfirstlab.place(x=770, y=300)

    # FOR FIFTH JEWELLERY

    url = "https://tse3.mm.bing.net/th?id=OIP.kDZcimtDNd8zyk7mAz_pPgHaJ4&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    jewfifth = Image.open("kis.jpg")
    rejewfifth = jewfifth.resize((205, 275))

    jewfifthphoto = ImageTk.PhotoImage(rejewfifth)

    jewfifthbut = Button(root9, image=jewfifthphoto, borderwidth=5,command=lastwindow)
    jewfifthbut.place(x=1010, y=10)

    jewfirstlab = Button(root9, text="BOGHRA\nHeart Shape Openable Locket\n390/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    jewfirstlab.place(x=1020, y=300)

    # FOR SIXTH JEWELLERY

    url = "https://tse1.mm.bing.net/th?id=OIP.0z4Z3D3CdCsxOBtxDMe10QHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    jewsixth = Image.open("kis.jpg")
    rejewsixth =jewsixth.resize((205, 275))

    jewsixthphoto = ImageTk.PhotoImage(rejewsixth)

    jewsixthbut = Button(root9, image=jewsixthphoto, borderwidth=5,command=lastwindow)
    jewsixthbut.place(x=1260, y=10)

    jewfirstlab = Button(root9, text="CHGOLD\nGold Plated Jewel Set\n2400/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    jewfirstlab.place(x=1270, y=300)

    # FOR SEVENTH JEWELLERY

    url = "https://tse3.mm.bing.net/th?id=OIP.uM4-SrPL0dc63cNiohKUnQHaIt&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    jewseven = Image.open("kis.jpg")
    rejewseven = jewseven.resize((205, 275))

    jewsevenphoto = ImageTk.PhotoImage(rejewseven)

    jewsevenbut = Button(root9, image=jewsevenphoto, borderwidth=5,command=lastwindow)
    jewsevenbut.place(x=10, y=400)

    jewfirstlab = Button(root9, text="BRADO\nBrass Gold Plated Necklace\n1600/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    jewfirstlab.place(x=20, y=690)

    # FOR EIGHT JEWELLERY

    url = "https://tse1.mm.bing.net/th?id=OIP.TsOEXtWo2XAB1MZ2Kdug4AHaFg&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    jeweight = Image.open("kis.jpg")
    rejeweight = jeweight.resize((205, 275))

    jeweightphoto = ImageTk.PhotoImage(rejeweight)

    jeweightbut = Button(root9, image=jeweightphoto, borderwidth=5,command=lastwindow)
    jeweightbut.place(x=260, y=400)

    jewfirstlab = Button(root9, text="SHREEJIHUF\nTraditional Toe Rings\n370/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    jewfirstlab.place(x=270, y=690)

    # FOR NINE JEWELLERY

    url = "https://tse3.mm.bing.net/th?id=OIP.M9wlLu0Q3ifFx8RsXlOjlwHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    jewnine = Image.open("kis.jpg")
    rejewnine = jewnine.resize((205, 275))

    jewninephoto = ImageTk.PhotoImage(rejewnine)

    jewninebut = Button(root9, image=jewninephoto, borderwidth=5,command=lastwindow)
    jewninebut.place(x=510, y=400)

    jewfirstlab = Button(root9, text="\n6.5 x 3.5 Length Brooch\n410/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    jewfirstlab.place(x=520, y=690)

    # FOR TENTH JEWELLERY

    url = "https://tse3.mm.bing.net/th?id=OIP.4-HC990NbpgS96-9N1BHQAHaHa&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    jewten = Image.open("kis.jpg")
    rejewten = jewten.resize((205, 275))

    jewtenphoto = ImageTk.PhotoImage(rejewten)

    jewtenbut = Button(root9, image=jewtenphoto, borderwidth=5,command=lastwindow)
    jewtenbut.place(x=760, y=400)

    jewfirstlab = Button(root9, text="MERSHI\nBeloved Zircon Necklace\n590/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    jewfirstlab.place(x=770, y=690)

    # FOR ELEVEN JEWELLERY

    url = "https://tse4.mm.bing.net/th?id=OIP.oLtWkTor1SS22825gt9f9QHaE7&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    jeweleven = Image.open("kis.jpg")
    rejeweleven = jeweleven.resize((205, 275))

    jewelevenphoto = ImageTk.PhotoImage(rejeweleven)

    jewelevenbut = Button(root9, image=jewelevenphoto, borderwidth=5,command=lastwindow)
    jewelevenbut.place(x=1010, y=400)

    jewfirstlab = Button(root9, text="GENICS\nWhite Stone Plated Ring\n280/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    jewfirstlab.place(x=1020, y=690)

    # FOR TWELVE JEWELLERY

    url = "https://tse1.mm.bing.net/th?id=OIP.5SEZCV_cWgk7aLqJs_BQmAHaE7&pid=Api&P=0"
    urllib.request.urlretrieve(url, 'kis.jpg')

    jewtwelve = Image.open("kis.jpg")
    rejewtwelve = jewtwelve.resize((205, 275))

    jewtwelvephoto = ImageTk.PhotoImage(rejewtwelve)

    jewtwelvebut = Button(root9, image=jewtwelvephoto, borderwidth=5,command=lastwindow)
    jewtwelvebut.place(x=1260, y=400)

    jewfirstlab = Button(root9, text="NARBHS\nBridal Anklets For Women\n1860/-", bg="black", fg="white", font=("BOLD", 12), borderwidth=0,command=lastwindow)
    jewfirstlab.place(x=1270, y=690)

    root9.mainloop()


# for shirts

url = "https://tse2.mm.bing.net/th?id=OIP.uIx6RIZluCZQOWuFTFO03gHaJ4&pid=Api&P=0"
urllib.request.urlretrieve(url,'shirt.jpg')

root = Tk()
root.geometry('560x700')
root.config(bg="honeydew2")
root.title('clothing app : click what you want')

# For scrolling

def marquee_fun(widget,widget_w,widget_h,total_w,total_h,direction,speed,position=0):
    if direction=='right':
        if position>=total_w-widget_w:
            position=0
        position=position+speed
        widget.place(x=position)
    elif direction=='left':
        if position<0:
            position=total_w-widget_w
        position=position-speed
        widget.place(x=position)
    widget.after(10,lambda:marquee_fun(widget,widget_w,widget_h,total_w,total_h,direction,speed,position))


x=Label(root,text="budget products || popular brands || trendy fits",font=("times to roman",15),bg="black",fg="white")
x.place(x=0,y=0,width=430,height=30)


x.after(100,lambda:marquee_fun(x,150,30,600,0,'left',1))
img = Image.open("shirt.jpg")
re=img.resize((140,140))

photo = ImageTk.PhotoImage(re)

but1 = Button(root,image=photo,borderwidth=5,command=for_shirts)
but1.place(x=20,y=40)

 
men=Button(root,text="mens wear",bg="black",fg="white",command=for_shirts)
men.place(x=60,y=200)

# for women

url = "https://tse3.mm.bing.net/th?id=OIP.jYDQ3RcIA9I7Su9VlwsjTgHaJT&pid=Api&P=0"
urllib.request.urlretrieve(url,'women1.jpg')

img2 = Image.open("women1.jpg")
re2=img2.resize((140,140))

pantphoto = ImageTk.PhotoImage(re2)

pantbut = Button(root,image=pantphoto,borderwidth=5,command=for_ladies)
pantbut.place(x=190,y=40)

women=Button(root,text="womens wear",bg="black",fg="white",command=for_ladies)
women.place(x=230,y=200)

# for kids

url = "https://tse1.mm.bing.net/th?id=OIP.88yzBiKFRLl51jv6jDy6EgHaHa&pid=Api&P=0"
urllib.request.urlretrieve(url,'kids.jpg')

img3 = Image.open("kids.jpg")
re3=img3.resize((140,140))

kidphoto = ImageTk.PhotoImage(re3)

kidbut = Button(root,image=kidphoto,borderwidth=5,command=for_kids)
kidbut.place(x=360,y=40)

kids=Button(root,text="kids wear",bg="black",fg="white",command=for_kids)
kids.place(x=400,y=200)

# for accesroies

url = "https://tse4.mm.bing.net/th?id=OIP.11uGctAOcay8ZfKpvr_WbQHaE3&pid=Api&P=0"
urllib.request.urlretrieve(url,'acc.jpg')

img4 = Image.open("acc.jpg")
re4=img4.resize((140,140))

accphoto = ImageTk.PhotoImage(re4)

accbut = Button(root,image=accphoto,borderwidth=5,command=for_acc)
accbut.place(x=20,y=250)

acc=Button(root,text="accesroies",bg="black",fg="white",command=for_acc)
acc.place(x=60,y=410)

# for footwear

url = "https://tse4.mm.bing.net/th?id=OIP.osXbQ2YMGxrMoBSbkFOsJwHaHa&pid=Api&P=0"
urllib.request.urlretrieve(url,'foot.jpg')

img5 = Image.open("foot.jpg")
re5=img5.resize((140,140))

footphoto = ImageTk.PhotoImage(re5)

footbut = Button(root,image=footphoto,borderwidth=5,command=for_footwear)
footbut.place(x=190,y=250)

foot=Button(root,text="foot wear",bg="black",fg="white",command=for_footwear)
foot.place(x=230,y=410)

# for gadgets

url = "https://tse1.mm.bing.net/th?id=OIP.rHyHufgDrUXEBonuXZ9nmQHaGP&pid=Api&P=0"
urllib.request.urlretrieve(url,'gadget.jpg')

img6 = Image.open("gadget.jpg")
re6=img6.resize((140,140))

gadphoto = ImageTk.PhotoImage(re6)

gadbut = Button(root,image=gadphoto,borderwidth=5,command=for_gadgets)
gadbut.place(x=360,y=250)

gad=Button(root,text="gadgets",bg="black",fg="white",command=for_gadgets)
gad.place(x=400,y=410)


# for beauty products

url = "https://tse4.mm.bing.net/th?id=OIP.dzqB33x0LyqukcKpPZ52owHaFj&pid=Api&P=0"
urllib.request.urlretrieve(url,'beauty.jpg')

img7 = Image.open("beauty.jpg")
re7=img7.resize((140,140))

beaphoto = ImageTk.PhotoImage(re7)

beabut = Button(root,image=beaphoto,borderwidth=5,command=for_bea)
beabut.place(x=20,y=470)

bea=Button(root,text="beauty",bg="black",fg="white",command=for_bea)
bea.place(x=60,y=630)

# for home

url = "https://tse4.mm.bing.net/th?id=OIP.k1ggA_pURI7w-wVAzTrlSQHaFY&pid=Api&P=0"
urllib.request.urlretrieve(url,'home.jpg')

img8 = Image.open("home.jpg")
re8=img8.resize((140,140))

homephoto = ImageTk.PhotoImage(re8)

homebut = Button(root,image=homephoto,borderwidth=5,command=for_home)
homebut.place(x=190,y=470)

hom=Button(root,text="home",bg="black",fg="white",command=for_home)
hom.place(x=230,y=630)


# for jewelllery

url = "https://tse4.mm.bing.net/th?id=OIP.nZYLDTD_cZFS5t6XnPCyYAHaHa&pid=Api&P=0"
urllib.request.urlretrieve(url,'jew.jpg')

img9 = Image.open("jew.jpg")
re9=img9.resize((140,140))

jewphoto = ImageTk.PhotoImage(re9)

jewbut = Button(root,image=jewphoto,borderwidth=5,command=for_jewellery)
jewbut.place(x=360,y=470)

jew=Button(root,text="jewellery",bg="black",fg="white",command=for_jewellery)
jew.place(x=400,y=630)

# for logo

url = "https://tse4.mm.bing.net/th?id=OIP.AimCF0eMXAVHFg1ofKCFiAHaHV&pid=Api&P=0"
urllib.request.urlretrieve(url,'logo.jpg')

logo = Image.open("logo.jpg")
relogo=logo.resize((30,30))

logophoto = ImageTk.PhotoImage(relogo)

logobut = Button(root,image=logophoto,borderwidth=0)
logobut.place(x=20,y=2)


root.mainloop()