import sqlite3
def create():
    con = sqlite3.connect("Donation.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Donation(id INTEGER PRIMARY KEY,name TEXT,user TEXT, password TEXT,category TEXT,cdate TEXT)")
    con.commit()
    con.close()
def viewall():
    con = sqlite3.connect("Donation.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Donation")
    rows = cur.fetchall()
    con.close()
    return rows

def search(name="",user="",password="",category=""):
    con = sqlite3.connect("Donation.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Donation WHERE name=? OR user=? OR password=? OR category=?",(name,user,password,category))
    rows = cur.fetchall()
    con.close()
    return rows
def add(name,user,password,category,cdate):
    con = sqlite3.connect("Donation.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Donation VALUES(NULL,?,?,?,?,?)",(name,user,password,category,cdate))
    con.commit()
    con.close()
def update(id,name,user,password,category,cdate):
    con = sqlite3.connect("Donation.db")
    cur = con.cursor()
    cur.execute("UPDATE Donation SET name=?,user=?,password=?,category=?,cdate=? WHERE id=?",(name,user,password,category,cdate,id))
    con.commit()
    con.close()
def delete(id):
    con = sqlite3.connect("Donation.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Donation WHERE id=?",(id,))
    con.commit()
    con.close()
create()
