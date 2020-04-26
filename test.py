import socket
import struct
import pytest
import sys

sys.path.insert(0, './')

from ipfunc import detect_addres_family_by_str, ipv4_to_ipv6_str, ip_to_int,\
    int_to_ip, int_to_bin_array, bin_array_to_int, calc_min_network_by_ip_int, IPV4LENGTH, IPV6LENGTH

from net_min import has_ipv6_in_list, convert_list_to_ipv6, convert_list_ips_to_int, normalize_list


class TestFunctions(object):
    ip_list = [
        '23.129.64.194',
        '23.129.64.200',
        '23.129.64.202',
        '23.129.64.204',
        '23.129.64.207',
        '23.129.64.226',
        '23.129.64.232',
        '5.199.135.107',
        '5.199.135.107',
        '5.199.135.107',
        '18.27.197.252',
        '23.129.64.157',
        '23.129.64.182',
        '23.129.64.184',
        '23.129.64.188',
        '23.129.64.191',
        '45.137.184.71',
        '45.154.255.44',
        '46.38.235.14',
        '46.165.230.5',
        '46.165.245.154',
        '46.166.139.111',
        '24.13.225.30',
        '24.107.120.217',
        '24.120.54.171',
        '38.86.43.91',
        '1.1.1.1',
        '45.18.96.160',
        '45.67.14.0',
        '45.128.133.242',
    ]
    ip_list2 = [
        '127.9.0.2',
        '2002:7a2d:4399::'
    ]

    def test_detect_addres_family_by_str1(self):
        assert detect_addres_family_by_str(
            '2002:7a2d:4399::') == socket.AF_INET6

    def test_detect_addres_family_by_str2(self):
        assert detect_addres_family_by_str('127.0.0.1') == socket.AF_INET

    def test_detect_addres_family_by_str3(self):
        assert detect_addres_family_by_str(
            '2002:7a2d:4399::') == socket.AF_INET6

    def test_ipv4_to_ipv6_str1(self):
        assert ipv4_to_ipv6_str('31.13.145.138') == '2002:1f0d:918a::'

    def test_ipv4_to_ipv6_str2(self):
        try:
            ipv4_to_ipv6_str('2002:7a2d:4399::')
            assert False
        except:
            assert True

    def test_ipv4_to_ipv6_str3(self):
        try:
            ipv4_to_ipv6_str('')
            assert False
        except:
            assert True

    def test_ip_to_int1(self):
        assert ip_to_int('24.107.120.217') == 409696473

    def test_ip_to_int2(self):
        assert ip_to_int('5.199.135.107') == 96962411

    def test_ip_to_int3(self):
        assert ip_to_int('46.165.245.154') == 782628250

    def test_ip_to_int4(self):
        assert ip_to_int(
            '2001:db8:85a3::8a2e:370:7334') == 42540766452641154071740215577757643572

    def test_ip_to_int5(self):
        assert ip_to_int(
            '2002:7a2d:4399::') == 42548158498993797542296958064054501376

    def test_ip_to_int6(self):
        assert ip_to_int('0.0.0.0') == 0

    def test_int_to_ip1(self):
        assert int_to_ip(socket.AF_INET, 409696473) == '24.107.120.217'

    def test_int_to_ip2(self):
        assert int_to_ip(socket.AF_INET, 96962411) == '5.199.135.107'

    def test_int_to_ip3(self):
        assert int_to_ip(socket.AF_INET, 782628250) == '46.165.245.154'

    def test_int_to_ip4(self):
        assert int_to_ip(
            socket.AF_INET6, 42540766452641154071740215577757643572) == '2001:db8:85a3::8a2e:370:7334'

    def test_int_to_ip5(self):
        assert int_to_ip(
            socket.AF_INET6, 42548158498993797542296958064054501376) == '2002:7a2d:4399::'

    def test_int_to_bin_array1(self):
        assert int_to_bin_array(ip_to_int('0.0.0.0'), IPV4LENGTH) == [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0]

    def test_int_to_bin_array2(self):
        assert int_to_bin_array(ip_to_int('24.107.120.217'), IPV4LENGTH) == [
            0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1]

    def test_int_to_bin_array3(self):
        assert int_to_bin_array(ip_to_int('5.199.135.107'), IPV4LENGTH) == [
            0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1]

    def test_int_to_bin_array4(self):
        assert int_to_bin_array(ip_to_int('2001:db8:85a3::8a2e:370:7334'), IPV6LENGTH) == [
            0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1,
            0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0]

    def test_int_to_bin_array5(self):
        assert int_to_bin_array(ip_to_int('2002:7a2d:4399::'), IPV6LENGTH) == [
            0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1,
            0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def test_bin_array_to_int1(self):
        assert bin_array_to_int([
            0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1,
            0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 42548158498993797542296958064054501376

    def test_bin_array_to_int2(self):
        assert bin_array_to_int([
            0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1,
            0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0]) == 42540766452641154071740215577757643572

    def test_bin_array_to_int3(self):
        assert bin_array_to_int([0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1,
                                 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1]) == 96962411

    def test_bin_array_to_int4(self):
        assert bin_array_to_int([0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0,
                                 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1]) == 409696473

    def test_bin_array_to_int5(self):
        assert bin_array_to_int([0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0]) == 0

    def test_calc_min_network_by_ip_int1(self):
        min_ip = ip_to_int('5.199.135.107')
        max_ip = ip_to_int('5.199.135.102')
        assert calc_min_network_by_ip_int(min_ip, max_ip, IPV4LENGTH) == (
            int_to_bin_array(ip_to_int('5.199.135.96'), IPV4LENGTH), 28)

    def test_calc_min_network_by_ip_int2(self):
        min_ip = ip_to_int('5.199.135.107')
        max_ip = ip_to_int('45.199.135.103')
        assert calc_min_network_by_ip_int(max_ip, min_ip, IPV4LENGTH) == (
            int_to_bin_array(0, IPV4LENGTH), 2)

    def test_has_ipv6_in_list1(self):
        assert has_ipv6_in_list(self.ip_list2)

    def test_has_ipv6_in_list2(self):
        assert not has_ipv6_in_list(self.ip_list)

    def test_convert_list_to_ipv6v1(self):
        assert convert_list_to_ipv6(self.ip_list2) == [
            '2002:7f09:0002::', '2002:7a2d:4399::']

    def test_convert_list_ips_to_int(self):
        assert convert_list_ips_to_int(self.ip_list2) == [
            2131296258, 42548158498993797542296958064054501376]
