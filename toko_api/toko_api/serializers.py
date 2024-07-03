from rest_framework import serializers
from .models import Produk
from .models import transaksi

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = '__all__'

class TransaksiSerializer(serializers.ModelSerializer):
    produk = ProdukSerializer()

    class Meta:
        model = Transaksi
        fields = '__all__'