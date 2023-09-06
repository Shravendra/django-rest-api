from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, RegexValidator
import re

class Company(models.Model):
    id = models.BigAutoField(primary_key=True)  
    company_name = models.CharField(max_length=255)
    email_id = models.EmailField(unique=True)
    company_code = models.CharField(max_length=5, unique=True, blank=True, validators=[
            RegexValidator(
                regex=r'^[A-Z]{2}\d{2}[EN]$',
                message='Company code must be in the format XX99E or XX99N',
            ),
        ],)  
    strength = models.PositiveBigIntegerField(null=True, blank=True)  
    website = models.URLField(null=True, blank=True)  
    created_time = models.DateTimeField()  
    
    def validate_company_code(self, value):
        if len(value) != 5:
            raise ValidationError('Company code must be 5 characters long')
        if not value[:2].isalpha():
            raise ValidationError('First two characters must be alphabets')
        if not value[2:4].isdigit():
            raise ValidationError('Third and fourth characters should be numbers')
        if value[4] not in ['E', 'N']:
            raise ValidationError('Fifth character should be either E or N')
    
    def clean(self):
        if self.company_code:
            if not re.match(r'^[A-Z]{2}\d{2}[EN]$', self.company_code):
                raise ValidationError('Company code must be in the format XX99E or XX99N')
        
    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = "Companies"