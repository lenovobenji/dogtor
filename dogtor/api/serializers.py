from rest_framework import serializers

# Modelos
from vet.models import PetOwner, Pet


# HTTP -> body
# Serializadores -> Representacion de nuestra API
class OwnersSerializers(serializers.HyperlinkedModelSerializer):
    """Pet owners serializer."""

    class Meta:
        model = PetOwner
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "phone",
            "created_at",
        ]


class PetsSerializer(serializers.HyperlinkedModelSerializer):
    """Pet serializer."""

    owner = serializers.PrimaryKeyRelatedField(
        queryset=PetOwner.objects.all(), many=False
    )

    class Meta:
        model = Pet
        fields = [
            "name",
            "type",
            "created_at",
            "owner",  # foreign key
        ]


class OwnersListSerializer(serializers.ModelSerializer):
    """Serializer to list all Pet Owners."""

    class Meta:
        model = PetOwner
        fields = ["first_name", "last_name"]


class OwnersDetailSerializer(serializers.ModelSerializer):
    """Serializer for the detail of a Pet Owner."""

    class Meta:
        model = PetOwner
        fields = "__all__"
        
        
        
class OwnersSerializer(serializers.ModelSerializer):
    """Serializer to list all Pet Owners."""

    class Meta:
        model = PetOwner
        fields = ["first_name", "last_name"]        
        
        
class OwnersCreateSerializer(serializers.ModelSerializer):
    """Serializer for the detail of a Pet Owner."""

    class Meta:
        model = PetOwner
        fields = "__all__"        
        
        
class OwnersUpdateSerializer(serializers.ModelSerializer):
    """Serializer for the detail of a Pet Owner."""

    class Meta:
        model = PetOwner
        fields = "__all__"        
        
        
        
class OwnersDeleteSerializer(serializers.ModelSerializer):
    """Serializer for the detail of a Pet Owner."""

    class Meta:
        model = PetOwner
        fields = "__all__"        
        



class OwnersListCreateView(serializers.ModelSerializer):
    """Serializer for the detail of a Pet Owner."""

    class Meta:
        model = PetOwner
        fields = "__all__"         
class OwnersRetrieveUpdateDestroyAPIView(serializers.ModelSerializer):
    """Serializer for the detail of a Pet Owner."""

    class Meta:
        model = PetOwner
        fields = "__all__" 
        