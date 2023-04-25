from django.contrib import admin
from .models import Book, User, Author, BookAuthor, Mentorship, InvestingCourses


admin.site.register(User)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookAuthor)
admin.site.register(Mentorship)
admin.site.register(InvestingCourses)
