from django.db import models

class Produk(models.Model):
    nama = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField()

class Transaksi(models.Model):
    tanggal = models.DateTimeField(auto_now_add=True)
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    total_harga = models.DecimalField(max_digits=10, decimal_places=2)
