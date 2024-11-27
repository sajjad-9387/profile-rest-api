from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of api views"""
        an_apiview = [
            'A',
            'B',
            'C',
            'D',
        ]
        return Response({'message': 'HELLO', 'an_apiview': an_apiview})
    
    def post(self, request):
        """create hello message with out name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updateing an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello messages"""
        a_viewset = [
            '1',
            '2',
            '3',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create (self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello my love: {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Retriving an object by ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Update an object by ID"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """some part of an object is updated"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Delete/Remove/Destroy an object"""
        return Response({'http_method': 'DELETE'})