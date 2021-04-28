months = {
    1: {"name":"Jan", "end":31},
    2: {"name":"Feb", "end":28},
    3: {"name":"Mar", "end":31},
    4: {"name":"Apr", "end":30},
    5: {"name":"May", "end":31},
    6: {"name":"June", "end":30},
    7: {"name":"Jul", "end":31},
    8: {"name":"Aug", "end":31},
    9: {"name":"Sep", "end":30},
    10: {"name":"Oct", "end":31},
    11: {"name":"Nov", "end":30},
    12: {"name":"Dec", "end":31},
}
from datetime import datetime

def str_to_float(num_str):
    try:
        nums = num_str.split(",")
        if len(nums) == 2:
            val = float("".join(nums))
        else:
            val = float(num_str)
        return val
    except Exception as e:
        return "No"
        print(e)
        
def formatStarter(day):
    if day < 10:
        return "0" + str(day)
    return str(day)

def set_end_intevals(starter, endPos, date, month_number):
    
    if date.day < endPos and date.month == month_number:
        #return formatStarter(starter) + " - " + str(endPos) + " " + months[month_number]["name"] + " " + str(date.year)
        return datetime(date.year, date.month, endPos).date()
    elif date.day > endPos and date.month == month_number:
         return datetime(date.year, date.month, endPos+1).date()
        
#return formatStarter(endPos+1) + " - " + str(months[month_number]["end"]) + " "+ months[month_number]["name"] + " " + str(date.year)
    

def rename_intervals(starter, endPos, date, month_number):
    if date.day == endPos and date.month == month_number:
        return formatStarter(starter) + " - " + str(endPos) + " " + months[month_number]["name"] + " " + str(date.year)
    elif date.day > endPos and date.month == month_number:
        return formatStarter(endPos+1) + " - " + str(months[month_number]["end"]) + " "+ months[month_number]["name"] + " " + str(date.year)
    
    
    
    
    
    
    
    
    