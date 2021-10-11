from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Reviews

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True,read_only=True)
    watchlist = WatchListSerializer(many=True,read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"

# def name_length(name):
#     if len(name) <5:
#         raise serializers.ValidationError("name is too short")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length]) 
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name')
#         instance.description = validated_data.get('description')
#         instance.active = validated_data.get('active')
#         instance.save()
#         return instance

#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Tityle and Description are same")
#         else:
#             return data

    # def validate_name(self, name):
    #     if len(name) <5:
    #         raise serializers.ValidationError("name is too short")
    #     else:
    #         return name
