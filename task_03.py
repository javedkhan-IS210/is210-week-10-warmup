#!/usr/bin/env python
# -*- coding: utf- -*-
""" Removing and adding keys to dictionaries"""

import data

CORRECTED = data.BANDS.copy()

CORRECTED['Dylan'] =  {'Bob Dylan': ['vocals', 'guitar', 'harmonica']}

del CORRECTED[ 'Van Halen']['David Lee Roth']

CORRECTED['Van Halen']['Sammy Hagar'] = ['Vocals']
