# Generated by Django 3.2.5 on 2021-07-31 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cof', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='cof.product'),
        ),
    ]