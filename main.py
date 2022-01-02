import sqlite3
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Inventory System")
root.geometry('1030x380')
my_tree = ttk.Treeview(root)
storeName = "Book Store"


def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

def insert(bookid,bookname,price,authorname):
    conn=sqlite3.connect("data.db")
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS
    inventory(itemBookID TEXT,itemBookName TEXT,itemPrice TEXT,itemAuthorName TEXT)""")
    cursor.execute("INSERT INTO inventory VALUES('"+str(bookid)+"','"+str(bookname)+"','"+str(price)+"','"+str(authorname)+"')")
    conn.commit()


def delete(data):
    conn = sqlite3.connect ( "data.db" )
    cursor = conn.cursor ()
    cursor.execute ( """CREATE TABLE IF NOT EXISTS
      inventory(itemBookID TEXT,itemBookName TEXT,itemPrice TEXT,itemAuthorName TEXT)""" )
    cursor.execute("DELETE FROM inventory WHERE itemBookID='"+str(data)+"'")
    conn.commit()


def update(bookid,bookname,price,authorname,idBookName):
    conn = sqlite3.connect ( "data.db" )
    cursor = conn.cursor ()
    cursor.execute ( """CREATE TABLE IF NOT EXISTS
         inventory(itemBookID TEXT,itemBookName TEXT,itemPrice TEXT,itemAuthorName TEXT)""" )
    cursor.execute("UPDATE inventory SET itemBookID='"+str(id)+"',itemBookName='"+str(name)+"',itemPrice='"+str(price)+"',itemAuthorName='"+str(authorname)+"' WHERE itemBookID='"+str(idBookName)+"'")
    conn.commit()


def read():
    conn = sqlite3.connect ( "data.db" )
    cursor = conn.cursor ()
    cursor.execute ( """CREATE TABLE IF NOT EXISTS
        inventory(itemBookID TEXT,itemBookName TEXT,itemPrice TEXT,itemAuthorName TEXT)""" )
    cursor.execute("SELECT * FROM inventory")
    results=cursor.fetchall()
    conn.commit()
    return results

def add1():
    global count

    get_BookID = txt_BookID.get()
    get_BookName = txt_BookName.get()
    get_Price = txt_Price.get()
    get_AuthorName = txt_AuthorName.get()

    data_list.clear()
    data_list.append((get_BookID, get_BookName, get_Price, get_AuthorName))

    for item in data_list:
        tree_table.insert(parent='',index='end',idd=count, text=f'{count + 1}', values=(item))

        txt_BookID.delete(0, END)
        txt_BookName.delete(0, END)
        txt_Price.delete(0, END)
        txt_AuthorName.delete(0, END)
        count += 1
        print(data_list)
def insert_data():
    itemBookID=str(entryBookId.get())
    itemBookName = str(entryBookName.get())
    itemPrice = str(entryPrice.get())
    itemAuthorName = str(entryAuthorName.get())
    if itemBookID == ""or itemBookID ==" ":
        print("Error Inserting BookID")
    if itemBookName == ""or itemBookName ==" ":
        print("Error Inserting BookName")
    if itemPrice == ""or itemPrice ==" ":
        print("Error Inserting Price")
    if itemAuthorName == ""or itemAuthorName ==" ":
        print("Error Inserting AuthorName")
    else:
        insert(str(itemBookID),str(itemBookName),str(itemPrice),str(itemAuthorName))

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='',index='end',iid=0,text="",values=(result), tag="orow")

    my_tree.tag_configure ( 'orow' , background="#EEEEEE" , font=('Arial bold' , 15) )
    my_tree.grid ( row=1 , column=5 , columnspan=4 , rowspan=5 , padx=10 , pady=10 )


def delete_data():
    selected_item = my_tree.selection()[0]
    deleteData = str(my_tree.item(selected_item)['values'][0])
    delete(deleteData)

    for data in my_tree.get_children ():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='' ,index='end',iid=0,text="",values=(result),tag="orow")

    my_tree.tag_configure ('orow',background="#EEEEEE",font=('Arial bold', 15))
    my_tree.grid(row=1,column=5,columnspan=4,rowspan=5,padx=10,pady=10)


def update_data():
    selected_item = my_tree.selection ()[0]
    update_bookname = str(my_tree.item(selected_item)['values'][0])
    update(entryBookID.get(),entryBookName.get(),entryPrice.get(),entryAuthorName.get(),update_bookname)

    for data in my_tree.get_children ():
        my_tree.delete ( data )

    for result in reverse ( read () ):
        my_tree.insert ( parent='' , index='end' , iid=0 , text="" , values=(result) , tag="orow" )

    my_tree.tag_configure ( 'orow' , background="#EEEEEE" , font=('Arial bold' , 15) )
    my_tree.grid ( row=1 , column=5 , columnspan=4 , rowspan=5 , padx=10 , pady=10 )


titleLabel = Label(root,text=storeName, font=('Arial bold',30),bd=2)
titleLabel.grid(row=0,column=0,columnspan=8,padx=20,pady=20)

idLabel=Label(root,text="BookID",font=('Arial Bold',15))
nameLabel=Label(root,text="BookName",font=('Arial bold',15))
priceLabel=Label(root,text="Price",font=('Arial bold',15))
authornameLabel=Label(root,text="Author Name",font=('Arial bold',15))
idLabel.grid(row=1,column=0,padx=10,pady=10)
nameLabel.grid(row=2,column=0,padx=10,pady=10)
priceLabel.grid(row=3,column=0,padx=10,pady=10)
authornameLabel.grid(row=4,column=0,padx=10,pady=10)

entryBookId=Entry(root, width=25,bd=5,font=('Arial bold',15))
entryBookName=Entry(root, width=25,bd=5,font=('Arial bold',15))
entryPrice=Entry(root, width=25,bd=5,font=('Arial bold',15))
entryAuthorName=Entry(root, width=25,bd=5,font=('Arial bold',15))
entryBookId.grid(row=1,column=1,columnspan=3,padx=5,pady=5)
entryBookName.grid(row=2,column=1,columnspan=3,padx=5,pady=5)
entryPrice.grid(row=3,column=1,columnspan=3,padx=5,pady=5)
entryAuthorName.grid(row=4,column=1,columnspan=3,padx=5,pady=5)

buttonEnter=Button(
    root,text="Enter",padx=5,pady=5,width=5,bd=3,
    font=('Arial',15),bg="#0099ff",command=insert_data
)
buttonEnter.grid(row=5,column=1,columnspan=1)

buttonUpdate=Button(
    root,text="Update",padx=5,pady=5,width=5,bd=3,
    font=('Arial',15),bg="#ffff00",command=update_data
)
buttonUpdate.grid(row=5,column=2,columnspan=1)

buttonDelete=Button(
    root,text="Delete",padx=5,pady=5,width=5,bd=3,
    font=('Arial',15),bg="#e62e00",command=delete_data
)
buttonDelete.grid(row=5,column=3,columnspan=1)

style=ttk.Style()
style.configure("Treeview.Heading",font=('Arial bold',15))

my_tree['columns']=("BookID","BookName","Price","AuthorName")
my_tree.column("#0", width=0,stretch=NO)
my_tree.column("BookID",anchor=W,width=100)
my_tree.column("BookName",anchor=W,width=200)
my_tree.column("Price",anchor=W,width=150)
my_tree.column("AuthorName",anchor=W,width=150)
my_tree.heading("BookID",text="BookID",anchor=W)
my_tree.heading("BookName",text="BookName",anchor=W)
my_tree.heading("Price",text="Price",anchor=W)
my_tree.heading("AuthorName",text="AuthorName",anchor=W)

for data in my_tree.get_children ():
    my_tree.delete ( data )

for result in reverse ( read () ):
    my_tree.insert(parent='', index='end', text="",values=(result),tag="orow")

my_tree.tag_configure ( 'orow' , background="#EEEEEE" , font=('Arial bold' , 15) )
my_tree.grid ( row=1 , column=5 , columnspan=4 , rowspan=5 , padx=10 , pady=10 )



root.mainloop()

