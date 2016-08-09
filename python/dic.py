#!/usr/bin/env python3
# -*- coding:utf-8 -*-

d = {'Michael':95, 'Bob':75, 'Tracy':85}
print(d['Michael'])

d['Adam'] = 67
print(d['Adam'])

print('Tomas in d', 'Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas', -1))

print(d.pop('Bob'))
