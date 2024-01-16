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


    


    
    
class Post(models.Model):
    title= models.CharField(max_length=200)
    meta_description = models.CharField(max_length = 500, default = '')
    title_image = models.ImageField(upload_to='post_images/',blank = True, null = True, default='')
    title_image_description = models.CharField(max_length = 500, default='')
    subtitle = models.CharField(max_length = 255,default='')
    heading1 = models.CharField(max_length = 100,blank = True, null = True, default='')
    image1 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    image1_description = models.CharField(max_length = 255, blank = True, null = True,default='')
    content1 = models.TextField(blank = True, null = True, default='' )
    
    heading2 = models.CharField(max_length = 100,blank = True, null = True, default='')
    image2 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    image2_description = models.CharField(max_length = 255, blank = True, null = True,default='')
    content2 = models.TextField(blank = True, null = True, default='')
    
    heading3 = models.CharField(max_length = 100,blank = True, null = True, default='')
    image3 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    image3_description = models.CharField(max_length = 255,blank = True, null = True,default='')
    content3 = models.TextField(blank = True, null = True, default='')
    
    heading4 = models.CharField(max_length = 100,blank = True, null = True,default='')
    image4 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    image4_description = models.CharField(max_length = 255,blank = True, null = True,default='')
    content4 = models.TextField(blank = True, null = True,default='')
    
    heading5 = models.CharField(max_length = 100,blank = True, null = True,default='')
    image5 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    image5_description = models.CharField(max_length = 255,blank = True, null = True,default='')
    content5 = models.TextField(blank = True, null = True,default='')
    
    heading6 = models.CharField(max_length = 100,blank = True, null = True,default='')
    image6 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    image6_description = models.CharField(max_length = 255,blank = True, null = True,default='')
    content6 = models.TextField(blank = True, null = True,default='')
    
    heading7 = models.CharField(max_length = 100,blank = True, null = True,default='')
    image7 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    image7_description = models.CharField(max_length = 255,blank = True, null = True,default='')
    content7 = models.TextField(blank = True, null = True,default='')
    
    heading8 = models.CharField(max_length = 100,blank = True, null = True,default='')
    image8 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    image8_description = models.CharField(max_length = 255,blank = True, null = True,default='')
    content8 = models.TextField(blank = True, null = True,default='')
    
    heading9 = models.CharField(max_length = 100,blank = True, null = True,default='')
    image9 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    image9_description = models.CharField(max_length = 255,blank = True, null = True,default='')
    content9 = models.TextField(blank = True, null = True,default='')
    
    heading10 = models.CharField(max_length = 100,blank = True, null = True,default='')
    image10 = models.ImageField(upload_to='post_images/',blank = True, null = True,default='' )
    image10_description = models.CharField(max_length = 255,blank = True, null = True,default='')
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
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title},{self.category}"
    

