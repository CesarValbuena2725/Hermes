from rest_framework import serializers
from .models import Developer


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(trim_whitespace=True, write_only=True)

    class Meta:
        model = Developer
        fields =  ['username', 'email', 'password','github','first_name','last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if(data['password'] != data['password_confirm']):
            raise serializers.ValidationError("Passwords don't match")
        del data['password_confirm']
        return data
        
    
    def create(self, validated_data):
        dev_password = validated_data.pop('password')
        dev = Developer(**validated_data)
        dev.set_password(dev_password)
        dev.save()
        return dev


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Developer
        fields = ['first_name','last_name','username','email','github']
        
    