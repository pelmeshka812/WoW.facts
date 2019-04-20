# Generated by Django 2.1.7 on 2019-04-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(default='Описание')),
                ('keywords', models.CharField(default='Ключевые слова', max_length=120)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('content', models.TextField()),
                ('visible', models.BooleanField(default=1)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0, verbose_name='Нравится')),
            ],
            options={
                'ordering': ['-id', '-timestamp'],
            },
        ),
    ]
