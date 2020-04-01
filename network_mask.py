from sys import argv
net_mask = argv[1]
#net_mask = input('Введите сеть и маску: ')
net = net_mask[0:-3]
mask = net_mask[-2:]
octet1 = ((8 - len(str(bin(int(net.split('.')[0])))[2:])) * '0') + str(bin(int(net.split('.')[0])))[2:]
octet2 = ((8 - len(str(bin(int(net.split('.')[1])))[2:])) * '0') + str(bin(int(net.split('.')[1])))[2:]
octet3 = ((8 - len(str(bin(int(net.split('.')[2])))[2:])) * '0') + str(bin(int(net.split('.')[2])))[2:]
octet4 = ((8 - len(str(bin(int(net.split('.')[3])))[2:])) * '0') + str(bin(int(net.split('.')[3])))[2:]
bin_net = (octet1+octet2+octet3+octet4)
bin_net = bin_net[0:int(mask)] + (32 - int(mask)) * '0'
print('Network: ')
print("{:11}{:11}{:11}{:11}".format(str(int(bin_net[0:8],2)),str(int(bin_net[8:16],2)),str(int(bin_net[16:24],2)),str(int(bin_net[24:32],2))))
print("{:11}{:11}{:11}{:11}".format(bin_net[0:8],bin_net[8:16],bin_net[16:24],bin_net[24:32]))

print('')
print("Mask: ")
print(net_mask[-3:])
bin_mask = (int(mask) * "1") + ((32 - int(mask)) * "0")
print("{:11}{:11}{:11}{:11}".format(str(int(bin_mask[0:8],2)),str(int(bin_mask[8:16],2)),str(int(bin_mask[16:24],2)),str(int(bin_mask[24:32],2))))

print(bin_mask[0:8],'  ' + bin_mask[8:16],'  ' + bin_mask[16:24],'  ' + bin_mask[24:32])
