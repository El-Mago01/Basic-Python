def convert_to_GMT4(time_string):
    hours = int(time_string[0:2])+4
    if hours >= 24:
        hours=hours-24
    return f"{hours:02}:{time_string[3:5]}"

print(convert_to_GMT4("10:00"))
print(convert_to_GMT4("20:59"))
print(convert_to_GMT4("23:59"))
