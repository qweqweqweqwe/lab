from rest_framework import serializers
from .models import Task
from .models import Tasklist
from .models import Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'completed', 'date_created', 'date_modified', 'due_date', 'priority', 'tags')
        read_only_fields = ('date_created', 'date_modified')


class TasklistSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tasklist
        fields = ('id', 'name', 'tasks')