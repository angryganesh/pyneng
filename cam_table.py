cam_input = open('/home/python/tools/first_repo/pyneng-examples-exercises/exercises/07_files/CAM_table.txt','r')
cam_dict = {}
for cam_input_str in cam_input.read().split('\n'):
	if len(cam_input_str.split()) > 3 and len(cam_input_str.split()[1].split('.')) == 3:
		cam_output_str = cam_input_str.split()
		cam_output_str.remove('DYNAMIC')
		cam_dict[int(cam_output_str[0])] = cam_output_str
print(cam_dict)
for keys in sorted(cam_dict):
	print('{:7} {:18} {:10}'.format(cam_dict[keys][0],
									cam_dict[keys][1],
									cam_dict[keys][2]))
#		print(cam_output_str)
cam_input.close()
		
