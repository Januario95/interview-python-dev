# Generated by Django 3.2 on 2022-03-25 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_usermodel_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['date_sent']},
        ),
    ]
