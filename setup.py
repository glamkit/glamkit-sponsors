from setuptools import setup, find_packages

setup(
    name='glamkit-sponsors',
    version='0.5.0',
    author='Thomas Ashelford',
    author_email='thomas@interaction.net.au',
    description='A Django app to manage sponsor logos',
    url='http://github.com/glamkit/glamkit-sponsors',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)