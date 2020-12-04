from django.urls import path
from . import views

#Handles all the urls. Use after view.py.
urlpatterns = [
    path('', views.index, name='index'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('requestbook', views.requestbook, name='requestbook'),
    path('request_delete/<int:request_id>', views.request_delete, name='request_delete'),
    path('book_addCart/<int:book_id>', views.book_addCart, name='book_addCart'),
    path('shoppingcart', views.shoppingcart, name='shoppingcart'),
    path('cart_delete/<int:cart_id>', views.cart_delete, name='cart_delete'),
]

