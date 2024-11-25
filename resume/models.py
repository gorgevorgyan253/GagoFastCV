from django.db import models

# Create your models here.
class Resume(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    photo = models.ImageField(upload_to='resumes/photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Model for skills
class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model for work experience
class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

# Model for education
class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=100)
    school_name = models.CharField(max_length=200)
    graduation_year = models.IntegerField()
    major = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.degree} from {self.school_name}"

# Model for languages
class Language(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='languages')
    name = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=50, choices=[('Basic', 'Basic'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Fluent', 'Fluent')])

    def __str__(self):
        return f"{self.name} ({self.proficiency})"

# Model for certifications
class Certification(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    date_obtained = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
