from django.db import models


# CATEGORY_CHOICES = (
#     ("1", "EDUCATION"),
#     ("2", "LABOR"),

# ) , choices=CATEGORY_CHOICES, default='EDUCATION'

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name

class Policies(models.Model): # 모델명의 첫 글자는 무조건 대문자
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 50)
    part = models.CharField(max_length = 255)
    description = models.TextField()
    categorycode =  models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name='category')
    

    def __str__(self):
        return self.name + ' ' + self.categorycode.name

