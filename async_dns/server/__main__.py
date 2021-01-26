'''
This module starts a DNS server according to console arguments.
'''
import argparse
import asyncio
import yaml
from . import start_dns_server, run_forever
from ..core import logger, Address

def main():
    '''Start a DNS server from command line.'''
    parser = argparse.ArgumentParser(
        prog='python3 -m async_dns.server',
        description='DNS server by Gerald.')
    parser.add_argument(
        '-b', '--bind', default=':53',
        help='the address for the server to bind')
    parser.add_argument(
        '--hosts', default='local',
        help='the path of a hosts file, `none` to disable hosts, `local` to read from local hosts file')
    parser.add_argument(
        '-x', '--proxy', nargs='*', default=None,
        help='the proxy DNS servers, `none` to serve as a recursive server, `default` to proxy to default nameservers')
    parser.add_argument(
        '-s', '--spoofing', default=None,
        help='path to yaml file with spoofing lists')
    args = parser.parse_args()
    logger.info('DNS server v2 - by Gerald')
    if args.spoofing:
        logger.info('DNS Spoofing enabled')
        with open(args.spoofing) as f:
            spf = yaml.safe_load(f)
        logger.debug('Spoofing config: %s', spf)
    run_forever(start_dns_server(bind=args.bind, hosts=args.hosts, proxies=args.proxy, spf=spf))

main()
