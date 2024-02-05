

if __name__ == '__main__':
	# print('after if name == main')
	from xbox.generator_main import regenerate
	# print('after import')
	try:
		# print('before regenerate')
		regenerate()
		# print('after regenerate')
	except Exception as e:
		print(type(e), str(e))
	# regenerate()
	import os
	os.system('pause')
	