from my_idea import *
from cryptocommon import *

chave = list(range(16))

def str_to_bytelist(mensagem):
	t = len(mensagem)
	b , r = (t >> 3) , (t & 7)
	ans = []
	for i in range(b):
		ans.append(asciistr_to_bytelist(mensagem[(i << 3):(i + 1) << 3]))
	ans.append(asciistr_to_bytelist(mensagem[-r:]+' '*(8-r)))
	return ans

def bytelist_to_str(blocks):
	ans = ''
	for block in blocks:
		ans += ''.join([chr(number) for number in block])
	return ans

def code(blocks, chave):
	ans = []
	for block in blocks:
		ans.append(encrypt(block, chave))
	return ans

def decode(blocks, chave):
	ans = []
	for block in blocks:
		ans.append(decrypt(block, chave))
	return ans

def get_encryp_message(message, chave):
	bytelist = str_to_bytelist(message)
	message_coded = code(bytelist, chave)
	return message_coded

def get_decryp_message(message, chave):
	bytelist_decoded = decode(message, chave)

	message_decoded = bytelist_to_str(bytelist_decoded)
	return message_decoded

