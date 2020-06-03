from django.db import models

# Create your models here.
class Dj_Model(models.Model):
    """Model definition for Dj_Model."""

    name = models.CharField('Model Name', max_length=100)
    verbose_name = models.CharField('Verbose Name', max_length=100)
    verbose_name_plural = models.CharField('Verbose Plural name', max_length=100)

    class Meta:
        """Meta definition for Dj_Model."""

        verbose_name = 'Dj_Model'
        verbose_name_plural = 'Dj_Models'

    def __str__(self):
        """Unicode representation of Dj_Model."""
        return self.name




class Dj_ModelField(models.Model):
    """Model definition for Dj_ModelField."""

    type = models.CharField('Field Type', max_length=50)

    class Meta:
        """Meta definition for Dj_ModelField."""

        verbose_name = 'Dj_ModelField'
        verbose_name_plural = 'Dj_ModelFields'

    def __str__(self):
        """Unicode representation of Dj_ModelField."""
        return self.type



class Dj_ModelLine(models.Model):
    """Model definition for Dj_FieldModelMapping."""
    model = models.ForeignKey(Dj_Model, on_delete=models.CASCADE)
    field_name = models.CharField('Field Name', max_length=100)
    field = models.ForeignKey(Dj_ModelField, on_delete=models.CASCADE)
    blank = models.BooleanField(default=False)
    null = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Dj_FieldModelMapping."""

        verbose_name = 'Dj_FieldModelMapping'
        verbose_name_plural = 'Dj_FieldModelMappings'

    def __str__(self):
        """Unicode representation of Dj_FieldModelMapping."""
        return f'{self.field_name} = {self.field}()'


