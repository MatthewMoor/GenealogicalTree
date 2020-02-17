from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Relation(MPTTModel):
    person = models.CharField(
        max_length=50, 
        )
    parent = TreeForeignKey(
        to='self',
        related_name='children',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{}".format(self.person)

    class MPTTMeta:
        order_insertion_by = ['parent']