from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# 게시글 번호(정의하지 않으면 자동적으로 생성), 제목, 내용, 저자, 날짜, 조회수
class Board(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    writer = models.CharField(max_length=20)
    hit = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    full_name = models.CharField(max_length=20, null=True)
    subscribe = models.BooleanField(default=False)

    def _str_(self):
        return self.user.username


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='website/product_image/%Y/%m/%d')
    price = models.IntegerField(default=0)
    stock_left = models.IntegerField(default=0)


'''
default:
    blank = False,
    null = False,
'''