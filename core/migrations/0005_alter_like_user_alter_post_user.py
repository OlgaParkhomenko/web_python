# Generated by Django 4.0 on 2022-01-03 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0004_alter_like_user_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
