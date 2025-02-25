from django.db import models


class About(models.Model):
    title = models.CharField(max_length=202)
    image = models.FileField(upload_to='about/')
    discription = models.TextField()
    paython = models.IntegerField()
    telbot = models.IntegerField()
    backend = models.IntegerField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=202)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="portfolio")
    image = models.FileField(upload_to="portfolio/")

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Services(models.Model):
    title = models.CharField(max_length=202)
    diskiriptions = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Resume(models.Model):
    title = models.CharField(max_length=202)
    job = models.CharField(max_length=202)
    compani = models.CharField(max_length=202)
    lokations = models.CharField(max_length=202)
    time = models.CharField(max_length=202)
    data = models.CharField(max_length=202)
    imag = models.FileField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class HeppiClents(models.Model):
    image = models.FileField()
    discrptions = models.CharField(max_length=202)
    name = models.CharField(max_length=202)
    lich = models.CharField(max_length=202)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Contect(models.Model):
    first_name = models.CharField(max_length=202)
    last_name = models.CharField(max_length=202)
    email = models.EmailField()
    message = models.TextField()

    is_published = models.BooleanField(default=False)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"