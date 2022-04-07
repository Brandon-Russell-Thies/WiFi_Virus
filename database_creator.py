from tkinter import *
import sqlite3 as sq
######################


def create_database():#This code creates a database and adds
    #the name of the router that is white listed to the database
    conn = sq.connect("system_info.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE ROUTER(Name VARCHAR(50));""")
    c.execute(f"INSERT INTO ROUTER VALUES ('{router.get()}')")
    conn.commit()
    root.destroy()#makes the interface disappear
    

root = Tk()#the interface

root.title("Router Name")
router = Entry(root)
button = Button(root, text="submit", command=create_database)

router.pack()
button.pack()

root.mainloop()
