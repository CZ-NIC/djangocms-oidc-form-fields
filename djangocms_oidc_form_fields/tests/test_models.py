from django.test import TestCase

from djangocms_oidc_form_fields.models import OIDCFieldPlugin

# OIDCTextAreaFieldPlugin, OIDCEmailFieldPlugin


class TestOIDCFieldPlugin(TestCase):

    def test_save(self):
        obj = OIDCFieldPlugin()
        obj.save()
        self.assertEqual(obj.pk, obj.cmsplugin_ptr_id)
        self.assertTrue(obj.unmodifiable)
        self.assertIsNone(obj.oidc_attributes)
