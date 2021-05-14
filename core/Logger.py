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

from datetime import datetime
import os
from termcolor import colored
from sys import platform as _platform


if _platform == 'win32':
    import colorama
    colorama.init()

def Red(value):
        return colored(value, 'red', attrs=['bold'])
    
def Green(value):
    return colored(value, 'green', attrs=['bold'])
    
          
class Logger:
    
    def __init__(self, nolog=False, verbose=False):
        self.NoLog = nolog
        self.Verbose = verbose
        
        
    def WriteLog(self, messagetype, message):
        filename = '{}.log'.format(datetime.strftime(datetime.now(), "%Y%m%d"))
        path = os.path.join('.', 'logs', filename)
        with open(path, 'a') as logFile:
            logFile.write('[{}] {} - {}\n'.format(messagetype, datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"), message))
              
              
    def PrintError(self, message):
        """Print/Log error message"""
        if not self.NoLog:
            self.WriteLog('ERROR', message)
        
        print('[{}] {}'.format(Red('ERROR'), message))
    
    
    def PrintResult(self, title, value):
        """print result to terminal"""
        print('{}: {}'.format(title, Green(value)))
    
    
    def Print(self, message):
        """print/log info message"""
        if not self.NoLog:
            self.WriteLog('INFO', message)
            
        if self.Verbose:
            print('[{}] {}'.format(Green('**'), message))
    
    
    def PrintIPGeoLocation(self, ipGeoLocation):
        """print IP Geolocation information to terminal"""
        self.PrintResult('\nTarget', ipGeoLocation.Query)
        self.PrintResult('IP', ipGeoLocation.IP)
        self.PrintResult('ASN', ipGeoLocation.ASN)
        self.PrintResult('City', ipGeoLocation.City)
        self.PrintResult('Country', ipGeoLocation.Country)
        self.PrintResult('Country Code', ipGeoLocation.CountryCode)
        self.PrintResult('ISP', ipGeoLocation.ISP)
        self.PrintResult('Latitude', str(ipGeoLocation.Latitude))
        self.PrintResult('Longtitude', str(ipGeoLocation.Longtitude))
        self.PrintResult('Organization', ipGeoLocation.Organization)
        self.PrintResult('Region Code', ipGeoLocation.Region)
        self.PrintResult('Region Name', ipGeoLocation.RegionName)
        self.PrintResult('Timezone', ipGeoLocation.Timezone)
        self.PrintResult('Zip Code', ipGeoLocation.Zip)
        self.PrintResult('Google Maps', ipGeoLocation.GoogleMapsLink)
        print()
        #.encode('cp737', errors='replace').decode('cp737')
    
