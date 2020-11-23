from django.contrib import admin

# Register your models here.

from .models import MainMenu
from .models import Book
from .models import Request
from .models import Review
from .models import UserCart

admin.site.register(MainMenu)

admin.site.register(Book)

admin.site.register(Request)

admin.site.register(Review)

admin.site.register(UserCart)