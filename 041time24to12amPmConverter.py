#https://en.wikipedia.org/wiki/12-hour_clock
#"a.m." and "p.m." are abbreviations of the Latin ante meridiem (before midday) and post meridiem (after midday
#example calculator and table can be found at - https://www.timecalculator.net/12-hour-to-24-hour-converter
# in 12AmPm format 12 is acting as zero
#0 o'clock and 12 o'clock in 24 format are exceptions and shown as 12am for 0 hour, and 12pm for 12 hour (midday)

def timeConverter24toAmPm(time):
    splTime = time.split(":")
    hours, minutes = int(splTime[0]), int(splTime[1])

    if hours == 12:
        return f'12:{minutes:02} p.m.'
    if hours > 12:
        return f'{hours-12}:{minutes:02} p.m.'
    if hours == 0:
        return f'12:{minutes:02} a.m.'
    return f'{hours}:{minutes:02} a.m.'    
    return time

if __name__ == '__main__':
    print(timeConverter24toAmPm('12:30'))
    assert timeConverter24toAmPm('12:30') == '12:30 p.m.'
    
    print(timeConverter24toAmPm('09:00'))
    assert timeConverter24toAmPm('09:00') == '9:00 a.m.'
    
    print(timeConverter24toAmPm('23:30'))
    assert timeConverter24toAmPm('23:30') == '11:30 p.m.'
    
    print(timeConverter24toAmPm('00:15'))
    assert timeConverter24toAmPm('00:15') == '12:15 a.m.'
