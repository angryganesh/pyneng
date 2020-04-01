mac = ['aabb:ccdd:7000','aabb:dd80:7340','aabb:ee80:7000','aabb:ff80:7000']
mac_cisco =[]
for wr_mac in mac:
    mac_cisco.append(wr_mac.replace(':','.'))
print(mac_cisco)
