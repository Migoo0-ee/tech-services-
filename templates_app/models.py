from unicodedata import category
from django.db import models

TEMPLATE_TYPE_CHOICES = [
    ('frontend', 'Frontend'),
    ('backend', 'Backend'),
    ('ai', 'AI Models'),
    ('ui-ux', 'UI & UX'),
    ('mobile', 'Mobile App'),
    ('desktop', 'Desktop App'),
]

class Templates(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='templates_app/')
    category = models.CharField(max_length=20, choices=TEMPLATE_TYPE_CHOICES)
    is_paid = models.BooleanField(default=False)  
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        type_text = "Paid" if self.is_paid else "Free"
        return f"{self.title} ({self.category} - {type_text})"


