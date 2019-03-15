from django.db import models
from datetime import datetime
from django.conf import settings
from simple_history.models import HistoricalRecords

class BaseEntity(models.Model):
	id = models.AutoField(primary_key=True)
	created_at = models.DateTimeField('created_at')
	created_by = models.CharField(max_length=20)
	updated_at = models.DateTimeField('updated_at')
	updated_by = models.CharField(max_length=20)
	history = HistoricalRecords(inherit=True)

	class Meta:
		abstract = True

	def save(self, *args, **kwargs):
		if self.created_at is None:
			self.created_at = datetime.utcnow()
		self.updated_at = datetime.utcnow()
		super(BaseEntity, self).save(*args, **kwargs)

class AutomatedObjects(BaseEntity):
	class Meta:
		abstract = True

	def save(self, *args, **kwargs):
		if self.created_by is None:
			self.created_by = settings.VARIABLES['server_name']
		self.updated_by = settings.VARIABLES['server_name']
		super(AutomatedObjects, self).save(*args, **kwargs)

class Currency(AutomatedObjects):
	name = models.CharField(max_length=20, null=False, blank=False)
	deleted = models.BooleanField(default=False)

class Crypto(AutomatedObjects):
	name = models.CharField(max_length=20, null=False, blank=False)
	deleted = models.BooleanField(default=False)

class CurrencyPrice(AutomatedObjects):
	crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE, null=False)
	currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=False)
	price = models.DecimalField(max_digits=15, decimal_places=6, null=False, blank=False)
	low_price = models.DecimalField(max_digits=15, decimal_places=6, null=False, blank=False)
	high_price = models.DecimalField(max_digits=15, decimal_places=6, null=False, blank=False)
	bid_price = models.DecimalField(max_digits=15, decimal_places=6, null=False, blank=False)
	ask_price = models.DecimalField(max_digits=15, decimal_places=6, null=False, blank=False)

	class Meta:
		unique_together = ('crypto', 'currency')