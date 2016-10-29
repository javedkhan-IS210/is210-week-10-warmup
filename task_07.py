#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A dictionary and a function """

DATA = {
    456: 456789,
    124: 151151,
    156: 564999,
    315: 516161,
    867: 530915,
    152: 651566,
    161: 616665,
    619: 365616,
    696: 515141,
    545: 154151}

def iter_dict_funky_sum(FUNKYDICT):
    """ A function that makes one argument, exracts a pair and adds it

        Args:
             FUNKYDICT(dictionary): a dictionary with integer keys & values.

        Returns:
             The funky total

        Examples:
             >>> import task_07
             >>> task_07.iter_dict_funky_sum(task_07.DATA)
             140166242

    """
    total = 1
    for key, value in FUNKYDICT.iteritems():
        total += value - key
    return total
