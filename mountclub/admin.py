from django.contrib import admin
from .models import Participant
from .models import Country
from .models import Mountain
from .models import ClimbingEvent


admin.site.register(Participant)
admin.site.register(Country)
admin.site.register(Mountain)
admin.site.register(ClimbingEvent)
