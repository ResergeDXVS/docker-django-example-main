from rest_framework import serializers
GENDER = [
    ("female","Femenino"),
    ("male","Masculino"),
    ("other","Otro")
]

class UserSerializer(serializers.Serializer):
    name            = serializers.CharField(max_length=100)
    paternal_name   = serializers.CharField(max_length=100)
    maternal_name   = serializers.CharField(max_length=100)
    age             = serializers.IntegerField()
    email           = serializers.EmailField()
    gender          = serializers.ChoiceField(choices=GENDER)
    phone           = serializers.CharField(max_length=20)