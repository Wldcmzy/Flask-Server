

if __name__ == '__main__':
	import time
	T = time.time()
	def R():
		t = time.time() - T
		t = int(t)
		print(f'{t // 3600} H  {(t % 3600) // 60} M  {t % 60} S')
	from xbox.generator_main import regenerate
	# try:
	# 	regenerate()
	# except Exception as e:
	# 	print(type(e), str(e))
	regenerate()
	R()
	import os
	os.system('pause')
	