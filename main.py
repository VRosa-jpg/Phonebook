class ExitProgram(Exception):
  pass

#This is for getting th response from the user
def get_input(prompt):
  #The variable for recieving th repsonse
  response = input(prompt + " (Press X to exit): ")
  # If the user presses x we outta here
  if response.upper() == 'X':
      raise ExitProgram
  return response

def main():
  contact = {}
  contact_list = []

  try:

      while True:
          user_name = get_input("What is your name?")
          user_phone_number = get_input("What is their number?")
          user_email = get_input("What is their email?")

          contact[user_name] = user_phone_number, user_email
          contact_list.append(contact)


  except ExitProgram:
      pass

  print(contact)
  print(contact_list)

main()