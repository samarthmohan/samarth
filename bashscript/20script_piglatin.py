def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split(' ')
  pigsent = ''
  pigword = ''
  for word in words:
    # Create the pig latin word and add it to the list
    pigword =  word [1:] + word[0] + 'ay' + ' '
    pigsent += pigword
    # Turn the list back into a phrase
  return pigsent

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
