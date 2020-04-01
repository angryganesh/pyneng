access_template = [
	'switchport mode access','switchport access vlan',
	'spanning-tree portfast','spanning-tree bpduguard enable'
	]
trunk_template = [
	'switchport trunk encapsulation dot1q','switchport mode trunk',
	'switchport trunk allowed vlan'
	]
access = {
	'0/12':'10',
	'0/14':'11',
	'0/16':'17',
	'0/17':'150'
	}
trunk = {
	'0/1':['add','10','20','100'],
	'0/2':['only','11','30'],
	'0/4':['del','17']
	}
for intf,vlan in access.items():
	print('interface FastEthernet' + intf)
	for command in access_template:
		if command.endswith('access vlan'):
			print(' {} {}'.format(command,vlan))
		else:
			print(' {}'.format(command))
for intf,cmd in trunk.items():
	print ('interface FastEthernet' + intf)
	for command in trunk_template:
		if command.endswith('allowed vlan'):
			vl = 1
			vls = ''
			if cmd[0] == 'add':
				while vl > 0 and vl < (len(cmd)):
					vls = vls + cmd[vl] + ','
					vl += 1
				print(' {} {} {}'.format(command,'add',vls.strip(',')))
				vls = ''
			elif cmd[0] == 'only':
				while vl > 0 and vl < (len(cmd)):
					vls = vls + cmd[vl] + ','
					vl += 1
				
				print(' {} {}'.format(command,vls.strip(',')))
				vls = ''
			elif cmd[0] == 'del':
				while vl > 0 and vl < (len(cmd)):
					vls = vls + cmd[vl] + ','
					vl += 1
				print(' {} {} {}'.format(command,'remove',vls.strip(',')))
				vls = ''
		else:
			print(' {}'.format(command))
			
