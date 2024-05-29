nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
# s = ""
# for i in range(0,nat.find("Fast")):
#     s = s + nat[i]
# s = s + "Gigabit"
# for i in range(a+4,len(nat)):
#     s = s + nat[i]
print(nat.replace("Fast","Gigabit"))



mac = "AAAA:BBBB:CCCC"
print(mac.replace(":", "."))



s1 = []
s = ""
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
# for i in range(config.find("vlan")+5,len(config)):
#     s1 = s1 + config[i]
# result = s1.split(",")
# print(result)
for i in config:
    if i.isdigit():
        s = s + i
    elif s != "":
        s1.append(s)
        s = ""
s1.append(s)
print(s1)
