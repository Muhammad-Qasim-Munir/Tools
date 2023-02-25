#!/usr/bin/env python3

import argparse
import ipaddress

# Define function to convert CIDR range to IPs
def cidr_to_ips(cidr):
    network = ipaddress.ip_network(cidr, strict=False)
    return [str(ip) for ip in network.hosts()]

# Parse command line options
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip', help='convert a single CIDR range to IPs')
parser.add_argument('-l', '--list', help='convert multiple CIDR ranges from a file to IPs')
parser.add_argument('-o', '--output', help='save output to a file')
args = parser.parse_args()

# Check that mode is set
if not args.ip and not args.list:
    parser.print_usage()
    exit(1)

# Convert CIDR range(s) to IPs
ips = []
if args.ip:
    ips = cidr_to_ips(args.ip)
elif args.list:
    with open(args.list, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            ips.extend(cidr_to_ips(line))

# Output results
if args.output:
    with open(args.output, 'w') as f:
        f.write('\n'.join(ips) + '\n')
else:
    print('\n'.join(ips))
