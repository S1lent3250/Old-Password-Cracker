import os, sys, crypt
from argparse import ArgumentParser
from colors import Normal as n, Bold as b, Symbols as s

"""
SAMPLE driver module for crack, the tiny module written using basic
Crypt functionality...This program should be familiar even if it is
modified a little.
"""
def salty_string(string):
	if len(string) is 0 or string is None:
		return
	else:
		s2 = crypt.crypt(string, "HX")

		print s.astk + n.ws + "String as salt (HX) is: " + n.ys + s2 + " - Len: ",len(s2),n.ce 
		pass


def test_pass(cPass, dict_file):
	salt = cPass[0:2]

	dictf = open(dict_file, 'r')

	# Iterate through the string lines 
	for word in dictf.readlines():
		word = word.strip('\n')
		cWord = crypt.crypt(word, salt)

		# If word matches the pass
		if cWord == cPass:
			print s.plus + b.wsb + "Found password: " + str(word) + b.ceb
			return
	print s.minus + n.ws + "Could not find password..." + n.ce
	pass

def main():
	parse = ArgumentParser(usage="crack.py -d <DICT> -p <PASS_FILE>", conflict_handler="resolve")
	parse.add_argument('-d', '--dict-file', type=str, dest="d_file", metavar='', default=None, help="The dictionary file to read (UNIX passwd)...")
	parse.add_argument('-p', '--pass-file', type=str, dest="p_file", metavar='', default=None, help="The password file with (*NIX) passwd...")
	parse.add_argument('-s', '--saltify', type=str, dest="c_salt", metavar='', default="Test", help="Return the string as salt \"HX\"...")

	args = parse.parse_args()

	if args.d_file:
		pFile = open(args.p_file)

		for line in pFile.readlines():
			if ":" in line:
				user = line.split(':')[0]  # Array Char Pos [0]

				cPass = line.split(':')[1].strip(' ')

				# Message indicator
				print s.astk + b.wsb + "Cracking password for: " + b.ysb + str(user) + b.ceb
				
				test_pass(cPass, args.d_file)
		return

	if args.c_salt:
		salty_string(args.c_salt)
		return



if __name__ == '__main__':
	main()
