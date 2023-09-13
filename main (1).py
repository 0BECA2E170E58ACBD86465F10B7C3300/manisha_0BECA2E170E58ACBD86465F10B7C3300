#leep year

"""
year % 4 == 0 &
year % 100 !=0/
year % 400 ==
"""
def isLeepYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
     return False
      
year = 2013

if isLeepYear(year):
    print('{} is a leap year .'.formate(year))
else:
    print('{} is a not a leep year.'.format(year))
