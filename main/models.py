from django.db import models
from django.contrib.auth.models import User


image = models.ImageField(upload_to='appname', null=True)

# Models.py에 Post클래스로 테이블을 만들었습니다.


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="post/", blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
