from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Tag
from .models import Task
from .models import Tasklist


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'completed',
                  'date_created', 'date_modified', 'due_date',
                  'priority', 'tags',)
        read_only_fields = ('date_created', 'date_modified')


class TasklistSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)
    owner = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Tasklist
        fields = ('id', 'name', 'tasks', 'owner')
