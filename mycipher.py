import sys
def caesar_cipher(message, shift):
  encoded_message = ''
  for char in message:
    if char.isalpha():
      char = char.upper()
      encoded_char = chr((ord(char) - 65 + shift) % 26 + 65)
      encoded_message += encoded_char
  return encoded_message

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 mycipher.py <shift_amount>")
    return

  shift_amount = int(sys.argv[1])

  for line in sys.stdin:
    message = line.strip()

  message = message.upper()
  encoded_message = ceaser_cipher(message, shift_amount)

  block_size = 5
  blocks_per_line = 10
  count = 0
  for char in encoded_message:
    if char.isalpha():
      if count % (block_size*blocks_per_line) == 0:
        print()
      elif count % block_size == 0:
        print(" ", end="")
      print(char, end="")
      count += 1
  print()
if __name__ == "__main__":
  main()