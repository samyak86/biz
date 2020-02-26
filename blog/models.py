from django.db import models

# Create your models here.
class UserType(models.Model):
    type_name=models.CharField(max_length=250,null=False)
    type_desc=models.TextField()
    active = models.IntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

class Company(models.Model):
    company_name=models.CharField(max_length=100)
    company_owner=models.CharField(max_length=100)
    company_domain=models.CharField(max_length=100)
    company_website = models.URLField()
    company_size= models.IntegerField()
    company_headquarters= models.CharField(max_length=250)
    company_type=models.CharField(max_length=100)
    company_establishmentyear=models.IntegerField()
    company_specialties=models.CharField(max_length=250)
    company_locations=models.CharField(max_length=250)
    active = models.IntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

class BloggerLogin(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.IntegerField()
    user_type=models.ForeignKey(UserType, on_delete=models.CASCADE)
    com_id=models.ForeignKey(Company, on_delete=models.CASCADE,default=-1)
    active=models.IntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

class Category(models.Model):
    cat_name = models.CharField(max_length=250, null=False)
    cat_desc = models.TextField()
    active = models.IntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

class SubCategory(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcat_name = models.CharField(max_length=250, null=False)
    subcat_desc = models.TextField()
    active = models.IntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

class Blog(models.Model):
    user_id=models.ForeignKey(BloggerLogin, on_delete=models.CASCADE)
    com_id=models.ForeignKey(Company, on_delete=models.CASCADE,default=-1)
    cat_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    subcat_id=models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    blog_title=models.CharField(max_length=300,null=False)
    blog_desc=models.TextField()
    blog_image=models.ImageField(upload_to='uploads/blog_image/', default='blog/images/already.png')
    blog_banner=models.ImageField(upload_to='uploads/blog_banner/', default='blog/images/already.png')
    blog_video=models.CharField(max_length=400)
    active = models.IntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)


class BlogSeo(models.Model):
    user_id=models.ForeignKey(BloggerLogin, on_delete=models.CASCADE)
    blog_id=models.ForeignKey(Blog, on_delete=models.CASCADE)
    seo_tag=models.CharField(max_length=300)
    seo_image=models.ImageField(upload_to='uploads/seo_image/', default='blog/images/already.png')
    seo_desc = models.TextField()
    seo_url=models.URLField()
    active = models.IntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)