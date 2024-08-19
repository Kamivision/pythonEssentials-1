hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
# find a total of all minutes
total_mins = mins + dura
# find a number of hours hidden in minutes and update the hour
hours = total_mins // 60
end_hour = (hour + hours) % 24
# correct minutes to fall in the (0..59) range
end_minutes = total_mins % 60
# correct hours to fall in the (0..23) range
print(end_hour, ":", end_minutes)

#Example Input = 23, 58, 642
#Example Output = 10 : 40