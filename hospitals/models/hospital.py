from django.db import models

# Create your models here.

class Hospital(models.Model):
  name = models.CharField("имя больници",max_length=50)
  description = models.TextField("описание")
  address = models.CharField("Адрес", max_length=80)
  city = models.CharField("Город", max_length=50)
  category = models.ManyToManyField(
      "hospitals.category",  related_name="hospitals")
  contact = models.OneToOneField("hospitals.contact", on_delete=models.CASCADE )

  class Meta:
    verbose_name = "Больница"
    verbose_name_plural = "Больници"

  def __str__(self): 
    return f"{self.name}"

