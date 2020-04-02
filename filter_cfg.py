cfg = open('config_sw1.txt','r')
cfg_str = cfg.read().split('\n')
for stri in cfg_str:
	if stri == '':
		continue
	if stri[0] == '!':
		continue
	else:
		print(stri)
cfg.close()
