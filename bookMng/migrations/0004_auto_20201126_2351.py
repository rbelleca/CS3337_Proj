# Generated by Django 3.1 on 2020-11-26 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0003_auto_20201124_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='reviewDesciption',
            new_name='review',
        ),
        migrations.RemoveField(
            model_name='review',
            name='reviewTitle',
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(max_length=200),
        ),
    ]
