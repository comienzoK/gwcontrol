from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

from import_export.admin import ExportMixin, ImportExportModelAdmin
from import_export import resources
from django.contrib.auth import get_user_model

User = get_user_model()  # CustomUser 사용

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'is_active', 'is_staff', 'is_superuser')
        export_order = ('id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser')

    # 🔹 비밀번호 해싱 처리
    def before_import_row(self, row, **kwargs):
        if 'password' in row and row['password']:
            row['password'] = User.objects.make_random_password()  # 랜덤 비밀번호 생성

class CustomUserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('id',)

admin.site.register(User, CustomUserAdmin)