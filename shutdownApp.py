from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()
st.title("Shutdown App")
st.geometry("700x700")
st.config(bg="blue")

r_button = Button(st, text="Restart", font=("Time New Roman", 15, "bold"),
                  relief=RAISED, cursor="plus",command=restart)
r_button.place(x=50, y=60, height=50, width=200)

rt_button = Button(st, text="Restart Time", font=("Time New Roman", 15, "bold"),
                   relief=RAISED, cursor="plus", command=restart_time)
rt_button.place(x=50, y=170, height=50, width=200)

lg_button = Button(st, text="Logout", font=("Time New Roman", 15, "bold"),
                   relief=RAISED, cursor="plus", command=logout)
lg_button.place(x=350, y=270, height=50, width=200)

st_button = Button(st, text="ShutDown", font=("Time New Roman", 15, "bold"),
                   relief=RAISED, cursor="plus", command=shutdown)
st_button.place(x=350, y=370, height=50, width=200)

st.mainloop()
