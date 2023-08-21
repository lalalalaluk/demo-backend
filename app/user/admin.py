from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin

# Register your models here.
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms

from app.user.models import User

class UserAdmin(_UserAdmin):
    list_display = ['username', 'email', 'date_joined', 'is_superuser', 'is_staff',
                    'is_active']
    search_fields = ['email', 'username', 'date_joined']

    fieldsets = (
        ('基本資料', {'fields': ('email', 'username', 'unit', 'contact', 'password')}),
        ('權限管理', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        ('登入狀態', {'fields': ('date_joined', 'last_login')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'unit', 'contact', 'password1', 'password2'),
        }),
    )


admin.site.register(User, UserAdmin)

admin.site.site_header = '圖書館系統管理後台'
admin.site.index_title = '管理後台'