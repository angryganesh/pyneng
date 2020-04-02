cfg = open('config_sw1.txt','r')
ignore = ['duplex','alias','Current configuration']
cfg_str = cfg.read().split('\n')
for stri in cfg_str:
	error1 = ''
	if stri == '':
		continue
	if stri[0] == '!':
		continue
	for ignore_st in ignore:
		if ignore_st in stri:
			error1 = 'error'
	if error1 == 'error':
		continue
	else:
		print(stri)
cfg.close()
