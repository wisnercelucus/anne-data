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
    
    
    
def lag_finder(temperature_list, arvi_list, sr):
    import numpy as np
    from scipy import signal
    import matplotlib.pyplot as plt
    
    n = len(temperature_list)

    corr = signal.correlate(arvi_list, temperature_list, mode='same') / np.sqrt(signal.correlate(temperature_list, temperature_list, mode='same')[int(n/2)] * signal.correlate(arvi_list, arvi_list, mode='same')[int(n/2)])

    delay_arr = np.linspace(-0.5*n/sr, 0.5*n/sr, n)
    delay = delay_arr[np.argmax(corr)]
    print('arvi_list is ' + str(delay) + ' behind temperature_list')

    plt.figure()
    plt.plot(delay_arr, corr)
    plt.title('Lag: ' + str(np.round(delay, 3)) + ' s')
    plt.xlabel('Lag')
    plt.ylabel('Correlation coefficient')
    plt.show()
    
    
    
    
    