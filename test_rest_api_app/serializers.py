##Our APIView for POST and UPDATE needs a serializer.
from rest_framework import serializers
from test_rest_api_app import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field fortestng our APIView"""##define the fields you want to serialize here

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""#docString

    class Meta: ##a metaclass defines the behavior of classes and their instances. like an interface but in this case it points to the model
        model = models.UserProfile
        fields = (
            'id',
            'email',
            'name',
            'password'
        )##a tuple
        extra_kwargs = {
            'password': {
                'write_only' : True,
                'style': {
                    'input_type': 'password'###hash the password on write
                }
            }
        }##this is a dictionary for fields that are sensitive like the password, it help us set permission for the fields.. extra_keywordsargs :)
    
    def create(self, validated_data): ##We're having this create method to overwrite the default create..
        """Create and return new User"""

        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile' : {'read_only': True}}