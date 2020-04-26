import socket
import struct

IPV4LENGTH = 32
IPV6LENGTH = 128


def detect_addres_family_by_str(s):
    # TODO: Make it better !!!!!
    if ":" in s:
        return socket.AF_INET6
    return socket.AF_INET


def ipv4_to_ipv6_str(s):
    # TODO: Make it small
    octets = list(map(int, s.split('.')))
    return '2002:{:02x}{:02x}:{:02x}{:02x}::'.format(*octets)


def ip_to_int(addr):
    addr_family = detect_addres_family_by_str(addr)
    if addr_family == socket.AF_INET:
        return struct.unpack("!I", socket.inet_pton(addr_family, addr))[0]
    hi, lo = struct.unpack('!QQ', socket.inet_pton(socket.AF_INET6, addr))
    return (hi << 64) | lo


def int_to_ip(addr_family, addr):
    if addr_family == socket.AF_INET6:
        return socket.inet_ntop(addr_family, struct.pack('!QQ', addr >> 64, addr & (2**64 - 1)))
    return socket.inet_ntop(addr_family, struct.pack("!I", addr))


def int_to_bin_array(i, w):
    return [1 if d == '1' else 0 for d in bin(i)[2:].zfill(w)]


def bin_array_to_int(arr):
    return int(''.join([str(i) for i in arr]), 2)


def calc_min_network_by_ip_int(min_ip_int, max_ip_int, ip_len):
    """

    :return (First_network_address as bit array, offset)
    """
    min_ip_bin = int_to_bin_array(min_ip_int, ip_len)
    max_ip_bin = int_to_bin_array(max_ip_int, ip_len)
    cnt = 0
    net_addr_bin = []
    for i in range(0, ip_len, 1):
        if max_ip_bin[i] != min_ip_bin[i]:
            break
        cnt = cnt + 1
        net_addr_bin.append(max_ip_bin[i])
    for i in range(cnt, ip_len):
        net_addr_bin.append(0)
    return (net_addr_bin, cnt)


def format_network(ip, offset_bits):
    return "{}/{}".format(ip, offset_bits)
