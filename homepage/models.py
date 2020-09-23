from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=80)
    website = models.URLField(max_length=100)

class ShoeType(models.Model):
    style = models.CharField(max_length=80)

class ShoeColor(models.Model):
    R = 'Red'
    O = 'Orange'
    Y = 'Yellow'
    G = 'Green'
    B = 'Blue'
    I = 'Indigo'
    V = 'Violet'
    Bl = 'Black'
    W = 'White'

    color_choices = [
        (R, 'Red'),
        (O, 'Orange'),
        (Y, 'Yellow'),
        (G, 'Green'),
        (B, 'Blue'),
        (I, 'Indigo'),
        (V, 'Violet'),
        (W, 'White'),
        (Bl, 'Black'),
    ]

    color_name = models.CharField(max_length=8, choices=color_choices, default='Black')


class Shoe(models.Model):
    size = models.IntegerField(null=False)
    brand_name = models.CharField(max_length=80)
    material = models.CharField(max_length=80)
    fasten_type = models.CharField(max_length=80)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name = 'manufacturer')
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE, related_name='color')
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE, related_name='shoe_type')


# While Joe Kaufield types away tirelessly at his computer writing line after line of code,
# he thinks back to when he was just a young boy growing up in the African Savanna. He remembers
# when he would frolick around with gazelles in his free time, and having to hunt his food with
# nothing but his trusty spear and bare hands.
# Joe smiles fondly, remebering a simpler time.