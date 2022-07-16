# Generated by Django 4.0.6 on 2022-07-14 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('counter', models.PositiveIntegerField(verbose_name='счетчик')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=255, verbose_name='название'),
        ),
        migrations.CreateModel(
            name='AudioContent',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.content')),
                ('bitrate', models.PositiveIntegerField(verbose_name='битрейт бит/c')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('api.content',),
        ),
        migrations.CreateModel(
            name='TextContent',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.content')),
                ('text', models.TextField(verbose_name='текст')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('api.content',),
        ),
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.content')),
                ('video_link', models.URLField(verbose_name='ссылка на видео')),
                ('subtitles_link', models.URLField(blank=True, verbose_name='ссылка на субтитры')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('api.content',),
        ),
        migrations.AddField(
            model_name='page',
            name='contents',
            field=models.ManyToManyField(blank=True, related_name='pages', to='api.content', verbose_name='контент'),
        ),
    ]
