def ConvertMinutesToSeconds(minutes):
    return minutes * 60
def ConvertSecondsToMinutes(seconds):
    return seconds / 60
def ConvertSecondsToHours(seconds):
    return seconds / 3600
def ConvertHoursToSeconds(hours):
    return hours * 3600
def ConvertHoursToMinutes(hours):
    return hours * 60
def ConvertMinutesToHours(minutes):
    return minutes / 60
def ConvertMinutesToDays(minutes):
    return minutes / 1440
def ConvertDaysToMinutes(days):
    return days * 1440
def ConvertDaysToHours(days):
    return days * 24
def ConvertHoursToDays(hours):
    return hours / 24
def ConvertDaysToSeconds(days):
    return days * 86400
def ConvertSecondsToDays(seconds):
    return seconds / 86400
def ConvertSecondsToHours(seconds):
    return seconds / 3600  # This is the same as ConvertHoursToSeconds


print("Convert Minutes to Seconds:", ConvertMinutesToSeconds(5))
print("Convert Seconds to Minutes:", ConvertSecondsToMinutes(300))
print("Convert Seconds to Hours:", ConvertSecondsToHours(3600))
print("Convert Hours to Seconds:", ConvertHoursToSeconds(2))
print("Convert Hours to Minutes:", ConvertHoursToMinutes(2))
print("Convert Minutes to Hours:", ConvertMinutesToHours(120))
print("Convert Minutes to Days:", ConvertMinutesToDays(1440))
print("Convert Days to Minutes:", ConvertDaysToMinutes(7))
print("Convert Days to Hours:", ConvertDaysToHours(7))
print("Convert Hours to Days:", ConvertHoursToDays(24))
print("Convert Days to Seconds:", ConvertDaysToSeconds(7))
print("Convert Seconds to Days:", ConvertSecondsToDays(86400))
print("Convert Seconds to Hours:", ConvertSecondsToHours(3600))


