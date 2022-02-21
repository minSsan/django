from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # 자동으로 현재 시간으로 저장

    def __str__(self): # 객체 이름을 제목과 동일하게 설정
        return self.title