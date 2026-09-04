def date_validation():
    date=input("Enter date(dd/mm/yy):")
    day,month,year=date.split('/')
    day=int(day)
    month=int(month)
    year=int(year)
    months=(
        "January",
        "February",
        "march",
        "April",
        "May",
        "June",
        "July",
        "Augst",
        "September",
        "October",
        "November",
        "December"
    )
    if month <1 or month>12 :
        print("invlaid date:")
    else:
        if month in(1,3,5,7,10,12):
            max_days=31
        elif month in(4,6,9,11):
            max_days=30
        else:
            if year %400==0 or (year %4==0 and year%100!=0):
                max_days=29
            else:
                max_days =28
        if day<1 or day>max_days:
            print("invalid date")
        else:
            print(f"{months[month-1]}, {day},{year}")
date_validation()
