from django.db import models
from django.contrib.auth.models import User

from package.models import Package
# Create your models here.


# class Migrate(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     upgrade = models.BooleanField(blank=True)
#     downgrade = models.BooleanField(blank=True)
#     package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user


class Upgrade(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Downgrade(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)
    is_paid = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
