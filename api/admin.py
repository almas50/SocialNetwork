from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, StackedPolymorphicInline, \
    PolymorphicInlineSupportMixin


from .models import Page, Content, VideoContent, AudioContent, TextContent


class ModelAChildAdmin(PolymorphicChildModelAdmin):
    base_model = Content


@admin.register(VideoContent)
class VideoContentAdmin(ModelAChildAdmin):
    base_model = VideoContent
    list_display = ('title', 'video_link', 'subtitles_link')


@admin.register(AudioContent)
class AudioContentAdmin(ModelAChildAdmin):
    base_model = AudioContent
    list_display = ('title', 'bitrate')


@admin.register(TextContent)
class TextContentAdmin(ModelAChildAdmin):
    base_model = TextContent
    list_display = ('title', 'text')


class ContentInline(StackedPolymorphicInline):

    class VideoContentInline(StackedPolymorphicInline.Child):
        model = VideoContent

    class AudioContentInline(StackedPolymorphicInline.Child):
        model = AudioContent

    class TextContentInline(StackedPolymorphicInline.Child):
        model = TextContent

    model = Page.contents.through
    child_inlines = (
        VideoContentInline,
        AudioContentInline,
        TextContentInline,
    )


@admin.register(Content)
class ContentParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = Content
    child_models = (VideoContent, AudioContent, TextContent)
    search_fields = ('title',)


@admin.register(Page)
class PageAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    search_fields = ('title', )
