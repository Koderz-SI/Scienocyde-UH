from django.db import models

# Create your models here.
class Host(models.Model):
    # id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    org = models.CharField(max_length=200)
    type_org = models.CharField(max_length=100, default='School')
    designation = models.CharField(max_length=150)
    phone = models.PositiveIntegerField()
    purpose = models.TextField()
    detail = models.TextField()
    theme = models.CharField(max_length=250)
    guidelines = models.TextField()
    elig_cri = models.TextField()
    slug = models.SlugField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.org

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']
