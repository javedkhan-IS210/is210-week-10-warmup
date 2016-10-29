#!/usr/bin/env python
#-*- coding: utf- -*-
""" Using update to modify a dictionary"""

import data

data.BANDS['Buckingham Nicks']={'Lindsey Buckingham': ['guitar', 'vocals']
                                'Stevie Nicks': ['vocals', 'tamborine']}

data.BANDS['Buckingham Nicks'].update(data.BANDS['Fleetwood Mac']
