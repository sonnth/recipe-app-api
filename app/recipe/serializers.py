from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializers for recipe"""

    class Meta:
        model = Recipe()
        fields = [
            'id',
            'title',
            'time_minutes',
            'price',
            'link',
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        return Recipe().objects.create(**validated_data)


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
