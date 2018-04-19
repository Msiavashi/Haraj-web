from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from auction.models import Customer

class userSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=Customer.objects.all())])
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=Customer.objects.all())])
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        user = Customer.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user
    
    class Meta:
        model = Customer
        fields = ('id', 'username', 'email', 'password')