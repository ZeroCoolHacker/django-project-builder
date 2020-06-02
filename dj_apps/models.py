from django.db import models
from django.template.loader import render_to_string

# Create your models here.
class Dj_App(models.Model):
    """Model definition for Dj_App."""

    name = models.CharField('App Name', max_length=50)
    label = models.CharField('App Label', max_length=50)
    verbose_name = models.CharField('Verbose Name', max_length=50)

    class Meta:
        """Meta definition for Dj_App."""

        verbose_name = 'Dj_App'
        verbose_name_plural = 'Dj_Apps'

    def __str__(self):
        """Unicode representation of Dj_App."""
        return f'{self.name} - {self.label} - {self.verbose_name}'

    def save(self):
        """Save method for Dj_App."""
        self.generate_file()
        self.super().save()

    def get_absolute_url(self):
        """Return absolute url for Dj_App."""
        return ('')

    def generate_file(self):
        context = {
            'name': self.name,
            'label': self.label,
            'verbose_name': self.verbose_name
        }
        template = render_to_string('builder/app_builder.html', context)
        with open('generated_app.py', 'w') as f:
            f.write(template)
        print("Done")

