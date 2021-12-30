from django.contrib import admin
from .models import Patient
from .models import Doctor
from .models import Medicine
from .models import Examine


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Medicine)
admin.site.register(Examine)
