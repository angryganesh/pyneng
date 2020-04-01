ip = input('Enter ip address: ')
error = False
while True:
	octets = ip.split('.')
	if len(octets) != 4:
		print('Октетов больше четырёх!')
		ip = input('Введите ещё раз: ')
		continue
	for octet in octets:
		if int(octet) < 0 or int(octet) > 255:
			error = True
			break
	if error:
		print ('Октет в неверном диапазоне!')
		ip = input('Введите ещё раз: ')
		error = False
		continue
	if int(octets[0]) > 0 and  int(octets[0]) < 224:
		print('unicast')
		break
	elif int(octets[0]) > 223 and  int(octets[0]) < 240:
		print('multicast')
		break
	elif ip == '0.0.0.0':
		print('unassigned')
		break
	elif ip == '255.255.255.255':
		print('local broadcast')
		break
	else:
		print('unused')
		break
	
