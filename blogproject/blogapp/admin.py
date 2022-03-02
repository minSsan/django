from django.contrib import admin
from .models import Blog, Comment

admin.site.register(Blog) # admin 페이지에 Blog 테이블을 관리할 수 있도록 등록
admin.site.register(Comment)