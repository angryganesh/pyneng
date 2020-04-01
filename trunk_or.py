access_template = ['switchport mode access','switchport access vlan {}','switchport nonegotiate','spanning tree portfast','spanning-tree bpduguard enable']
trunk_template = ['switchport trunk encapsulation dot1q', 'switchport mode trunk','switchport trunk allowed vlan {}']
cfg = {'access':access_template, 'trunk':trunk_template}
question = {'access':'Введите номер VLAN','trunk':'Введите разрешенные VLANы'}
mode = input('Введите режим работы интерфейса(access/trunk): ')
inter = input('Введите тип и номер интерфейса: ')
vlans = input(question[mode] + ": ")
print('Interface {}'.format(inter))
cli = str(cfg[mode]).replace(', ', '\n').strip('[]').replace("'",'')
print(cli.format(vlans))
