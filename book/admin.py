from django.contrib import admin

from book.models import book,student
#to register the  table name in admin
admin.site.register(book)
admin.site.register(student)