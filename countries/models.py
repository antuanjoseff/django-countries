from django.contrib.gis.db import models

class Country(models.Model):
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    name = models.CharField(max_length=200)
    bbox = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
            verbose_name = 'País'
            verbose_name_plural = 'Països'

    def __str__(self):
        return '{} ({})'.format(self.name, self.iso3)
    
class Institution(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nom')
    country = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name='País')
    geom = models.PointField(null=True, blank=True, spatial_index=False)
    
    class Meta:
        verbose_name = 'Institució'
        verbose_name_plural = 'Institucions'

    def __str__(self):
        return self.name        