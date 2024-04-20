# Generated by Django 5.0.2 on 2024-03-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_room_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='room',
            name='tags',
            field=models.ManyToManyField(blank=True, to='book.tag'),
        ),
    ]
