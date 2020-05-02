from django.urls import path, include
from booksAuthorsAPP import views

urlpatterns = [
    path('', views.index),
    path('addBook', views.addBook),
    path('addAuthor', views.addAuthor),
    path('viewBook/<int:bookID>', views.viewBook),
    path('viewAuthor/<int:authorID>', views.viewAuthor),
    path('createNewBook', views.createNewBook),
    path('createNewAuthor', views.createNewAuthor),
    path('addAuthorToBook/<int:bookID>', views.addAuthorToBook),
    path('addBookToAuthor/<int:authorID>', views.addBookToAuthor)
]