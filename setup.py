
from setuptools import setup

setup(
    name='sphinx_bernard_theme',
    version='1.0.0',
    url='https://github.com/bernardphp/bernardphp-com/',
    license='MIT',
    author='Henrk Bjornskov',
    author_email='henrik@bjrnskov.dk',
    description='Theme for Bernard repositories and bernardphp.com.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['sphinx_bernard_theme'],
    package_data={'sphinx_bernard_theme': [
        'theme.conf',
        '*.html',
        'static/bernard.css_t',
        'static/img/*.png',
        'static/*.css',
        'static/bootstrap/css/*.css',
        'static/bootstrap/fonts/*.*',
    ]},
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
    ],
)
