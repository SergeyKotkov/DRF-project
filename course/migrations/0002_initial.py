# Generated by Django 5.1.2 on 2024-11-09 13:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("course", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец курса",
            ),
        ),
        #migrations.AddField(
         #   model_name="lesson",
        #    name="course",
         #   field=models.ForeignKey(
         #       on_delete=django.db.models.deletion.CASCADE,
          #      related_name="lessons",
          #      to="course.course",
           #     verbose_name="Курс",
           # ),
        #),
        migrations.AddField(
            model_name="lesson",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец курса",
            ),
        ),
    ]
