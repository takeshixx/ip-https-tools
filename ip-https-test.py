#!/usr/bin/env python2
# author: takeshix@adversec.com
import ssl,socket,sys

HTTP_REQ = """POST /IPHTTPS HTTP/1.1
Host: vpn1.contoso.com
Content-Length: 18446744073709551615

"""

def http_negotiation(s):
    s.write(HTTP_REQ)
    r = s.read()
    return r

def get_ssl_socket():
    HOST = sys.argv[1]
    PORT = 443
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = ssl.wrap_socket(s)
    ssl_sock.connect((HOST, PORT))
    return ssl_sock

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: {} HOST/IP'.format(sys.argv[0])

    try:
        s = get_ssl_socket()
        r = http_negotiation(s)

        if not 'HTTP/1.1 200' in r:
            raise Exception('IP-HTTPS is not supported.')

        print 'IP-HTTPS is supported.'
    except Exception as e:
        print 'Error: {}'.format(e)
