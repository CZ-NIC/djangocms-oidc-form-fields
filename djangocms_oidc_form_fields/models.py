from aldryn_forms.models import FieldPluginBase
from django.db import models
from django.utils.translation import ugettext_lazy as _


class OIDCFieldPluginBase(FieldPluginBase):

    unmodifiable = models.BooleanField(
        verbose_name=_("Unmodifiable"), default=True,
        help_text=_("The value of the field cannot be changed by the user.")
    )
    oidc_attributes = models.CharField(
        verbose_name=_('OIDC attributes'), max_length=255, null=True, blank=True,
        help_text=_('OIDC attributes handovered from provider (names separated by space).')
    )

    FIELD_TYPE_OIDC = True

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.pk is None and self.cmsplugin_ptr_id is not None:
            self.cmsplugin_ptr_id = None
        return super().save(force_insert, force_update, using, update_fields)


class OIDCFieldPlugin(OIDCFieldPluginBase):

    def copy_relations(self, oldinstance):
        if hasattr(oldinstance, "option_set"):
            for option in oldinstance.option_set.all():
                option.pk = None  # copy on save
                option.field = self
                option.save()


class OIDCTextAreaFieldPlugin(OIDCFieldPluginBase):
    text_area_columns = models.PositiveIntegerField(
        verbose_name=_('columns'), blank=True, null=True)
    text_area_rows = models.PositiveIntegerField(
        verbose_name=_('rows'), blank=True, null=True)


class OIDCEmailFieldPlugin(OIDCFieldPluginBase):
    email_send_notification = models.BooleanField(
        verbose_name=_('send notification when form is submitted'),
        default=False,
        help_text=_('When checked, the value of this field will be used to '
                    'send an email notification.')
    )
    email_subject = models.CharField(
        verbose_name=_('email subject'),
        max_length=255,
        blank=True,
        default='',
        help_text=_('Used as the email subject when email_send_notification '
                    'is checked.')
    )
    email_body = models.TextField(
        verbose_name=_('Additional email body'),
        blank=True,
        default='',
        help_text=_('Additional body text used when email notifications '
                    'are active.')
    )
