#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > Convert US date to EU date"""

usdate = input()

months = ('months', 'January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')

if ',' in usdate or ' ' in usdate:
    usdate = usdate.replace(',', '')
    usdate = usdate.replace(' ', '/')
    month = usdate.split('/')[0]
    usdate = usdate.replace(month, str(months.index(month)))
    
mm, dd, yyyy = usdate.split('/')
eudate = '{}/{}/{}'.format(dd, mm, yyyy)
print(eudate)
