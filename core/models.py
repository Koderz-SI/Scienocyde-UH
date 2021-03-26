from django.db import models

# Create your models here.
class Host(models.Model):
    # id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, default="null")
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    org = models.CharField(max_length=200)
    type_org = models.CharField(max_length=100, default="School")
    designation = models.CharField(max_length=150)
    phone = models.PositiveIntegerField()
    purpose = models.TextField()
    detail = models.TextField()
    theme = models.CharField(max_length=250)
    guidelines = models.TextField()
    elig_cri = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.org

    class Meta:
        ordering = ["-date"]


class Participant(models.Model):
    # id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, default="null")
    School_Name = models.CharField(max_length=50)
    School_Phone_no = models.CharField(max_length=150)
    School_Email_address = models.EmailField(max_length=100)
    School_Address = models.CharField(max_length=200)
    State = models.CharField(max_length=100)
    Student_Name_1 = models.CharField(max_length=50)
    Contact_no1 = models.CharField(max_length=150)
    Email_address1 = models.EmailField(max_length=100)
    House_Address1 = models.CharField(max_length=200)
    gender1 = models.CharField(max_length=100)
    Student_Name_2 = models.CharField(max_length=50, default="null")
    Contact_no2 = models.CharField(max_length=150, default="null")
    Email_address2 = models.EmailField(max_length=100, default="null")
    House_Address2 = models.CharField(max_length=200, default="null")
    Gender2 = models.CharField(max_length=100, default="null")
    Title_of_your_project = models.CharField(max_length=200)
    Question_or_Problem = models.CharField(max_length=100)
    Hypothesis_or_possible_solution = models.CharField(max_length=50)
    Materials_needed = models.CharField(max_length=150)
    Results = models.EmailField(max_length=100)
    Image_of_Project = models.CharField(max_length=200)
    Link_of_your_project = models.CharField(max_length=100)
    host_id = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Student_Name_1

    class Meta:
        ordering = ["-date"]
