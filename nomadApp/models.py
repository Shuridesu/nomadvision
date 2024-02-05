from django.db import models
from django.utils.text import slugify
from django.urls import reverse
class Author(models.Model):
    name = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=255,default='')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # スラッグが未設定の場合、名前からスラッグを生成
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name



from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

def send_email(post):
        User = get_user_model()
        subject = "A New Article Has Been Published: " + post.title
        html_message=render_to_string('email/new_post_notification.html', {'post': post})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        emails = [user.email for user in User.objects.filter(is_active=True) if user.email]
    
        for email in emails:
            msg = EmailMultiAlternatives(subject, plain_message, from_email, [email])
            msg.attach_alternative(html_message, "text/html")  # HTMLコンテンツを追加
            msg.send()
    
class Post(models.Model):
    title= models.CharField(max_length=200)
    meta_description = models.CharField(max_length = 500, default = '')
    title_image = models.ImageField(upload_to='post_images/',blank = True, null = True, default='')
    subtitle = models.CharField(max_length = 255,default='')
    heading1 = models.CharField(max_length = 100,blank = True, null = True, default='')
    image1 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    content1 = models.TextField(blank = True, null = True, default='' )
    
    heading2 = models.CharField(max_length = 100,blank = True, null = True, default='')
    image2 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    content2 = models.TextField(blank = True, null = True, default='')
    
    heading3 = models.CharField(max_length = 100,blank = True, null = True, default='')
    image3 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    content3 = models.TextField(blank = True, null = True, default='')
    
    heading4 = models.CharField(max_length = 100,blank = True, null = True,default='')
    image4 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    content4 = models.TextField(blank = True, null = True,default='')
    
    heading5 = models.CharField(max_length = 100,blank = True, null = True,default='')
    image5 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    content5 = models.TextField(blank = True, null = True,default='')
    
    heading6 = models.CharField(max_length = 100,blank = True, null = True,default='')
    image6 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    content6 = models.TextField(blank = True, null = True,default='')
    
    heading7 = models.CharField(max_length = 100,blank = True, null = True,default='')
    image7 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    content7 = models.TextField(blank = True, null = True,default='')
    
    heading8 = models.CharField(max_length = 100,blank = True, null = True,default='')
    image8 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    content8 = models.TextField(blank = True, null = True,default='')
    
    heading9 = models.CharField(max_length = 100,blank = True, null = True,default='')
    image9 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    content9 = models.TextField(blank = True, null = True,default='')
    
    heading10 = models.CharField(max_length = 100,blank = True, null = True,default='')
    image10 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    content10 = models.TextField(blank = True, null = True,default='')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default='')
    pub_date = models.DateField()
    category = models.ManyToManyField(Category,blank=True)
    slug = models.SlugField(unique = True, blank = True, max_length=500)
    is_recommended = models.BooleanField(default = False)
    is_trends_ai = models.BooleanField(default = False)
    is_trends_data = models.BooleanField(default = False)
    is_industry_insights = models.BooleanField(default = False)
    is_ai_software = models.BooleanField(default = False)
    sponsor_link = models.CharField(max_length = 500, blank = True, null = True, default='')
    
    
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            send_email(self)
        
    
    

    def __str__(self):
        return f"{self.title},{self.category}"
    
from django.conf import settings

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)