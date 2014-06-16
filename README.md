ip-https-tools
==============

A collection of tools for the IP over HTTPS (IP-HTTPS) Tunneling Protocol used by Microsoft DirectAccess to send Teredo related IPv6 packets over an IPv4-based HTTPS session.

* [\[MS-IPHTTPS\] \(protocol pecification\)](http://msdn.microsoft.com/en-us/library/dd358571)
* [DirectAccess Technical Overview](http://technet.microsoft.com/en-US/de-us/library/dd637827)
* [DirectAccess Requirements](http://technet.microsoft.com/en-us/library/dd637797)
* [DirectAccess Deployment Guide](http://technet.microsoft.com/en-us/library/ee649163)


#### ip-https-discover.nse
A NSE script for Nmap that checks if IP-HTTPS is supported by a given host.
Sample output:
```
 ip-https-tools » nmap -p443 --script ./ip-https-discover.nse 172.23.11.201

 Starting Nmap 6.46 ( http://nmap.org ) at 2014-06-16 11:29 CEST
 Nmap scan report for 172.23.11.201
 Host is up (0.00065s latency).
 PORT    STATE SERVICE
 443/tcp open  https
 |_ip-https-discover: IP-HTTPS is supported. This indicates that this host supports Microsoft DirectAccess.
 
 Nmap done: 1 IP address (1 host up) scanned in 12.61 seconds )
```
#### ip-https-test.py
A Python script that checks if IP-HTTPS is supported by a given host.
