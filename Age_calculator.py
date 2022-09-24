# defining function to calculate age
def dob(y, m, d):
    
    import datetime
    
    today= datetime.datetime.now().date()
    birth_date= datetime.date(y, m, d)
    
    # formula to calculate age
    age= int((today-birth_date).days / 365.25)
    
    print(f'Your age is {age}')

# driver code 
if __name__ == "__main__":
    print("Enter DOB in format \n")
    date= int(input("date: "))
    month= int(input("month: "))
    year= int(input("year: "))
    
    # calling the function
    dob(year, month, date)
