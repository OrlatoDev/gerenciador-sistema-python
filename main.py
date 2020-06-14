import os
import platform
from time import sleep
from tkinter import *

try:
    user = os.getlogin()
except:
    user = "Error"

try:
    pcname = platform.node()
except:
    pcname = "Error"

try:
    sistemaoperacional = platform.system()
except:
    sistemaoperacional = "Error"

try:
    infoos = platform.platform()
except:
    infoos = "Error"

try:
    patch = os.getenv("PATH")
except:
    patch = "Error"

try:
    architeture = platform.machine()
except:
    architeture = "Error"

try:
    ncpu = os.cpu_count()
except:
    ncpu = "Error"

try:
    infoprocessador = platform.processor()
except:
    infoprocessador = "Error"

window = Tk()

def msconfig():
    os.system("C:\Windows\System32\msconfig.exe")

def panelcontrol():
    os.system("start control")

def cmd():
    os.system("start cmd")

def regedit():
    os.system("start regedit")

def dxdiag():
    os.system("start dxdiag")

def msinfo():
    os.system("C:\Windows\System32\msinfo32.exe")

try:
    window.iconbitmap("C:\\Users\\Samuel\\Documents\\PROJETOS COM TKINTER\\Gerenciador de Sistema com Tkinter\\system_iSX_icon.ico")
except:
    pass
window.geometry("450x300")
window.title("SYSTEM MANAGEMENT")
window["bg"] = "white"
window.resizable(width=False, height=False)

L_user = Label(window, text="Hello, "+str(user), bg="white", fg="RoyalBlue2", font="Antipasto 20")
L_user.pack(side=TOP, fill=BOTH)

image1 = PhotoImage("")

FrameEsquerdo = Frame(window, bg="RoyalBlue2", width=30)
FrameEsquerdo.pack(side=LEFT, fill=Y)

L_PCname = Label(window, text="PC Name: "+str(pcname), bg="white", fg="black", font="Antipasto 10")
L_PCname.place(x=30, y=40)

L_os = Label(window, text="Operational System: "+str(sistemaoperacional), bg="white", fg="black", font="Antipasto 10")
L_os.place(x=30, y=70)

L_ios = Label(window, text="Info OS: "+str(infoos), bg="white", fg="black", font="Antipasto 10")
L_ios.place(x=30, y=90)

L_arch = Label(window, text="Architeture: "+str(architeture), bg="white", fg="black", font="Antipasto 10")
L_arch.place(x=30, y=120)

L_ncpu = Label(window, text="Number of Processors: "+str(ncpu), bg="white", fg="black", font="Antipasto 10")
L_ncpu.place(x=30, y=150)

L_icpu = Label(window, text="Processors Info: "+str(infoprocessador), bg="white", fg="black", font="Antipasto 10")
L_icpu.place(x=30, y=170)

configinit = Button(window, text="Configure Startup and Others", bg="RoyalBlue2", fg="black", font="Antipasto 10", width=30, command=msconfig)
configinit.place(x=125, y=210)

controlpanel = Button(window, text="Open Control Panel", bg="RoyalBlue2", fg="black", font="Antipasto 10", width=30, command=panelcontrol)
controlpanel.place(x=125, y=240)

cmd = Button(window, text="Open CMD", bg="RoyalBlue2", fg="black", font="Antipasto 10", width=30, command=cmd)
cmd.place(x=125, y=270)

regedit = Button(window, text="Regedit", bg="RoyalBlue2", fg="black", font="Antipasto 10", command=regedit)
regedit.place(x=31, y=270)

dxdiag = Button(window, text="DxDiag", bg="RoyalBlue2", fg="black", font="Antipasto 10", width=7,command=dxdiag)
dxdiag.place(x=31, y=240)

msinfo = Button(window, text="MsInfo", bg="RoyalBlue2", fg="black", font="Antipasto 10", width=7,command=msinfo)
msinfo.place(x=31, y=210)

window.mainloop()