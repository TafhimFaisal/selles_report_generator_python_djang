from .models import Sale
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

@receiver(m2m_changed,sender=Sale.possition.through)

def calculate_totel_price(sender,instance,action,**kwargs):
    totel_price = 0
    print(instance.get_possitions())
    if action == 'post_add' or action=='post_remove':
        positions = instance.get_possitions()
        for position in positions:
            totel_price+=position.price
    instance.totat_price = totel_price
    instance.save()
