from django.contrib.gis.db import models
from django.contrib.gis.db import models

class Country(models.Model):
    iso3 = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=200)
    geom = models.MultiPolygonField(spatial_index=False, null=True, blank=True)
    bbox = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
            verbose_name = 'País'
            verbose_name_plural = 'Països'

    def __str__(self):
        return self.name


class Person(models.Model):
    class Meta:
        verbose_name = 'Perfil de mobilitat'
        verbose_name_plural = 'Perfils de mobilitats'
    
    def __str__(self):
        return self.type

    type = models.CharField(max_length=255, verbose_name='Nom')


class Mobility(models.Model):
    class Meta:
        verbose_name = 'Mobilitats'
        verbose_name_plural = 'Mobilitats'
    
    def __str__(self):
        return "{} {} {} ({})".format(self.in_or_out, self.staying_units, self.staying_time_units, self.type)

    IN_OUT_CHOICES = (
        ("in", "in"),
        ("out", "out"),
    )

    TIME_UNIT_CHOICES = (
        ("days", "Dies"),
        ("months", "Mesos"),
        ("years", "Anys"),
    )

    type = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Tipus de mobilitat')
    in_or_out = models.CharField(max_length=9,
                  choices=IN_OUT_CHOICES,
                  default="out")
    staying_time_units = models.CharField(max_length=9,
                  choices=TIME_UNIT_CHOICES,
                  default="days", verbose_name='Tipus d \'estada')
    staying_units = models.IntegerField(default=1, verbose_name="Número de dies / mesos / anys")

    institution = models.ForeignKey('Institution', on_delete=models.CASCADE, verbose_name='Institució', null=True, blank=True)



class MobilityCalendar(models.Model):
    class Meta:
        verbose_name = 'Calendarització de les mobilitats'
        verbose_name_plural = 'Calendaritzacions de les mobilitats'

    IN_OUT_CHOICES = (
        ("in", "in"),
        ("out", "out"),
    )

    yeaar = models.IntegerField(blank=False, null=False)
    units = models.IntegerField(blank=False, null=False, verbose_name='Número de persones')
    type = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Tipus de mobilitat')
    in_or_out = models.CharField(max_length=9,
                  choices=IN_OUT_CHOICES,
                  default="out")

    institution = models.ForeignKey('Institution', on_delete=models.CASCADE, verbose_name='Institució', null=True, blank=True)


class MobilityDone(models.Model):
    class Meta:
        verbose_name = 'Mobilitat realizada'
        verbose_name_plural = 'Mobilitats realizades'

    def __str__(self):
        return "{} - {}".format(self.year, self.in_or_out)

    IN_OUT_CHOICES = (
        ("in", "in"),
        ("out", "out"),
    )

    yeaar = models.IntegerField(blank=False, null=False)
    
    in_or_out = models.CharField(max_length=9,
                  choices=IN_OUT_CHOICES,
                  default="out")

    description = models.TextField(null=True, blank=True)

    program = models.CharField(max_length=255, null=True, blank=True)

    institution = models.ForeignKey('Institution', on_delete=models.CASCADE, verbose_name='Institució', null=True, blank=True)



class YearResult(models.Model):
    year = models.IntegerField()

    description = models.CharField(max_length=255)


class Result(models.Model):
    class Meta:
        verbose_name = 'Resultats obtinguts'
        verbose_name_plural = 'Resultats obtinguts'



    description = models.TextField(null=True, blank=True)
    year_result = models.ForeignKey('YearResult', on_delete=models.CASCADE, verbose_name='Resultats')


class Institution(models.Model):
    class Meta:
            verbose_name = 'Institució'
            verbose_name_plural = 'Institucions'

    def __str__(self):
        return self.name       

    country = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name='País')

    region_ue = models.CharField(max_length=255, verbose_name='Resgió segons UE', null=True, blank=True)

    region_udg = models.CharField(max_length=255, verbose_name='Regió segons UdG', null=True, blank=True)


    #DETALLS DE LA SOLICITUD
    benefits = models.TextField(null=True, blank=True, verbose_name='Beneficis previstos de la col·laboració per a la UdG i per a la contrapart. Alinieació amb les polítiques de l’UE ')

    name = models.CharField(max_length=255, verbose_name='Nom')

    geom = models.PointField( spatial_index=False, verbose_name='Localització', null=True, blank=True)

    empowerment = models.TextField(null=True, blank=True, verbose_name='Fortaleses de la institució per a la UdG i viceversa')

    collaboration_start = models.TextField(null=True, blank=True, verbose_name='Inici de la col·laboració')


    #MOBILITATS SOL·LICITADES
    motive = models.TextField(null=True, blank=True, verbose_name='Fortaleses de la institució per a la UdG i viceversa')


