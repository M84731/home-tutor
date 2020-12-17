# Register your models here.
from django.contrib import admin
from .models import stregister
from.models import ttregister
from.models import login
from.models import formtutor
from.models import booknow

admin.site.register(stregister)
admin.site.register(ttregister)
admin.site.register(login)
admin.site.register(formtutor)
admin.site.register(booknow)




