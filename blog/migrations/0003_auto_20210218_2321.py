# Generated by Django 3.1.6 on 2021-02-19 02:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_blog_subtitulo_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de Publicacion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
