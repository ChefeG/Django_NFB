from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from modeltranslation.admin import TranslationAdmin

from .models import ModelNewsLine, ModelСover, ModelMatches, ModelTeams, ModelTopPlayer, ModelStatistics, \
    ModelTopMatches, ModelAnnouncements


@admin.register(ModelNewsLine)
class NewsLineAdmin(admin.ModelAdmin):
    list_display = ['news']
    save_on_top = True
    save_as = True

@admin.register(ModelСover)
class СoverAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'anons')
    list_display_links = ('title',)
    save_on_top = True
    save_as = True
    actions = ['publish', 'unpublish']

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 record has been updated'
        else:
            message_bit = f'{row_update} records have been updated'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 record has been updated'
        else:
            message_bit = f'{row_update} records have been updated'
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Publish'
    publish.allowed_permissions = ('change',)
    unpublish.short_description = 'Unpublish'
    unpublish.allowed_permissions = ('change',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'image'

class MatchesAdminForm(forms.ModelForm):
    description = forms.CharField(
        label='description',
        widget=CKEditorUploadingWidget())

    class Meta:
        model = ModelMatches
        fields = '__all__'

@admin.register(ModelMatches)
class MatchesAdmin(TranslationAdmin):
    list_display = ('team_1', 'team_2', 'date', 'venue')
    list_display_links = ('team_1', 'team_2')
    save_on_top = True
    save_as = True
    form = MatchesAdminForm

@admin.register(ModelTeams)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ('team', 'win', 'draw', 'lose', 'pts')
    list_display_links = ('team',)
    save_on_top = True
    save_as = True

@admin.register(ModelTopPlayer)
class TopPlayerAdmin(admin.ModelAdmin):
    list_display = ('image', 'name')
    list_display_links = ('name',)
    save_on_top = True
    save_as = True

@admin.register(ModelStatistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('discord_members', 'twitter_members', 'nft_in_stake')
    save_on_top = True
    save_as = True

@admin.register(ModelTopMatches)
class TopMatchesAdmin(admin.ModelAdmin):
    list_display = ('team_1_image', 'team_2_image', 'vs', 'description')
    list_display_links = ('team_1_image', 'team_2_image',)
    save_on_top = True
    save_as = True

class AnnouncementsAdminForm(forms.ModelForm):
    description = forms.CharField(
        label='description',
        widget=CKEditorUploadingWidget())
    text = forms.CharField(
        label='description',
        widget=CKEditorUploadingWidget())
    blockquote = forms.CharField(
        label='description',
        widget=CKEditorUploadingWidget())


    class Meta:
        model = ModelAnnouncements
        fields = '__all__'

@admin.register(ModelAnnouncements)
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ('day', 'month', 'image', 'description')
    list_display_links = ('description',)
    save_on_top = True
    save_as = True
    form = AnnouncementsAdminForm



admin.site.site_title = 'NFB'
admin.site.site_header = 'NFT_NFB'
