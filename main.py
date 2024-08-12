class ExitProgram(Exception):
  pass
# to get the input fromt the user and exit at anytime
def get_input(prompt):
  response = input(prompt + " (Press X to exit): ")
  if response.upper() == 'X':
      raise ExitProgram
  return response
#Make sure the email is a valid email
def email_attributes(prompt):
  while True:
      response = input(prompt + " (Email must have @, gmail.com, yahoo.com)")
      email_necessities = ['@', 'gmail.com', 'yahoo.com', 'dot.net']
      for char in email_necessities:
          if char in response:
              return response
      else:
          print("Invalid email. Must include @, gmail.com, yahoo.com or dot.net")

# The start of the program
def main():
  contact = {}
  contact_list = []

  try:

      while True:
          user_name = get_input("What is your name?")
          while True:
              user_phone_number = get_input("What is their number?")
              if len(user_phone_number) != 10:
                  print("Invalid phone number! Must be 10 digits!")
              else:
                  break
          user_email = email_attributes("What is their email?")

          contact[user_name] = user_phone_number, user_email
          contact_list.append(contact)


  except ExitProgram:
      pass

  print(contact)
  print(contact_list)

main()