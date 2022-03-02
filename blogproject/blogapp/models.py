from distutils.command.upload import upload
from statistics import mode
from tkinter import CASCADE
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # 자동으로 현재 시간으로 저장 허용
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')

    def __str__(self): # 객체 이름을 제목과 동일하게 설정
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE) # 이 댓글이 달린 게시글을 가리킴
    # on_delete=CASCADE :: 참조 대상이 삭제되면, 자기 자신도 삭제

    def __str__(self):
        return self.comment