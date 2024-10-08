from notes.models import Note
from rest_framework.serializers import ModelSerializer


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ["title", "text"]
