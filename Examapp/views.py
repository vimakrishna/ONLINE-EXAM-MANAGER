
from rest_framework.views import APIView
from rest_framework.response import Response
from Examapp.models import QuestionDb
from Examapp.serializers import QuestionSerializer


class QuestionView(APIView):

    def get(self, request):
        questions = QuestionDb.objects.all()
        serializer_instance = QuestionSerializer(questions, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():
            original_data = serializer_instance.validated_data
            QuestionDb.objects.create(**original_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)


class QuestionsRetreiveUpadteDeleteView(APIView):

    
    def get(Self, request, pk):

        qs =QuestionDb.objects.get(id=pk)
        serializer_instance = QuestionSerializer(qs)

        return Response(data=serializer_instance.data)


    def put(self, request, pk):
        form_data = request.data
        serializer_instance = QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            QuestionDb.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self, request, pk):
        QuestionDb.objects.filter(id=pk).delete()
        return Response({"message": "Question deleted successfully!"})

