from django.db import models

# Create your models here.

class Establishment(models.Model):
  name = models.CharField("название заведения",max_length=50)
  description = models.TextField("описание")
  address = models.CharField("Адрес", max_length=80)
  city = models.CharField("Город", max_length=50)
  category = models.ManyToManyField(
      "establishments.category",  related_name="establishments")
  contact = models.OneToOneField(
      "establishments.contact", on_delete=models.CASCADE)

  class Meta:
    verbose_name = "заведения"
    verbose_name_plural = "заведение"

  def __str__(self): 
    return f"{self.name}"

