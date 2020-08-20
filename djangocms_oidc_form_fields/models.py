from django.db import models
from django.utils.translation import ugettext_lazy as _

from aldryn_forms.models import FieldPlugin


class OIDCFieldPlugin(FieldPlugin):

    unmodifiable = models.BooleanField(
        verbose_name=_("Unmodifiable"), default=True,
        help_text=_("The value of the field cannot be changed by the user.")
    )
    oidc_attributes = models.CharField(
        verbose_name=_('OIDC attributes'), max_length=255, null=True, blank=True,
        help_text=_('OIDC attributes handovered from provider (names separated by space).')
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.pk is None and self.cmsplugin_ptr_id is not None:
            self.cmsplugin_ptr_id = None
        return super().save(force_insert, force_update, using, update_fields)
