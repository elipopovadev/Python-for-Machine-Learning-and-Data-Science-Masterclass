import pandas as pd


date = '10-Dec-2022'
date_format = pd.to_datetime(date, format='%d-%b-%Y')
print(date_format.year)
print(date_format.day_name())

'''
%Y  Full year with century  2021,2022
%y  Year without century with zero padded value 00,01,….21,22…,99
%-y Year without century    0,1…,99
%m  Month with zero padded value    01-12
%-m Month without zero padded value 1-12
%B  Full month name January, February,…, December
%b  Short form of month     Jan, Feb,…,Dec
%A  Full weekday name   Sunday, Monday,..
%a  Short form of weekday name  Sun, Mon,..
%w  Weekday as decimal value    0-6
%d  Days with zero padded value 01-31
%-d Days with decimal value 1-31
%H  Hour (24-hour clock) as a zero-padded value.    00-23
%-H Hour (24-hour clock) without zero-padded value. 0,1,…,23
%I  Hour (12-hour clock) as a zero-padded value.    01-12
%-I Hour (12-hour clock) without zero-padded value. 1-12
%M  Mins with zero-padded   00-59
%-M Mins without zero padded value  0-59
%S  Secs with zero padded value 00-59
%-S Secs without zero padded value  0-59
%f  Micro Secs with zero-padded value   000000 – 999999
%p  Locale’s AM or PM.    AM/PM
%j  Day of the year with zero padded value  001-366
%-j Day of the year without zero padded value   1-366
%z  UTC offset in the form +HHMM or -HHMM.   
%Z  Time zone name.  
%C  Locale’s appropriate date and time    Fri Apr 02 02:09:07 2020
%x  Locale’s appropriate date 02/04/22
%X  Locale’s appropriate time 02:04:22
%W  Week number of the year. Monday as first day of week    00-53
%U  Week number of the year. Sunday as first day of week    00-53 '''
