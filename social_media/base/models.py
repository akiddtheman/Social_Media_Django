from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.urls import reverse

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    username = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')

    def __str__(self):
        return str(self.user)  # Возвращаем строковое представление пользователя

    def get_absolute_url(self):
        return reverse('home')  # Возвращаем URL для перенаправления на домашнюю страницу

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user  # Возвращаем строковое представление пользователя

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255, default="")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=255, default="")
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title + " | " + str(self.author)  # Возвращаем строковое представление поста

    def get_absolute_url(self):
        return reverse('home')  # Возвращаем URL для перенаправления на домашнюю страницу

    def get_owner_pp(self):
        return self.author.profileimg.url  # Возвращаем URL изображения профиля автора поста

    def profileid(self):
        return self.author.user.id  # Возвращаем идентификатор пользователя автора поста

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)  # Возвращаем строковое представление комментария

    def get_absolute_url(self):
        return reverse('home')  # Возвращаем URL для перенаправления на домашнюю страницу

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username  # Возвращаем строковое представление пользователя



