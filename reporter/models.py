from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models


class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Incidences"


class SaoPaulo(models.Model):
    uf = models.CharField(max_length=254)
    nome = models.CharField(max_length=254)
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "SaoPaulo"


class Municipios(models.Model):
    id = models.AutoField(primary_key=True)
    cd_geocodm = models.CharField(max_length=20)
    nm_municip = models.CharField(max_length=60)
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.nm_municip

    class Meta:
        verbose_name_plural = "Municipios"