from rest_framework import serializers
from .models import BankUser,UserPayMethod,UserTransaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankUser
        fields = '__all__'
class PayMethodSerializer(serializers.ModelSerializer):
    userid = UserSerializer()
    class Meta:
        model = UserPayMethod
        fields = ('id','method','userid')
        
        def create(self, validated_data):
            user_data = validated_data.pop('userid')
            data = UserPayMethod.objects.create(**validated_data)
            #UserPayMethod.objects.create(verb=verb, **user_data)
            return data
class TransacSerializer(serializers.ModelSerializer):
    payid = PayMethodSerializer()
    class Meta:
        model = UserTransaction
        fields = ('id','payid','userid','amount')
        def create(self, validated_data):
            user_data = validated_data.pop('payid')
            data = UserTransaction.objects.create(**validated_data)
            #UserPayMethod.objects.create(verb=verb, **user_data)
            return data
