from rest_framework import serializers
from .models import Attribute, Hero, Role, HeroRoles, Aspects, Skills, News


class HeroIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ['id']


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class HeroSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(read_only=True)

    class Meta:
        model = Hero
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class HeroRolesSerializer(serializers.ModelSerializer):
    hero = HeroIdSerializer(read_only=True)
    role = RoleSerializer(read_only=True)

    class Meta:
        model = HeroRoles
        fields = '__all__'


class AspectsSerializer(serializers.ModelSerializer):
    hero = HeroIdSerializer(read_only=True)

    class Meta:
        model = Aspects
        fields = '__all__'


class SkillsSerializerHero(serializers.ModelSerializer):
    hero = HeroIdSerializer(read_only=True)

    class Meta:
        model = Skills
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
    hero = HeroSerializer(read_only=True)

    class Meta:
        model = Skills
        fields = '__all__'
