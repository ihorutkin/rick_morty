from rest_framework import serializers

from characters.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ["api_id", "name", "status", "species", "gender", "image"]

        read_only_fields = ["api_id"]
