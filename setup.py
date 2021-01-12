from setuptools import setup, find_packages
from distutils.command.build import build


class CustomBuild(build):
    sub_commands = [("compile_catalog", lambda x: True)] + build.sub_commands


setup(
    author='Zdeněk Böhm',
    author_email='zdenek.bohm@nic.cz',
    name='djangocms-oidc-form-fields',
    version='1.0.0',
    description='Plugin OIDC (OpenID Connect) for Aldryn form fields.',
    url='https://github.com/CZ-NIC/djangocms-oidc-form-fields',
    license='GPL GNU License',
    platforms=['OS Independent'],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: DjangoCMS',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django CMS',
        'Framework :: Django CMS :: 3.7',
    ),
    install_requires=(
        'django>=2.0.0,<3.0.0',
        'django-cms==3.7.4',
        'djangocms-oidc @ git+https://github.com/CZ-NIC/djangocms-oidc@1.0.0',
        # Default installs aldryn-forms 4.0.1, which is incompatible.
        # Version aldryn-forms > 5.0.4 is compatible only with python 3.7.
        'aldryn-forms @ git+https://github.com/zbohm/aldryn-forms.git@email-into-from_5_0_5',
    ),
    extras_require={
        'quality': ['isort', 'flake8'],
    },
    packages=find_packages(exclude=['tests']),
    cmdclass={"build": CustomBuild},
    setup_requires=["Babel >=2.3"],
    include_package_data=True,
    zip_safe=False
)
