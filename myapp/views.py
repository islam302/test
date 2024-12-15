from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def greeting_view(request):
    message = request.data.get('message', '').strip()
    if message == "test":
        return Response({"response": "hello world"}, status=status.HTTP_200_OK)
    return Response({"response": "Message not recognized"}, status=status.HTTP_400_BAD_REQUEST)
