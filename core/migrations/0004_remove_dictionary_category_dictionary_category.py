# Generated by Django 4.2 on 2023-04-25 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_is_start_term_term_is_star_term'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dictionary',
            name='category',
        ),
        migrations.AddField(
            model_name='dictionary',
            name='category',
            field=models.ManyToManyField(related_name='dictionary_category', to='core.dictionarycategory'),
        ),
    ]
