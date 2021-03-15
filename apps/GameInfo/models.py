from django.db import models

# Create your models here.
class BJLGoodRecord(models.Model):
    content = models.TextField()
    filter_len = models.IntegerField(blank=True, null=True)
    filter_single = models.IntegerField(blank=True, null=True)
    filter_double = models.IntegerField(blank=True, null=True)
    cut_start = models.IntegerField(blank=True, null=True)
    cut_end = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "bjl_ok_record"