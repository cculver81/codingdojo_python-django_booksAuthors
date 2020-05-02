
from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    return redirect('/addBook')

#Books Pages Functions
def addBook(request):
    context = {
        'allBooks' : Book.objects.all()
    }
    return render(request, 'addBook.html', context)

def createNewBook(request):
    P = request.POST
    B = Book.objects
    B.create(title = P['title'],description = P['description'])
    return redirect('/addBook')
    

def viewBook(request, bookID):
    print(bookID)
    B = Book.objects.get(id = bookID)
    allAuthors = Author.objects.all()

    context = {
        'bookInfo' : B,
        'bookAuthors' : B.authors.all(),
        'allAuthors' : allAuthors
    }
    print(type(context['bookAuthors']))
    return render(request, 'viewBook.html', context)

def addAuthorToBook(request, bookID):
    # print('Ran add Author to Book')
    # print(bookID)
    # print(request.POST)

    B = Book.objects.get(id = bookID)
    A = Author.objects.get(id = request.POST['addAuthorToBook'])
    B.authors.add(A)
    B.save()

    return redirect('/viewBook/' + str(bookID))

#Authors Pages Functions
def addAuthor(request):
    context = {
        'allAuthors' : Author.objects.all()
    }
    return render(request, 'addAuthor.html', context)

def createNewAuthor(request):
    P = request.POST
    A = Author.objects
    A.create(fname = P['fname'], lname = P['lname'], notes = P['notes'])
    return redirect('/addAuthor')

def viewAuthor(request, authorID):
    A = Author.objects.get(id = authorID)
    allBooks = Book.objects.all()

    context = {
        'authorInfo' : A,
        'authoredBooks' : A.books.all(),
        'allBooks': allBooks
    }
    return render(request, 'viewAuthor.html', context)

def addBookToAuthor(request, authorID):
    # print(request.POST['addBookToAuthor'])
    # print(authorID)
    A = Author.objects.get(id = authorID)
    B = Book.objects.get(id = request.POST['addBookToAuthor'])
    A.books.add(B)
    return redirect('/viewAuthor/' + str(authorID))