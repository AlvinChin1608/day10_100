# Function with Output

def format_name(f_name, l_name):
  """Take a first and last and format it
  to return the title case version of the time"""
  if f_name == "" or l_name =="":
    return "You did not provide a valid input "#this terminate the function early
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}" #the return tell the computer this is the end of the function
  print("This got printed") # and this never get executed 
  # print(f"{formated_f_name} {formated_l_name}")

# formated_string = format_name("alvin", "ALVIN")
# print(formated_string)

print(format_name(input("what is your first name "), input("What is your last name ")))

# Exercise Challenge - create a leap year 
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True      
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month - 1]

year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

# Another note for return 
"""
def outer_function(a, b):
  def inner_function(c, d):
      return c + d
  return inner_function(a, b)

result = outer_function(5, 10)
print(result)

output = 15
"""