

if __name__ == '__main__':
	from xbox.generator_main import regenerate
	try:
		regenerate()
	except Exception as e:
		print(type(e), str(e))
	# regenerate()
	import os
	os.system('pause')
	