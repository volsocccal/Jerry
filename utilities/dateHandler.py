import datetime


def computeYearDuration(firstDate: datetime, secondDate: datetime) -> int:
    age = secondDate.year - firstDate.year
    if (secondDate.month < firstDate.month):
        if (secondDate.day < firstDate.day):
            age -= 1
    return age

def computeAge(birthDate: datetime) -> int:
    return computeYearDuration(birthDate, datetime.datetime.today())

def computeYearsOfService(startDate: datetime) -> int:
    return computeYearDuration(startDate, datetime.datetime.today())

