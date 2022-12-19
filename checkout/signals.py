from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Updates order total on lineitem create/update.
    sender = OrderLineItem
    instance = instance of model that sent the signal
    created = boolean sent by Django if this is a new instance or
    updates existing one.
    kwargs = any key word arguments
    Awaits for signal on post_save
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, created, **kwargs):
    """
    Updates order total on lineitem delete.
    """
    instance.order.update_total()
