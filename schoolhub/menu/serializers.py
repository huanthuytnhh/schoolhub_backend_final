# menu/serializers.py

from rest_framework import serializers
from .models import Menu, MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'amount'] # Exclude 'menu' field as it's handled by parent serializer

class MenuSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only=False) # 'many=True' because a menu has multiple items

    class Meta:
        model = Menu
        fields = ['id', 'date', 'imageUrl', 'items'] # Include 'items' to support nested data

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        menu = Menu.objects.create(**validated_data)
        for item_data in items_data:
            MenuItem.objects.create(menu=menu, **item_data)
        return menu

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)

        instance.date = validated_data.get('date', instance.date)
        instance.imageUrl = validated_data.get('imageUrl', instance.imageUrl)
        instance.save()

        if items_data is not None:
            # Clear existing items and recreate them
            instance.items.all().delete()
            for item_data in items_data:
                MenuItem.objects.create(menu=instance, **item_data)

        return instance