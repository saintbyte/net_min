#!/usr/bin/env python3
import sys
import socket
import struct
from ipfunc import detect_addres_family_by_str, ipv4_to_ipv6_str, ip_to_int,\
    int_to_ip, int_to_bin_array, bin_array_to_int, calc_min_network_by_ip_int, format_network,  IPV4LENGTH, IPV6LENGTH


def has_ipv6_in_list(lst):
    for ip in lst:
        if detect_addres_family_by_str(ip) == socket.AF_INET6:
            return True
    return False


def convert_list_to_ipv6(lst):
    ip_list2 = []
    for ip in lst:
        if detect_addres_family_by_str(ip) == socket.AF_INET:
            ip = ipv4_to_ipv6_str(ip)
        ip_list2.append(ip)
    return ip_list2


def convert_list_ips_to_int(lst):
    ip_list2 = []
    for ip in lst:
        ip_list2.append(ip_to_int(ip))
    return ip_list2


def normalize_list(lst):
    ip_len_global = IPV4LENGTH
    addr_family_global = socket.AF_INET
    if has_ipv6_in_list(lst):
        addr_family_global = socket.AF_INET6
        ip_len_global = IPV6LENGTH
        lst = convert_list_to_ipv6(lst)
    lst = convert_list_ips_to_int(lst)
    return (ip_len_global, addr_family_global, lst)


def get_ips_from_args():
    argv = sys.argv
    if len(argv) > 1:
        if (argv[0] in ['python', 'python3', 'net_min.py']) or 'python' in argv[0]:
            argv = argv[1:]
    if 'net_min' in argv[0]:
        argv = argv[1:]
    return argv


def help():
    print("Usage: net_min.py [list of IPs]")
    quit()


def main():
    ip_list = get_ips_from_args()
    if len(ip_list) == 0:
        help()
    if len(ip_list) == 1:
        print('One IP network its for r341 h4x0rz')  # TODO: Make it some fun
        if detect_addres_family_by_str(ip_list[0]) == socket.AF_INET6:
            print(format_network(ip_list[0], IPV6LENGTH))
        else:
            print(format_network(ip_list[0], IPV4LENGTH))
        quit()
    (ip_len_global, addr_family_global, ip_list) = normalize_list(ip_list)
    (net_addr_bin, cnt) = calc_min_network_by_ip_int(
        min(ip_list), max(ip_list), ip_len_global)
    print(format_network(int_to_ip(addr_family_global,
                                   bin_array_to_int(net_addr_bin)), cnt))


if __name__ == '__main__':
    main()
