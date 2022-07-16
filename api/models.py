from django.db import models
from polymorphic.models import PolymorphicModel


class Content(PolymorphicModel):
    title = models.CharField(max_length=255, verbose_name='название')
    counter = models.PositiveIntegerField(verbose_name='счетчик', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'


class VideoContent(Content):
    video_link = models.URLField(verbose_name='ссылка на видео')
    subtitles_link = models.URLField(verbose_name='ссылка на субтитры', blank=True)

    class Meta:
        verbose_name = 'Видео контент'
        verbose_name_plural = 'Видео контент'


class AudioContent(Content):
    bitrate = models.PositiveIntegerField(verbose_name='битрейт бит/c')

    class Meta:
        verbose_name = 'Аудио контент'
        verbose_name_plural = 'Аудио контент'


class TextContent(Content):
    text = models.TextField(verbose_name='текст')

    class Meta:
        verbose_name = 'Текстовый контент'
        verbose_name_plural = 'Текстовый контент'


class Page(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    contents = models.ManyToManyField(Content, related_name='pages', verbose_name='контент', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
