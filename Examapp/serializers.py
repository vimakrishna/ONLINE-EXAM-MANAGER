from rest_framework import serializers
from Examapp.models import QuestionDb

class QuestionSerializer(serializers.Serializer):


    question = serializers.CharField(max_length=100)
    option_A = serializers.CharField(max_length=50)
    option_B = serializers.CharField(max_length=50)
    option_C = serializers.CharField(max_length=50)
    option_D = serializers.CharField(max_length=50)
    correct_answer = serializers.CharField(max_length=50)

