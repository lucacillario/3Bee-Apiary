import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Apiary(models.Model):
    name = models.CharField(
        max_length=50, blank=True, help_text="The name of the apiary"
    )
    address = models.CharField(
        max_length=100, blank=True, help_text="The address of the apiary"
    )
    city = models.CharField(
        max_length=20, blank=True, help_text="The city where the apiary is located"
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, help_text="The apiary longitude value"
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, help_text="The apiary latitude value"
    )

    class Meta:
        verbose_name = "Apiary"
        verbose_name_plural = "Apiaries"

    def hives_count(self) -> int:
        """Returns the total number of hives in this apiary."""
        return self.hives.count()

    def __str__(self) -> str:
        return self.name


class Hive(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the hive")
    apiary = models.ForeignKey(
        Apiary,
        related_name="hives",
        on_delete=models.CASCADE,
        help_text="The apiary where the hive is located",
    )

    class Meta:
        verbose_name = "Hive"
        verbose_name_plural = "Hives"

    def __str__(self) -> str:
        return self.name


class Device(models.Model):
    class Status(models.TextChoices):
        OK = "OK", _("Device status is ok")
        WARNING = "WARN", _("Device status is warning")
        ERROR = "ERR", _("Device status is error")
        CRITICAL = "CRIT", _("Device status is critical")
        UNKNOWN = "UNK", _("Device status is unknown")

    serial = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text="Device serial number",
    )
    is_on = models.BooleanField(
        default=False, help_text="Whether the device is ON or OFF"
    )
    status = models.CharField(
        max_length=5,
        choices=Status.choices,
        default=Status.UNKNOWN,
        help_text="Device status",
    )
    hive = models.OneToOneField(
        Hive,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Hive where the device is located",
    )

    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"

    def __str__(self) -> str:
        return str(self.serial)
