from django.contrib import admin
from django.db import models
from grocery.models import Cleaning



# Register your models here.

class search(admin.ModelAdmin):
    fields=["name","op","adp","subdepartment"]   #detail view fields
    search_fields=["name"]                       
    list_filter=["subdepartment"]
    list_display=["name","adp","op","subdepartment"]
    list_editable=["adp","op"]
    list_per_page=(5)
    #change_list_template=["index.html"] #change the template
    #admin.site.index_template=["index.html"]


admin.site.register(Cleaning,search)

