FLAG = "uctftheweakestencryption"
FILENAME = "encrypted"

f = open(FILENAME, "w")

for letter in FLAG:
  f.write("0" * (ord(letter) - ord('a')) + "1")
  print(ord(letter) - ord("a") + 1)

f.write('\n')
f.close()
  