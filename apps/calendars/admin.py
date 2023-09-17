from django.contrib import admin
from .models import (Actual, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,
                     ActualButtonOne, ActualButtonTwo, ActualButtonThird, ActualButtonFourth,
                     ActualButtonFifth
                     )

admin.site.register(Actual)
admin.site.register(ActualButtonOne)
admin.site.register(ActualButtonTwo)
admin.site.register(ActualButtonThird)
admin.site.register(ActualButtonFourth)
admin.site.register(ActualButtonFifth)
admin.site.register(Monday)
admin.site.register(Tuesday)
admin.site.register(Wednesday)
admin.site.register(Thursday)
admin.site.register(Friday)
admin.site.register(Saturday)


