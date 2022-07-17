from collections.abc import Mapping


from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer


from .models import Page, Content, VideoContent, AudioContent, TextContent


class VideoContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContent
        fields = ('title', 'video_link', 'subtitles_link', 'counter')


class AudioContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioContent
        fields = ('title', 'bitrate', 'counter')


class TextContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextContent
        fields = ('title', 'text', 'counter')


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = '__all__'


class ContentPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Content: ContentSerializer,
        VideoContent: VideoContentSerializer,
        AudioContent: AudioContentSerializer,
        TextContent: TextContentSerializer
    }

    def to_representation(self, instance):
        if isinstance(instance, Mapping):
            resource_type = self._get_resource_type_from_mapping(instance)
            serializer = self._get_serializer_from_resource_type(resource_type)
        else:
            serializer = self._get_serializer_from_model_or_instance(instance)

        ret = serializer.to_representation(instance)
        return ret


class PageListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ('title', 'url')


class PageRetrieveSerializer(serializers.ModelSerializer):
    contents = ContentPolymorphicSerializer(read_only=True, many=True)

    class Meta:
        model = Page
        fields = ('title', 'contents')
