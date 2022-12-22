byte = b'This is a byte array \n.'

string = str(byte)

print("Byte : ",byte)
print("String : ", string)

decode = byte.decode()

print("Decode : ", decode)


errorMessage = b'I0605 15:43:22.896754745    6597 ev_epoll1_linux.cc:121]     grpc epoll fd: 3\nD0605 15:43:22.896881064    6597 ev_posix.cc:174]            Using polling engine: epoll1\nD0605 15:43:22.896949578    6597 lb_policy_registry.cc:39]   registering LB policy factory for "grpclb"\nD0605 15:43:22.896964371    6597 lb_policy_registry.cc:39]   registering LB policy factory for "cds_experimental"\nD0605 15:43:22.896977479    6597 lb_policy_registry.cc:39]   registering LB policy factory for "eds_experimental"\nD0605 15:43:22.896985969    6597 lb_policy_registry.cc:39]   registering LB policy factory for "lrs_experimental"\nD0605 15:43:22.896998170    6597 lb_policy_registry.cc:39]   registering LB policy factory for "priority_experimental"\nD0605 15:43:22.897006292    6597 lb_policy_registry.cc:39]   registering LB policy factory for "weighted_target_experimental"\nD0605 15:43:22.897014138    6597 lb_policy_registry.cc:39]   registering LB policy factory for "xds_routing_experimental"\nD0605 15:43:22.897022257    6597 lb_policy_registry.cc:39]   registering LB policy factory for "pick_first"\nD0605 15:43:22.897030189    6597 lb_policy_registry.cc:39]   registering LB policy factory for "round_robin"\nD0605 15:43:22.897038742    6597 dns_resolver_ares.cc:504]   Using ares dns resolver\nD0605 15:43:22.907832649    6597 tcp_posix.cc:1812]          cannot set inq fd=5 errno=92\nE0605 15:43:22.909072477    6597 port_server_client.cc:187]  assertion failed: port > 1024\n'

print(errorMessage.decode())


b = b'abc'
print(b[0])

import sys

v = sys.version_info
print(" Python Version : ", v)


if(b[0] == b'a'):
    print("Both are same !!!", v);


