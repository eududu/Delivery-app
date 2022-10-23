from rest_framework import serializers
from .models import Store, Address


class AddressSerializar(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'number', 'district', 'complement', 'zipcode']


class StoreSerializer(serializers.ModelSerializer):
    address = AddressSerializar()

    class Meta:
        model = Store
        fields = ['id', 'name', 'description', 'address']

    def create(self, request):
        return Store.objects.create(
            name=request.get('name'),
            description=request.get('description'),
            address= Address.objects.create(**request.get('address')),
        )
    
    def update(self, instance, request):
        instance.name = request.get('name', instance.name)
        instance.description = request.get('description', instance.description)

        if 'address' in request:
            address = request.get('address')
            instance.address.street = address.get('street')
            instance.address.number = address.get('number')
            instance.address.district = address.get('district')
            instance.address.complement = address.get('complement')
            instance.address.zipcode = address.get('zipcode')

        instance.save()

        return instance
