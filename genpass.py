#!/usr/bin/env python3
import string
import random
import sys
import getopt

def displayhelp():
	mess = '''Personal Password generator using Python 3
version: 1.0
by: r0s3l

Options:
	-l , length of password
	-s , your character list
	-h , print this help

Default, 
	The script will provide a 12 characters password.
'''
	print(mess)

def main():
	length = 12
	cdb = ""
	special = '-!#$%&()*,./:;?@[]^_{|}~+<=>'
	cdb += string.ascii_letters
	cdb += string.digits
	cdb += special
	out = []
	out.append(random.choice(string.ascii_letters))

	argv = sys.argv[1:]
	try: 
		opts, args = getopt.getopt(argv, "s:l:h")   
	except: 
		print("Error") 
	for opt, arg in opts: 
		if opt in ['-s']: 
			cdb = arg
		elif opt in ['-l']: 
			length = int(arg)
		else:
			displayhelp()
			exit(0)
				
	for i in range(length-1):
		temp = random.choice(cdb)
		out.append(temp)
		
	print("".join(out))


if __name__ == "__main__":
    main()