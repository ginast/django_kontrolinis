# Generated by Django 4.0.3 on 2022-10-25 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Pavadinimas')),
                ('summary', models.TextField(help_text='Trumpas žaidimo aprašymas', max_length=1000, verbose_name='Aprašymas')),
                ('genre', models.ManyToManyField(help_text='Išrinkite žanrą(us) šiam žaidimui', to='reviews.genre')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.publisher')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
