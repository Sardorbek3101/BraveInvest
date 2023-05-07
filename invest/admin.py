from django.contrib import admin
from .models import Book, User, Author, BookAuthor, Mentorship, InvestingCourses, Notes, Questions


admin.site.register(User)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookAuthor)
admin.site.register(Mentorship)
admin.site.register(InvestingCourses)
admin.site.register(Notes)
admin.site.register(Questions)
