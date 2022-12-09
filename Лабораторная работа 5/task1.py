from pprint import pprint

val = [{"bin": bin(num), "dec": num, "hex": hex(num), "oct": oct(num)} for num in range(0, 16)]
pprint(val)
