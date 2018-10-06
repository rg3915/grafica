from django.contrib import admin
from .models import UserProfile, Fotolito, Ctp, ProvaDeCor, Lineatura, Formato, Papel, FineArt


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Lineatura)
class LineaturaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('titulo', )


@admin.register(Formato)
class FormatoAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('titulo', )


@admin.register(Papel)
class PapelAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('titulo', )


@admin.register(Fotolito)
class FotolitoAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('titulo', )


@admin.register(Ctp)
class CtpAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('titulo', )


@admin.register(ProvaDeCor)
class ProvaDeCorAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('titulo', )


@admin.register(FineArt)
class FineArtAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('titulo', )
