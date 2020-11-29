from rest_framework import serializers
from .models import Answer, Question, Poll
from django.forms import ValidationError


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['pk', 'title', ]


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, source='question_set', )

    class Meta:
        model = Poll
        fields = ['pk', 'title', 'is_active', 'date_start', 'date_finish', 'questions', ]


class AnswerSerializer(serializers.ModelSerializer):
    # answers = serializers.JSONField(required=False)

    class Meta:
        model = Answer
        fields = ['pk', 'username', 'poll', 'created', 'question', 'answers', ]
