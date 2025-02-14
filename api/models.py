from django.db import models
from django.utils.text import slugify

class SafariPackage(models.Model):
    title = models.CharField(max_length=200, unique=True)
    overview = models.TextField(
        help_text="A short summary of the safari package.",
        default="An exciting safari adventure filled with wildlife and breathtaking landscapes."
    )
    full_description = models.TextField(
        help_text="A detailed description covering the safari experience, activities, wildlife, and accommodations.",
        default="Experience an unforgettable safari with breathtaking landscapes, diverse wildlife, and luxury accommodations."
    )
    image = models.ImageField(upload_to='safari_packages/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class SafariItinerary(models.Model):
    safari_package = models.ForeignKey(SafariPackage, related_name="itinerary", on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['day_number']  # Ensure itinerary days are displayed in order

    def __str__(self):
        return f"Day {self.day_number}: {self.title}"

from django.db import models

class Destination(models.Model):
    title = models.CharField(max_length=255, unique=True, default="Maasai Mara National Reserve")
    slug = models.SlugField(unique=True, default="maasai-mara")
    image = models.ImageField(upload_to='destinations/', default="destinations/maasai-mara.jpg")
    highlights = models.TextField(default="Famous for the Great Migration and the Big Five.")
    about = models.TextField(default="Maasai Mara is one of the most famous safari destinations in Kenya.")
    features = models.TextField(default="Big Five spotting, Hot air balloon safari, Maasai cultural experience.")

    def __str__(self):
        return self.title

    
class SafariBooking(models.Model):
    SAFARI_TYPES = [
        ('budget', 'Budget Safari'),
        ('luxury', 'Luxury Safari'),
        ('midrange', 'Mid-range Safari'),
    ]

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    destination = models.CharField(max_length=255)
    safari_type = models.CharField(max_length=20, choices=SAFARI_TYPES)
    time = models.DateTimeField()
    message = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.destination}"
    
    
class SafariAdventure(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='safari_adventures/')

    def __str__(self):
        return self.title