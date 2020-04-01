device = input('Введи имя устройства: ')
london_co = {
    'r1': {
           'location': '21 New Globe Walk',
           'vendor': 'Cisco',
           'model': '4451',
		   'ios': '15.4',
		   'ip': '10.255.0.1'
	},
	'r2': {
	       'location': '21 New Globe Walk',
           'vendor': 'Cisco',
           'model': '4451',
		   'ios': '15.4',
		   'ip': '10.255.0.2'
	},
	'sw1': {
           'location': '21 New Globe Walk',
           'vendor': 'Cisco',
           'model': '3850',
		   'ios': '3.6.XE',
		   'ip': '10.255.0.101',
		   'vlans': '10,20,30',
		   'routing': True
	}
}
params = str(sorted(london_co[device])).replace('[','').replace(']','').replace("'",'')
key = ('Введи параметр(') + params + ('): ')
param = str(input(key)).lower()
print(london_co[device].get(param,'Нет такого параметра'))
