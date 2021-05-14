#!/usr/bin/env python3
# encoding: UTF-8

"""
     IPTrack tool.
    https://github.com/Strix2109/IPTrack.git
    
 ____ _____ ____  _____  __   ___ ____
/ ___|_   _|  _ \|_ _\ \/ /  |_ _|  _ \
\___ \ | | | |_) || | \  /    | || |_) |
 ___) || | |  _ < | | /  \    | ||  __/
|____/ |_| |_| \_\___/_/\_\  |___|_|
By STRIX CYBER COMMUNITY
Instagram- @strix_21
Youtube- STRIX.D
    IPGeoLocation - Retrieve IP Geolocation information 
    Powered by http://ip-api.com
"""

__author__  = 'Santkr.'


import webbrowser, ipaddress, socket
from sys import platform as _platform
from subprocess import call
from urllib import request
from core import MyExceptions 
from core.Logger import Logger

class Utils:
    
    def __init__(self, nolog=False, verbose=False):    
        self.Logger = Logger(nolog, verbose)
        
        
    def openLocationInGoogleMaps(self, ipGeolObj):
        """Open IP Geolocation in Google Maps with default browser"""
        if type(ipGeolObj.Longtitude) == float and type(ipGeolObj.Latitude) == float:
            self.Logger.Print('Opening Geolocation in browser..')
            
            if _platform == 'cygwin':
                call(['cygstart', ipGeolObj.GoogleMapsLink])
                
            elif _platform == 'win32' or _platform == 'linux' or _platform == 'linux2':
                webbrowser.open(ipGeolObj.GoogleMapsLink)
            
            else:
                self.Logger.PrintError('-g option is not available on your platform.')
                
                
    def hostnameToIP(self, hostname):
        """Resolve hostname to IP address"""
        try:
            return socket.gethostbyname(hostname)
        except:
            return False
    
    
    def isValidIPAddress(self, ip):
        """Check if ip is a valid IPv4/IPv6 address"""
        try:
            ipaddress.ip_address(ip)
            return True
        except:
            return False
    
            
    def checkProxyConn(self, url, proxy):
        """check proxy connectivity"""
        check = True
        self.Logger.Print('Testing proxy {} connectivity..'.format(proxy))
    
        try:
            req = request.Request(url)
            req.set_proxy(proxy, 'http')
            request.urlopen(req)
        except:
            check = False
        
        if check == True:
            self.Logger.Print('Proxy server is reachable.')
        else:
            raise MyExceptions.ProxyServerNotReachableError()
            
            
