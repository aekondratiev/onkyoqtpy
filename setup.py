#!/usr/bin/env python2


import glob
import os
from distutils.command.build import build
from distutils.core import setup


setup(
    name='onkyoqt',
    version='0.3',
    description='QT GUI for onkyo',
    author='Andry Kondratiev',
    author_email='andry.kondratiev@gmail.com',
    url='https://github.com/massdest/onkyoqtpy',
    license='GPLv3',
    packages=['onkyoqt'],
    keywords=['qt', 'onkyo'],
    install_requires=['onkyo-eiscp'],
    data_files=[('/usr/share/applications', ['share/onkyoqt.desktop']),
                ('/usr/share/icons', ['onkyoqt/icons/onkyo.png']),
                ('/usr/share/icons', ['onkyoqt/icons/onkyo_exit.png']),
                ('/usr/share/icons', ['onkyoqt/icons/onkyo_mute.png']),
                ('/usr/share/icons', ['onkyoqt/icons/onkyo_poweroff.png']),
                ('/usr/share/icons', ['onkyoqt/icons/onkyo_restore.png']),
                ('/usr/share/icons', ['onkyoqt/icons/onkyo_volumedown.png']),
                ('/usr/share/icons', ['onkyoqt/icons/onkyo_about.png']),
                ('/usr/share/icons', ['onkyoqt/icons/onkyo_settings.png']),
                ('/usr/share/icons', ['onkyoqt/icons/onkyo_volumeup.png'])
                ],
        scripts=["bin/onkyoqt"],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Other Audience',
            'Natural Language :: English',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
        ],
)


