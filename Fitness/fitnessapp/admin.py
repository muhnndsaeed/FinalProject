from django.contrib import admin
from .models import Profile, Blog , Consultation, Comment , ConComment

admin.site.register(Profile)
admin.site.register(Blog)
admin.site.register(Consultation)
admin.site.register(Comment)
admin.site.register(ConComment)

