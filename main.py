from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("¡Bienvenidxs a la subasta secreta!")
bidders = {}
there_are_bidders = True
set_key = ""
set_value = 0
chosen_option = ""
invalid_option = True
while there_are_bidders:
  set_key = input("Escribe tu nombre: \n")
  set_value = int(input("Escribe cuánto deseas ofrecer: \n"))
  bidders[set_key] = set_value
  chosen_option = input("¿Aún hay quien ofrecerá para la subasta? Escribe 'si' o 'no'. \n")
  if chosen_option == "no":
    there_are_bidders = False
    invalid_option = False
  elif chosen_option == "si":
    clear()
  else:
    there_are_bidders = False

winner_name = ""
winner_bid = 0
if not invalid_option:
  for bidder in bidders:
    if bidders[bidder] > winner_bid:
      winner_bid = bidders[bidder]
      winner_name = bidder
  print(f"{winner_name} ganó la subasta al ofrecer MXN ${winner_bid}.")
else:
  print("Opción incorrecta. El programa se cerrará.")


  