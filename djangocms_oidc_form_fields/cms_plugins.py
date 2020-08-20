import re

from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from aldryn_forms.cms_plugins import (BooleanField, EmailField,
                                      EmailIntoFromField, FormPlugin,
                                      HiddenField, NumberField, PhoneField,
                                      TextAreaField, TextField)
from aldryn_forms.forms import FormSubmissionBaseForm
from aldryn_forms.signals import form_post_save, form_pre_save
from cms.plugin_pool import plugin_pool
from djangocms_oidc.constants import DJNAGOCMS_USER_SESSION_KEY

from .models import OIDCFieldPlugin


@plugin_pool.register_plugin
class OIDCFormPlugin(FormPlugin):
    name = _('OIDC Form')
    module = _('OpenID Connect Form')

    def process_form(self, instance, request):
        form_class = self.get_form_class(instance, request)
        form_kwargs = self.get_form_kwargs(instance, request)
        form = form_class(**form_kwargs)

        if request.POST.get('form_plugin_id') == str(instance.id) and form.is_valid():
            fields = [field for field in form.base_fields.values()
                      if hasattr(field, '_plugin_instance')]

            # pre save field hooks
            for field in fields:
                field._plugin_instance.form_pre_save(
                    instance=field._model_instance,
                    form=form,
                    request=request,
                )

            form_pre_save.send(
                sender=FormPlugin,
                instance=instance,
                form=form,
                request=request,
            )

            self.form_valid(instance, request, form)

            # post save field hooks
            for field in fields:
                field._plugin_instance.form_post_save(
                    instance=field._model_instance,
                    form=form,
                    request=request,
                )

            form_post_save.send(
                sender=FormPlugin,
                instance=instance,
                form=form,
                request=request,
            )
        elif request.POST.get('form_plugin_id') == str(instance.id) and request.method == 'POST':
            # only call form_invalid if request is POST and form is not valid
            self.form_invalid(instance, request, form)
        return form

    def get_form_class(self, instance, request=None):
        """
        Constructs form class basing on children plugin instances.
        """
        fields = self.get_form_fields(instance, request)
        formClass = (
            type(FormSubmissionBaseForm)
            ('OIDCAldrynDynamicForm', (FormSubmissionBaseForm,), fields)
        )
        return formClass

    def get_form_fields(self, instance, request=None):
        form_fields = {}
        fields = instance.get_form_fields()
        for field in fields:
            plugin_instance = field.plugin_instance
            field_plugin = plugin_instance.get_plugin_class_instance()
            if isinstance(plugin_instance, OIDCFieldPlugin):
                form_fields[field.name] = field_plugin.get_form_field(plugin_instance, request)
            else:
                form_fields[field.name] = field_plugin.get_form_field(plugin_instance)
        return form_fields


class OIDCFieldMixin:
    module = _('OpenID Connect Form Field')
    model = OIDCFieldPlugin

    form_field_enabled_options = [
        'unmodifiable',
        'oidc_attributes',
    ] + TextField.form_field_enabled_options
    fieldset_general_fields = [
        'unmodifiable',
        'oidc_attributes',
    ] + TextField.fieldset_general_fields

    def get_form_field(self, instance, request=None):
        form_field_class = self.get_form_field_class(instance)
        form_field_kwargs = self.get_form_field_kwargs(instance, request)
        field = form_field_class(**form_field_kwargs)
        # allow fields access to their model plugin class instance
        field._model_instance = instance
        # and also to the plugin class instance
        field._plugin_instance = self
        return field

    def get_oidc_attribute_value(self, user_info, attributes):
        values = []
        for key in re.split(r'\s+', attributes):
            value = user_info.get(key)
            values.append("" if value is None else force_text(value))
        return " ".join(values)

    def get_form_field_kwargs(self, instance, request=None):
        kwargs = super().get_form_field_kwargs(instance)
        if instance.unmodifiable:
            kwargs['disabled'] = True
        if request is not None and instance.oidc_attributes:
            user_info = request.session.get(DJNAGOCMS_USER_SESSION_KEY)
            if user_info is not None:
                kwargs['initial'] = self.get_oidc_attribute_value(user_info, instance.oidc_attributes)
        return kwargs


@plugin_pool.register_plugin
class OIDCTextField(OIDCFieldMixin, TextField):
    name = _('OIDC Text Field')


@plugin_pool.register_plugin
class OIDCTextAreaField(OIDCFieldMixin, TextAreaField):
    name = _('OIDC Text Area Field')


@plugin_pool.register_plugin
class OIDCHiddenField(OIDCFieldMixin, HiddenField):
    name = _('OIDC Hidden Field')


@plugin_pool.register_plugin
class OIDCPhoneField(OIDCFieldMixin, PhoneField):
    name = _('OIDC Phone Field')


@plugin_pool.register_plugin
class OIDCNumberField(OIDCFieldMixin, NumberField):
    name = _('OIDC Number Field')


@plugin_pool.register_plugin
class OIDCEmailField(OIDCFieldMixin, EmailField):
    name = _('OIDC Email Field')


@plugin_pool.register_plugin
class OIDCBooleanField(OIDCFieldMixin, BooleanField):
    name = _('OIDC Yes/No Field')


@plugin_pool.register_plugin
class OIDCEmailIntoFromField(OIDCFieldMixin, EmailIntoFromField):
    name = _('OIDC Email into From Field')
