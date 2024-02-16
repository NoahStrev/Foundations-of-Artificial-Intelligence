from kanren import *

genre = Relation()
title = Relation()
author = Relation()

def titles_in_genre(which_genre) :
   x = var()
   h = run(0,x,genre(which_genre,x))
   titles_to_return = []
   for t in h:
       xx = var()
       hh = run(0,xx,title(xx,t))
       for m in hh:
           titles_to_return.append(m)
   return titles_to_return

def books_written_by(which_author) :
    a=var()
    y=var()
    b =run(0, a, author('James Patterson', y), title(a, y))
    return list(b)

def who_wrote_book(whatBook) :
    a = var()
    y = var()
    whowrote = run(0, a, author(a, y), title(whatBook, y))
    return list(whowrote)
    


# ###############    DEFINE THE FACTS   ###############################

facts(genre,('mystery', 'ISBN1')) 
facts(genre,('mystery', 'ISBN2'))
facts(genre,('mystery', 'ISBNx') )
facts(title,('Rose are Red','ISBN1') )
facts(title,('Gone Girl', 'ISBN2') )
facts(title,('22 Seconds', 'ISBNx') )
facts(author,('James Patterson', 'ISBN1') )
facts(author,('James Patterson', 'ISBNx') )
facts(author,('Gillian Flynn', 'ISBN2') )


# ####################   ASK ABOUT THE FACTS  ###########################
print()
print('Book Collection Information:')
x = var()
print()
print('MYSTERY GENRE:')
mw = titles_in_genre('mystery')
for mw_item in mw:
    print(mw_item)
print()


print('***********************')
print('Books written by James Patterson')
authorbooks = books_written_by('James Patterson')
for book in authorbooks:
    print(book)
print()
print('***********************')

print()
whatBook = 'Gone Girl'
print('Who wrote ', whatBook,'?')
bookauthor = who_wrote_book(whatBook) 
for writer in bookauthor:
    print(writer)
print()

