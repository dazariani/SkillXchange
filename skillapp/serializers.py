from rest_framework import serializers
from .models import SkillClass, Enrollment, Review, CustomUser

class SkillClassSerializer(serializers.ModelSerializer):
  tutor = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), queryset=CustomUser.objects.all())

  class Meta:
    model = SkillClass
    fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
  client = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), queryset=CustomUser.objects.all())

  class Meta:
    model = Review
    fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
  student = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), queryset=CustomUser.objects.all())

  class Meta:
    model = Enrollment
    fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ['id', 'username', 'password', 'isTutor', 'isStudent']
    extra_kwargs = {
      'password': {'write_only': True}
    }


  def create(self, validated_data):
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)
    if password is not None:
      instance.set_password(password)
    instance.save()
    return instance