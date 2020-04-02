strings = ['Protocol:','Prefix:','AD/Metric:','Next-Hop:','Last update:','Outbound Interface:']
ospf_in = open('ospf.txt','r')
ospf_data = ospf_in.read().strip().split()
ospf_data.remove('via')
ospf_data[0] = ospf_data[0].replace('O','OSPF')
ospf_data[2] = ospf_data[2].strip('[]')
table_len = 0
while table_len < 6:
	print('{:20} {:20}'.format(strings[table_len], ospf_data[table_len]))
	table_len += 1
ospf_in .close()
