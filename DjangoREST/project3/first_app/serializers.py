from rest_framework import serializers
from .models import Student

# Model Serializer
class StudentSerializer(serializers.ModelSerializer):
    # validator
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should start with r')
    name = serializers.CharField(valueErrors=[start_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        read_only_fields = ['name', 'roll']
        extra_kwargs = {'city': {'read_only': True}}

    # field level validation
    def validate_roll(self, value):
        if value >= 200:    
            raise serializers.ValidationError("Seat Full")
        return value

    # object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'tutal' and ct.lower() != 'york':
            raise serializers.ValidationError("City must be York")
        return data

# Validators
# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError('Name should start with r')

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100, validators=[start_with_r])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

#     # post method
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data) 
#     # update method
#     def update(self, instance, validated_data):
#         print(instance.name)
#         instance.name = validated_data.get('name', instance.name)
#         print(instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance

#     # validation
#     # field level validation
#     def validate_roll(self, value):
#         if value >= 200:    
#             raise serializers.ValidationError("Seat Full")
#         return value
    
#     # object level validation
#     def validate(self, data):
#         nm = data.get('name')
#         ct = data.get('city')
#         if nm.lower() == 'rogi' and ct.lower() != 'nana':
#             raise serializers.ValidationError("City must be Nana")
#         return data
