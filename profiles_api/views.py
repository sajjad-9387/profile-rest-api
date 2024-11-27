from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""


    def get(self, request, format=None):
        """Return a list of api views"""
        an_apiview = [
            'A',
            'B',
            'C',
            'D',
        ]

        return Response({'message': 'HELLO', 'an_apiview': an_apiview})
