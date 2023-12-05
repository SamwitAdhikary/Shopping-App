# Generated by Django 4.2.8 on 2023-12-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('fashion', 'FASHION'), ('clothes', 'CLOTHES'), ('shoes', 'SHOES'), ('electronics', 'ELECTRONICS')], default='fashion', max_length=30),
        ),
    ]