red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"
print ("Do you want to see something cool? Type Yes or No below!")
ans = input ()
if ans == 'Yes':
  print (magenta, "This is magenta text")
  print (red, "This is red text")
  print (green, "This is green text")
  print ( yellow, "This is yellow text")
  print (blue, "This is blue text")
  print (cyan, "This is cyan text")
  print (white, "This is white text")
  print (bright_black, "This is bright black text")
  print (bright_red, "This is bright red text")
  print (bright_green, "This is bright green text")
     print ( bright_yellow, "This is bright yellow text")
  print ( bright_blue, "This is bright blue text")
  print ( bright_magenta, "This is bright magenta text")
  print (bright_cyan, "This is bright cyan text")
  print (bright_white, "Wasn't that cool?")
elif ans == 'No':
  print ("Oh, well. Your loss.")
else:
  print ("What was that again? remember to only type Yes or No with the Y in Yes uppercase and/or the N in No uppercase. Do not type any word other than Yes or No. You'll have to restart this repl.")