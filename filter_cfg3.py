from sys import argv
file_in = argv[1]
file_out = argv[2]
cfg = open(file_in,'r')
cfg_out = open(file_out,'w')
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
		cfg_out.write(stri)
		cfg_out.write('\n')
cfg.close()
cfg_out.close()
