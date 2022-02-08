import sys
# 입력
n = int(sys.stdin.readline()) # ip 갯수

ip_address = [list(map(int, sys.stdin.readline().strip().split('.'))) for _ in range(n)] # ip 주소

net_address = [] # 네트워크 주소
net_mask = [] # 네트워크 마스크

for i in range(4):
  max_ip = ip_address[0][i]
  min_ip = ip_address[0][i]
  for ip in ip_address:
    if max_ip < ip[i]:
      max_ip = ip[i]
    if min_ip > ip[i]:
      min_ip = ip[i]
  if max_ip == min_ip:
    net_mask.append(255)
  else:
    part = ''
    max_ip_part = format(max_ip, 'b')
    min_ip_part = format(min_ip, 'b')
    if len(max_ip_part) < 8:
      for _ in range(8 - len(max_ip_part)):
        max_ip_part = '0' + max_ip_part    
    if len(min_ip_part) < 8:  
      for _ in range(8 - len(min_ip_part)):
        min_ip_part = '0' + min_ip_part
    for j in range(8):
      if max_ip_part[j] == min_ip_part[j]:
        part += '1'
      else:
        for k in range(8 - j):
          part += '0'
        break
    net_mask.append(int(part, 2))
    for k in range(3):
      net_mask.append(0)
    break


for i in range(4):
  net_address.append(ip_address[0][i] & net_mask[i])

print("{}.{}.{}.{}".format(net_address[0], net_address[1], net_address[2], net_address[3])) 
print("{}.{}.{}.{}".format(net_mask[0], net_mask[1], net_mask[2], net_mask[3]))
