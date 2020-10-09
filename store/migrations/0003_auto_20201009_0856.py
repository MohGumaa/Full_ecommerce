# Generated by Django 3.1.1 on 2020-10-09 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20201009_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Outwear')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(blank=True, choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=1, null=True),
        ),
    ]