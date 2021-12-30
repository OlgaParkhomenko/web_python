from django.contrib import admin
from .models import Counterparty
from .models import Good
from .models import Consignment
from .models import Lot
from .models import Auction


admin.site.register(Counterparty)
admin.site.register(Good)
admin.site.register(Consignment)
admin.site.register(Lot)
admin.site.register(Auction)
