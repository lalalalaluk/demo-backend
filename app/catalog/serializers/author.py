from rest_framework import serializers

from app.catalog.models.author import Author


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    date_of_death = serializers.DateField(required=False, allow_null=True)

    def to_internal_value(self, data):
        # Convert empty strings to None for date fields
        if data.get("date_of_birth") == "":
            data["date_of_birth"] = None
        if data.get("date_of_death") == "":
            data["date_of_death"] = None
        return super().to_internal_value(data)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.date_of_birth = validated_data.get(
            "date_of_birth", instance.date_of_birth
        )
        instance.date_of_death = validated_data.get(
            "date_of_death", instance.date_of_death
        )
        instance.save()
        return instance
