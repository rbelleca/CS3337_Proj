from django.contrib.admin import AdminSite
from django.shortcuts import render, redirect
from django.http import HttpResponse
from  .models import MainMenu

from .forms import BookForm
from django.http import HttpResponseRedirect

from .models import Book

from .forms import RequestForm
from .models import Request

from .forms import ReviewForm
from .models import Review

from .models import UserCart

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

# Create your views here.
class MainMenuAdminSite(AdminSite):
    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        ordering = {
            "Display Books": 1,
            "Request Book": 2,
            "My Books": 3,
            "Shopping Cart": 4,
            "Post Book": 5,
        }
        app_dict = self._build_app_dict(request)
        # a.sort(key=lambda x: b.index(x[0]))
        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: ordering[x['name']])

        return app_list

def index(request):
    # return HttpResponse("<h1 align='center'>Hello World</h1>")
    # return render( request, 'base.html')
    # return render(request, 'bookMng/displaybooks.html')
    return render(request,
                  'bookMng/home.html',
                  {
                    'item_list': MainMenu.objects.all()
                  }
                  )

@login_required(login_url=reverse_lazy('login'))
def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                    'bookMng/postbook.html',
                    {
                        'form': form,
                        'item_list': MainMenu.objects.all(),
                        'submitted': submitted
                    })

@login_required(login_url=reverse_lazy('login'))
def displaybooks(request):
    books = Book.objects.all()
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
        'bookMng/displaybooks.html',
        {
            'item_list': MainMenu.objects.all(),
            'books': books
        })

@login_required(login_url=reverse_lazy('login'))
def mybooks(request):
    books = Book.objects.filter(username=request.user)
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
        'bookMng/mybooks.html',
        {
            'item_list': MainMenu.objects.all(),
            'books': books
        })

@login_required(login_url=reverse_lazy('login'))
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request,
        'bookMng/book_delete.html',
        {
            'item_list': MainMenu.objects.all(),
        })

@login_required(login_url=reverse_lazy('login'))
def requestbook(request):
    #submitted = False
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            requests = form.save(commit=False)
            try:
                requests.username = request.user
            except Exception:
                pass
            requests.save()
            return HttpResponseRedirect('/requestbook?submitted=True')
    else:
        form = RequestForm()
        #if 'submitted' in request.GET:
        #    submitted = True
    return render(request,
                    'bookMng/requestbook.html',
                    {
                        'form': form,
                        'item_list': MainMenu.objects.all(),
                        #'submitted': submitted
                    })

@login_required(login_url=reverse_lazy('login'))
def bookrequests(request):
    requests = Request.objects.all()
    return render(request,
        'bookMng/bookrequests.html',
        {
            'item_list': MainMenu.objects.all(),
            'requests': requests
        })

@login_required(login_url=reverse_lazy('login'))
def request_delete(request, request_id):
    requests = Request.objects.get(id=request_id)
    requests.delete()
    return render(request,
        'bookMng/request_delete.html',
        {
            'item_list': MainMenu.objects.all(),
        })

@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = Review.objects.filter(bookId = book_id)
    book.pic_path = book.picture.url[14:]

    #Form for writing a review.
    submitted = False
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            review = form.save(commit=False)
            try:
                review.username = request.user
                review.bookId = book
            except Exception:
                pass
            review.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = ReviewForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'reviews': reviews,
                      'book': book,
                      'submitted': submitted
                  })

@login_required(login_url=reverse_lazy('login'))
def book_addCart(request, book_id):
    books = Book.objects.all()
    book = Book.objects.get(id=book_id)
    item = UserCart()
    item.username = request.user
    item.bookId = book
    item.price = book.price
    item.name = book.name
    item.save()
    return redirect('displaybooks')

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    #User login is successful
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

@login_required(login_url=reverse_lazy('login'))
def shoppingcart(request):
    books = UserCart.objects.filter(username=request.user)
    # print(f'User: {request.user}')
    # print(books)
    totalPrice = list(books.aggregate(Sum('price')).values())[0]
    return render(request,
        'bookMng/shoppingcart.html',
        {
            'item_list': MainMenu.objects.all(),
            'books': books,
            'totalPrice': totalPrice
        })

@login_required(login_url=reverse_lazy('login'))
def cart_delete(request, cart_id):
    cartItem = UserCart.objects.get(id=cart_id)
    cartItem.delete()
    return redirect('shoppingcart')
