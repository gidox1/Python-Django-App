from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication #for tokenization on log in.
from rest_framework import filters #to filter data by params
from rest_framework.authtoken.views import ObtainAuthToken #gets a token for logIn viewset
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from test_rest_api_app import serializers
from test_rest_api_app import models
from test_rest_api_app import permissions



class HelloApiView(APIView):
    """Our test APIView"""
    serializer_class = serializers.HelloSerializer ## This serializes data from our post requests
    
    def get(self, request, format=None):
        """Returns a list of APIViews features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, delete)',
            'Is similar to a traditional django view',
            'gives you the most control over your app logic',
            'is mapped manually to URLS',
        ]

        return Response({'message': 'hello', 'an api view': an_apiview})

    def post(self, request):
        """Creates a Hello Message with the name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(): 
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else: 
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )##this already returns a dictionary

    def put(self, request, pk=None):
        """Handles updatingg an object""" 
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handles a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Deletes an Object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializers_class = serializers.HelloSerializer #We also use the serializer to validate requests to the viewsets
    
    def list(self, request):
        """Return an Hello Message"""

        a_viewset = [
            'Users actions (list, create, retrieve, update, partial_update)',
            'automatically maps to urls usingg the routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello! ', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create new hello message"""

        serializer = self.serializers_class(data=request.data)  

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        """Handle getting an object by id"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handdles updating part of the object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all() 

    authentication_classes = (TokenAuthentication, ) 
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = (
        'name',
        'email'
    )


class UserLoginApiView(ObtainAuthToken):
    """handle creating user auth token"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles Creating reading and updating profile feed items"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer): 
        """Sets the user profile to be logged in the user"""

        serializer.save(user_profile=self.request.user)

        permission_classes = (
            permissions.UpdateOwnStatus,
            isAuthenticatedOrReadOnly, 
        )