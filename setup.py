from distutils.command.build import build

from setuptools import find_packages, setup


class CustomBuild(build):
    sub_commands = [("compile_catalog", lambda x: True)] + build.sub_commands


setup(
    author='Zdeněk Böhm',
    author_email='zdenek.bohm@nic.cz',
    name='djangocms-oidc-form-fields',
    version='3.0.1',
    description='Plugin OIDC (OpenID Connect) for Aldryn form fields.',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    url='https://github.com/CZ-NIC/djangocms-oidc-form-fields',
    license='GPL GNU License',
    platforms=['OS Independent'],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Framework :: Django CMS :: 4.1',
    ),
    python_requires='>=3.10',
    install_requires=(
        # 'django-cms~=4.1',
        # 'djangocms-aldryn-forms~=7.0',
        "djangocms-aldryn-forms[captcha] @ git+https://github.com/CZ-NIC/djangocms-aldryn-forms@b7368e4a6abb32744e8fa2f2e7ee914cd0b62c00",
        # 'djangocms-oidc~=4.0',
        "djangocms-oidc @ git+https://github.com/CZ-NIC/djangocms-oidc@upgrade-cms",
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
