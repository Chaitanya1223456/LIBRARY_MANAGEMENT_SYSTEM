# PROJECT ON LIBRARY MANAGEMENT
class Book:
    def __init__(self,title,author,ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN 
    def __str__(self):
        return str(self.title)
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return str(self.data)
    
class Linkedlist:
    Books_list = []
    d = {}
    def __init__(self):
        self.head = None
        
    def __str__(self):
        l = []
        if self.head is None:
            return 'linked list is empty'
        else:
            n = self.head 
            while n:
                l.append(str(n.data))
                n = n.next
            return ' --> '.join(l)
        
    def __len__(self):
        length = 0
        n = self.head
        while n:
            length+=1
            n = n.next
        return length
    
    def add(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode   
            self.Books_list.append(data)
        else:
            n = self.head 
            self.head = newnode 
            newnode.next = n 
            self.Books_list.append(data)
        return self.head
    def delete(self,val):
        n = self.head 
        if n.data == val:
            n = n.next 
        else:
            while n.next and n.next.data != val:
                n = n.next 
            if n.next.data == val:
                n.next = n.next.next
        return self.head
def input_info():
    bookname = input('Enter Book name: ')
    author = input('Enter Author name: ')
    ISBN = input('Enter ISBN No: ')
    username = input('Enter your name: ')
    ID = input('Enter your ID: ')
    return bookname,username
    
def user_status():
    purpose = input('Enter(BORROW or RETURN): ')
    return purpose
def book_status(ll,bookname):
    if bookname not in ll.Books_list:
        return False
    return True 
def Borrow(ll,bookname,username):
    if book_status(ll,bookname):
        if bookname in ll.d:
            print('This book was taken by '+ ll.d[bookname] )
            print('Books available in library are given below')
            print(ll)
        else:
            ll.d[bookname] = username 
            ll.delete(bookname)
            print('Book borrowed successfully.')
            print(ll)
    else:
        print("This book is unavailable in the library!")
        print('Books available in library are given below')
        print(ll)
def Return(ll,bookname):
    if bookname not in ll.d:
        print('This book is not from this library!')
        return
    newnode = Node(bookname)
    n = ll.head 
    ll.head = newnode
    newnode.next = n
    ll.d.pop(bookname)
    print('Book is handed successfully.')
    print(ll)
    
def start():
    s = input('Do you want to go through the library(YES or NO): ')
    if s == 'YES':
        return True
    else:
        return False
def LMS(ll):
    s = start()
    while s:
        bname,uname = input_info()
        purpose = user_status()
        print('Books available in library are given below')
        print(ll)
        if purpose == 'BORROW':
            Borrow(ll,bname,uname)
            s = start()
        else:
            Return(ll,bname)
            s = start()
        
        
        
MATH = Book('MATH','RAMANUJAN','978-93-96055-0-6')
PHYSICS = Book('PHYSICS','NEWTON','978-93-96055-0-7')
BIOLOGY = Book('BIOLOGY','ARISTOTLE','978-93-96055-0-8')
COMPUTER = Book('COMPUTER','CHARLES','978-93-96055-0-9')
        
ll = Linkedlist()
ll.add(MATH.title)
ll.add(PHYSICS.title)
ll.add(BIOLOGY.title)
ll.add(COMPUTER.title)  

print(ll)
LMS(ll)

            