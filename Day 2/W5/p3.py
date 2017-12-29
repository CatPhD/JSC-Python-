def weeklySalary(hoursWorked, hourlyRate):
    salary = 0
    if hoursWorked <= 40:
        salary = hoursWorked*hourlyRate
    else:
        salary = 40 * hourlyRate + (hoursWorked-40)*1.5*hourlyRate
    return format(salary, '.0f')

print('10 Hours worked($9/Hour): $', weeklySalary(10, 9), sep='')
print('50 Hours worked($10/Hour): $', weeklySalary(50, 10), sep='')
