from django.forms import ModelForm
from invest.models import User, Book, Author, BookAuthor, Mentorship, InvestingCourses, Notes

class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", 'first_name', 'last_name' ,'email', 'password')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
        

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "profile_picture")


class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = ("title", "description", "cover_picture", "pdf", )


class AuthorCreateForm(ModelForm):
    class Meta:
        model = Author
        fields = ("first_name", "last_name", "about", "picture", )


class BookAuthorCreateForm(ModelForm):
    class Meta:
        model = BookAuthor
        fields = ("book", "author", )


class MentorshipCreateForm(ModelForm):
    class Meta:
        model = Mentorship
        fields = ("title", "video_url", )


class InvestingCoursesCreateForm(ModelForm):
    class Meta:
        model = InvestingCourses
        fields = ("title", "video_url", )

    
class NotesCreateForm(ModelForm):
    class Meta:
        model = Notes
        fields = ("title", "text", )