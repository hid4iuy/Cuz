from django.db import models
import uuid

#共通
class COMMON(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdDateTime = models.DateTimeField(auto_now_add=True)
    modeifiedDateTime = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True