from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getCourses(request):
    return Response({"msg": "courses"})
