# Generated by Django 3.1.7 on 2021-03-23 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0005_contact_company"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="company",
        ),
    ]
