# Generated by Django 4.1.3 on 2022-12-02 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_api', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=80),
        ),
    ]
