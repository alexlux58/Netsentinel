from django.db import models


class Alert(models.Model):
    timestamp = models.DateTimeField()
    src_ip = models.GenericIPAddressField()
    dest_ip = models.GenericIPAddressField()
    dest_port = models.IntegerField(null=True, blank=True)
    signature = models.CharField(max_length=255)
    anomaly_score = models.IntegerField(default=0)
    is_anomaly = models.BooleanField(default=False)
    geoip_country = models.CharField(max_length=100, null=True, blank=True)
    ip_reputation = models.IntegerField(default=0)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.timestamp} - {self.signature}"
