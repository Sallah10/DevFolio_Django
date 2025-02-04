from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import (
    UserProfile,
    ContactProfile,
    Testimonial,
    Media,
    Portfolio,
    Blog,
    Skill,
    Services
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'timestamp', 'name',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name','score')

@admin.register(Services)
class  ServicesAdmin(admin.ModelAdmin):
     list_display = ('id','name','is_active')