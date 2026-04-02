from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    bio = models.TextField()
    career_interests = models.TextField()
    profile_photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Profiles"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('language', 'Programming Language'),
        ('framework', 'Framework / Library'),
        ('editing', 'Editing Softwares'),
        ('tool', 'Tool / Software'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300, help_text="Comma-separated list of technologies")
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    tiktok_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]

    class Meta:
        ordering = ['order', '-created_at']

class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    year_start = models.IntegerField()
    year_end = models.IntegerField(blank=True, null=True, help_text="Leave blank if currently attending")
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} - {self.school}"

    def get_year_range(self):
        if self.year_end:
            return f"{self.year_start} – {self.year_end}"
        return f"{self.year_start} – Present"

    class Meta:
        ordering = ['-year_start']


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} – {self.subject}"

    class Meta:
        ordering = ['-sent_at']
