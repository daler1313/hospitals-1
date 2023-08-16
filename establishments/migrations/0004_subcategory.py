# Generated by Django 4.2.4 on 2023-08-14 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0003_remove_category_subcategories'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название под категории')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establishments.category')),
            ],
        ),
    ]
