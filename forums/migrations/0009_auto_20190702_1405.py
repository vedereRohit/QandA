# Generated by Django 2.2.2 on 2019-07-02 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0008_auto_20190630_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='votes',
            field=models.ManyToManyField(blank=True, to='forums.Votes'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='tags',
            field=models.ManyToManyField(blank=True, to='forums.Tags'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='votes',
            field=models.ManyToManyField(blank=True, to='forums.Votes'),
        ),
    ]
