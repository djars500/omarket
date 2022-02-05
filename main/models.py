from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории' 
        
class Post(models.Model):
    title = models.CharField('Описание',max_length=255, blank=True, null=True)
    video = models.FileField('Видео',upload_to='video/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
