switch_ip_mask = "0"
mgmt_ip = "0"
switch_default_gateway = "0"
ISP_Connection = "dhcp"
ip_address = "0"
hostname_old = "hostname XXX-XXX-XXX-XXX"
snmp_details_old = 'snmp-server location "Site Name: , Project ID: , Address: "'
hostnamesw = "sw01"
swipold = "ip address xx.xx.xx.xx xx.xx.xx.xx"
swgaold = "ip default-gateway xx.xx.xx.xx"

# this function creates the wildcard and subnet mask
def create_mask():
    subnet = int(input("enter subnet size(24, 27 etc): "))
    subnetbin = "00000000000000000000000000000000"
    subnetbin = subnetbin[:subnet].replace("0", "1") + subnetbin[subnet:]
    subnetbin = subnetbin[:8] + "." + subnetbin[8:]
    subnetbin = subnetbin[:17] + "." + subnetbin[17:]
    subnetbin = subnetbin[:26] + "." + subnetbin[26:]
    subnetcalc = (subnetbin.split("."))
    subnetmask = str(int(subnetcalc[0], 2)) + "." + str(int(subnetcalc[1], 2)) + "." + str(int(subnetcalc[2], 2)) + "." + str(int(subnetcalc[3], 2))
    wildcardcalc = (subnetmask.split("."))
    wildcard = str(255-int(wildcardcalc[0])) + "." + str(255-int(wildcardcalc[1])) + "." + str(255-int(wildcardcalc[2])) + "." + str(255-int(wildcardcalc[3]))
    return subnetmask, wildcard


# to create mask, do following: mask_vlan10, wildcardvlan10 = create_mask()
def create_rtrip():
    # this function creates the router IP#
    rtriplast = int(ip_address[-1])
    rtriplast = rtriplast + 1
    swiplast = rtriplast + 1
    ip_address_rest = len(ip_address)
    rtrip = ip_address[:ip_address_rest - 1] + str(rtriplast)
    return rtrip

def create_swip():
    # this function creates the router IP#
    rtriplast = int(ip_address[-1])
    rtriplast = rtriplast + 1
    swiplast = rtriplast + 1
    ip_address_rest = len(ip_address)
    swip = ip_address[:ip_address_rest - 1] + str(swiplast)
    return swip

#creates the needed L3 details
def create_rtripL3():
    # this function creates the router IP#
    rtriplast = int(ip_address[-1])
    rtriplast = rtriplast + 1
    ip_address_rest = len(ip_address)
    l3ip = ip_address[:ip_address_rest - 1] + str(rtriplast)
    rtriplast = int(ip_address[-1])
    rtriplast = rtriplast + 2
    ip_address_rest = len(ip_address)
    rtrip = ip_address[:ip_address_rest - 1] + str(rtriplast)
    return rtrip, l3ip

# writes the ip address for vlan to config file
def write_rtr_ip():
    fout = open("RTR Config.txt", "rt")
    data = fout.read()
    data = data.replace(rtr_ip_mask_old, rtr_ip_mask)
    fout.close()
    fout2 = open("RTR Config.txt", "wt")
    fout2.write(data)
    fout2.close()


def write_sw_ip():
    fout = open("Switch Config.txt", "rt")
    data = fout.read()
    data = data.replace(swipold, swipmgmt)
    swga = "ip default-gateway " + rtripvlan10
    data = data.replace(swgaold, swga)
    fout.close()
    fout2 = open("Switch Config.txt", "wt")
    fout2.write(data)
    fout2.close()
    print("Switch config created")

# writes the access lists
def write_subnet_wildcard():
    fout2 = open("RTR Config.txt", "rt")
    data = fout2.read()
    data = data.replace(old_wildcard, subnet_wildcard)
    fout2.close()
    fout2 = open("RTR Config.txt", "wt")
    fout2.write(data)
    fout2.close()

#writes router L3 details
def write_L3():
    fout2 = open("RTR Config.txt", "rt")
    data = fout2.read()
    data = data.replace(rtr_ip_mask_old, rtr_ip_mask)
    data = data.replace(l3_ip_old, l3_ip_corp)
    fout2.close()
    fout2 = open("RTR Config.txt", "wt")
    fout2.write(data)
    fout2.close()

# writes the hostname
def write_hostname():
    hostname = input("enter the hostname (eg: VDE-Gjerdrumsvei10-12345-RTR): ")
    hostname = "hostname" + " " + hostname
    fout2 = open("RTR Config.txt", "rt")
    data = fout2.read()
    data = data.replace(hostname_old, hostname)
    fout2.close()
    fout2 = open("RTR Config.txt", "wt")
    fout2.write(data)
    fout2.close()
    hostnamesw = len(hostname)
    hostnamesw = hostname[:hostnamesw - 3] + "SW01"
    hostnamesw = hostnamesw
    fout2 = open("Switch Config.txt", "rt")
    data = fout2.read()
    data = data.replace(hostname_old, hostnamesw)
    fout2.close()
    fout2 = open("Switch Config.txt", "wt")
    fout2.write(data)
    fout2.close()
    print(hostname + " written!")

#writes the SNMP details
def write_snmp_details():
    snmp_details1 = input("enter the sitename: ")
    snmp_details1 = "Site Name: " + snmp_details1
    snmp_details_final = snmp_details_old.replace('Site Name: ', snmp_details1)
    snmp_details1 = input("enter the project number: ")
    snmp_details1 = "Project ID: " + snmp_details1
    snmp_details_final = snmp_details_final.replace('Project ID:', snmp_details1)
    snmp_details1 = input("enter the Project Address (eg. Skabos Vei 4, 0278 Skøyen) : ")
    snmp_details1 = "Address: " + snmp_details1
    snmp_details_final = snmp_details_final.replace('Address:', snmp_details1)
    fout = open("RTR Config.txt", "rt")
    data = fout.read()
    data = data.replace(snmp_details_old, snmp_details_final)
    fout.close()
    fout = open("RTR Config.txt", "wt")
    fout.write(data)
    fout.close()
    fout = open("Switch Config.txt", "rt")
    data = fout.read()
    data = data.replace(snmp_details_old, snmp_details_final)
    fout.close()
    fout = open("Switch Config.txt", "wt")
    fout.write(data)
    fout.close()
    print("SNMP data replaced")


# checks for connection type and copies a clean version of corresponding config to rtr confit.txt
connection_type = input("enter the connection type (VPN or MPLS): ")
# some general input correction
if connection_type == "vpn":
    connection_type = "VPN"
if connection_type == "mpls":
    connection_type = "MPLS"
# adding the correct clean config to "RTR Config.txt" and "Switch Config.txt"
if connection_type == "VPN":
    clean = open("Clean - VPN Config.txt", "rt")
    clean2 = clean.read()  # reads the config to variable "clean2"
    clean.close()
    clean = open("RTR Config.txt", "wt")
    clean.write(clean2)  # writes the text from clean2 to VPN config
    clean.close()
    clean = open("Clean - Switch VPN.txt", "rt")
    clean2 = clean.read()  # reads the config to variable "clean2"
    clean.close()
    clean = open("Switch Config.txt", "wt")
    clean.write(clean2)  # writes the text from clean2 to mpls config
    clean.close()
if connection_type == "MPLS":
    clean = open("Clean - MPLS Config.txt", "rt")
    clean2 = clean.read()  # reads the config to variable "clean2"
    clean.close()
    clean = open("RTR Config.txt", "wt")
    clean.write(clean2)  # writes the text from clean2 to mpls config
    clean.close()
    clean = open("Clean - Switch MPLS.txt", "rt")
    clean2 = clean.read()  # reads the config to variable "clean2"
    clean.close()
    clean = open("Switch Config.txt", "wt")
    clean.write(clean2)  # writes the text from clean2 to mpls config
    clean.close()
write_hostname()
write_snmp_details()

'''''
# if there are more vlans to be added, copy and paste one of the ones below.
# some changes will be needed if the IP addresses are different for vendor network beetween VPN and MPLS
# vlan 10 has some additional stuff to create config for Switch 1
'''''

# creates variables for vlan 10 and writes them to config file
ip_address = input("enter the subnet address for vlan 10: ")
if connection_type == "VPN":
    rtr_ip_mask_old = "10.106.x.x 255.255.x.x"
    old_wildcard = "10.106.x.x 0.0.x.x"
elif connection_type == "MPLS":
    rtr_ip_mask_old = "10.101.x.x 255.255.x.x"
    old_wildcard = "10.101.x.x 0.0.x.x"
subnet_vlan10 = ip_address
rtripvlan10 = create_rtrip()
swipmgmt = create_swip()
mask_vlan10, wildcard_vlan10 = create_mask()
rtr_ip_mask = rtripvlan10 + " " + mask_vlan10
swipmgmt = swipmgmt + " " + mask_vlan10
subnet_wildcard = subnet_vlan10 + " " + wildcard_vlan10
switch_default_gateway = rtripvlan10
write_rtr_ip()
write_sw_ip()
write_subnet_wildcard()


# creates variables for vlan 11 and writes them to config file
ip_address = input("enter the subnet address for vlan 11: ")
if connection_type == "VPN":
    rtr_ip_mask_old = "10.107.x.x 255.255.x.x"
    old_wildcard = "10.107.x.x 0.0.x.x"
if connection_type == "MPLS":
    rtr_ip_mask_old = "10.102.x.x 255.255.x.x"
    old_wildcard = "10.102.x.x 0.0.x.x"
subnet_vlan11 = ip_address
rtripvlan11 = create_rtrip()
mask_vlan11, wildcard_vlan11 = create_mask()
rtr_ip_mask = rtripvlan11 + " " + mask_vlan11
subnet_wildcard = subnet_vlan11 + " " + wildcard_vlan11
write_rtr_ip()
write_subnet_wildcard()

# creates variables for vlan 12 and writes them to config file
ip_address = input("enter the subnet address for vlan 12: ")
if connection_type == "VPN":
    rtr_ip_mask_old = "10.108.x.x 255.255.x.x"
    old_wildcard = "10.108.x.x 0.0.x.x"
if connection_type == "MPLS":
    rtr_ip_mask_old = "10.104.x.x 255.255.x.x"
    old_wildcard = "10.104.x.x 0.0.x.x"
subnet_vlan12 = ip_address
rtripvlan12 = create_rtrip()
mask_vlan12, wildcard_vlan12 = create_mask()
rtr_ip_mask = rtripvlan12 + " " + mask_vlan12
subnet_wildcard = subnet_vlan12 + " " + wildcard_vlan12
write_rtr_ip()
write_subnet_wildcard()

# creates variables for vlan 13 and writes them to config file
ip_address = input("enter the subnet address for vlan 13: ")
if connection_type == "VPN":
    rtr_ip_mask_old = "10.109.x.x 255.255.x.x"
    old_wildcard = "10.109.x.x 0.0.x.x"
if connection_type == "MPLS":
    rtr_ip_mask_old = "10.100.x.x 255.255.x.x"
    old_wildcard = "10.100.x.x 0.0.x.x"
subnet_vlan13 = ip_address
rtripvlan13 = create_rtrip()
mask_vlan13, wildcard_vlan13 = create_mask()
rtr_ip_mask = rtripvlan13 + " " + mask_vlan13
subnet_wildcard = subnet_vlan13 + " " + wildcard_vlan13
write_rtr_ip()
write_subnet_wildcard()

# creates variables for vlan 14 and writes them to config file
ip_address = input("enter the subnet address for vlan 14: ")
if connection_type == "VPN":
    rtr_ip_mask_old = "10.110.x.x 255.255.x.x"
    old_wildcard = "10.110.x.x 0.0.x.x"
if connection_type == "MPLS":
    rtr_ip_mask_old = "10.103.x.x 255.255.x.x"
    old_wildcard = "10.103.x.x 0.0.x.x"
subnet_vlan14 = ip_address
rtripvlan14 = create_rtrip()
mask_vlan14, wildcard_vlan14 = create_mask()
rtr_ip_mask = rtripvlan14 + " " + mask_vlan14
subnet_wildcard = subnet_vlan11 + " " + wildcard_vlan11
write_rtr_ip()
write_subnet_wildcard()

# creates variables for vlan 120 and writes them to config file
ip_address = input("enter the subnet address for vlan 120: ")
rtr_ip_mask_old = "10.120.x.x 255.255.x.x"
old_wildcard = "10.120.x.x 0.0.x.x"
subnet_vlan120 = ip_address
rtripvlan120 = create_rtrip()
mask_vlan120, wildcard_vlan120 = create_mask()
rtr_ip_mask = rtripvlan120 + " " + mask_vlan120
subnet_wildcard = subnet_vlan120 + " " + wildcard_vlan120
write_rtr_ip()
write_subnet_wildcard()

# creates variables for vlan 123 and writes them to config file
ip_address = input("enter the subnet address for vlan 123: ")
rtr_ip_mask_old = "10.123.x.x 255.255.x.x"
old_wildcard = "10.123.x.x 0.0.x.x"
subnet_vlan123 = ip_address
rtripvlan123 = create_rtrip()
mask_vlan123, wildcard_vlan123 = create_mask()
rtr_ip_mask = rtripvlan123 + " " + mask_vlan123
subnet_wildcard = subnet_vlan120 + " " + wildcard_vlan120
write_rtr_ip()
write_subnet_wildcard()


# this checks for MPLS connection and takes the remaining vlan/ L3 details
if connection_type == "MPLS":

    ip_address = input("enter the subnet address for CORP L3: ")
    rtr_ip_mask_old = "10.105.x.x 255.255.255.248 -corpl3rtr"
    l3_ip_old = "10.105.x.x -corpl3"
    subnet_CorpL3 = ip_address
    rtripCorpL3, l3_ip_corp = create_rtripL3()
    mask_CorpL3, wildcard_CorpL3 = create_mask()
    rtr_ip_mask = rtripCorpL3 + " " + mask_CorpL3
    write_L3()

    ip_address = input("enter the subnet address for Guest L3: ")
    rtr_ip_mask_old = "10.105.x.x 255.255.255.248 -guestl3rtr"
    l3_ip_old = "10.105.x.x -guestl3"
    subnet_CorpL3 = ip_address
    rtripCorpL3, l3_ip_corp = create_rtripL3()
    mask_CorpL3, wildcard_CorpL3 = create_mask()
    rtr_ip_mask = rtripCorpL3 + " " + mask_CorpL3
    write_L3()

    ip_address = input("enter the subnet address for Vendor L3: ")
    rtr_ip_mask_old = "10.105.x.x 255.255.255.248 -vendorl3rtr"
    l3_ip_old = "10.105.x.x -vendorl3"
    subnet_CorpL3 = ip_address
    rtripCorpL3, l3_ip_corp = create_rtripL3()
    mask_CorpL3, wildcard_CorpL3 = create_mask()
    rtr_ip_mask = rtripCorpL3 + " " + mask_CorpL3
    write_L3()

    ip_address = input("enter the subnet address for MGMT L3: ")
    rtr_ip_mask_old = "10.105.x.x 255.255.255.248 -mgmtl3rtr"
    l3_ip_old = "10.105.x.x -mgmtl3"
    subnet_CorpL3 = ip_address
    rtripCorpL3, l3_ip_corp = create_rtripL3()
    mask_CorpL3, wildcard_CorpL3 = create_mask()
    rtr_ip_mask = rtripCorpL3 + " " + mask_CorpL3
    write_L3()

    print("L3 IPs Written")

# this asks for static ip or dhcp, and writes the relevant details to the config (eg. ip address dhcp, default route)
if connection_type == "VPN":
    ISP_Connection = input("please enter the IP address and mask for WAN, if site uses DHCP enter DHCP: ")
    if ISP_Connection == "dhcp":
        ISP_Connection = "DHCP"
        print("Router will use DHCP")
    if ISP_Connection != "DHCP":
        ISP_Connection = "ip address " + ISP_Connection
        default_gateway = input("enter the default gateway: ")
        default_route = "ip route 0.0.0.0 0.0.0.0 " + default_gateway
        fout2 = open("RTR Config.txt", "rt")
        data = fout2.read()
        data = data.replace("ip address dhcp", ISP_Connection)
        fout2.close()
        fout2 = open("RTR Config.txt", "wt")
        fout2.write(data)
        fout2.close()
        fout2 = open("RTR Config.txt", "a")
        fout2.write(default_route)
        fout2.close()
        print("WAN IP written")
input("Router config created, press enter to exit")
