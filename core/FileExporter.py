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

import csv
from xml.etree import ElementTree as etree
from collections import OrderedDict

class FileExporter:
    
    def __init__(self):
        pass
    
    def ExportListToCSV(self, ipGeoLocObjs, filename):
        return self.__ExportToCSV(ipGeoLocObjs, filename)
        
    def ExportToCSV(self, ipGeoLocObj, filename):
        return self.__ExportToCSV([ipGeoLocObj], filename)
    
    def ExportListToXML(self, ipGeoLocObjs, filename):
        return self.__ExportToXML(ipGeoLocObjs, filename)
    
    def ExportToXML(self, ipGeoLocObj, filename):
        return self.__ExportToXML([ipGeoLocObj], filename)

    def ExportListToTXT(self, ipGeoLocObjs, filename):
        return self.__ExportToTXT(ipGeoLocObjs, filename)
        
    def ExportToTXT(self, ipGeoLocObj, filename):
        return self.__ExportToTXT([ipGeoLocObj], filename)
    
    def __ExportToTXT(self, ipGeoLocObjs, filename):
        try:
            with open(filename, 'w') as txtfile:
                txtfile.write('Results IPGeolocation\n')
                for ipGeoLocObj in ipGeoLocObjs:
                    if ipGeoLocObj:
                        txtfile.write('Target: {}\n'.format(ipGeoLocObj.Query))
                        txtfile.write('IP: {}\n'.format(ipGeoLocObj.IP))
                        txtfile.write('ASN: {}\n'.format(ipGeoLocObj.ASN))
                        txtfile.write('City: {}\n'.format(ipGeoLocObj.City))
                        txtfile.write('Country: {}\n'.format(ipGeoLocObj.Country))
                        txtfile.write('Country Code: {}\n'.format(ipGeoLocObj.CountryCode))
                        txtfile.write('ISP: {}\n'.format(ipGeoLocObj.ISP))
                        txtfile.write('Latitude: {}\n'.format(ipGeoLocObj.Latitude))
                        txtfile.write('Longtitude: {}\n'.format(ipGeoLocObj.Longtitude))
                        txtfile.write('Organization: {}\n'.format(ipGeoLocObj.Organization))
                        txtfile.write('Region: {}\n'.format(ipGeoLocObj.Region))
                        txtfile.write('Region Name: {}\n'.format(ipGeoLocObj.RegionName))
                        txtfile.write('Timezone: {}\n'.format(ipGeoLocObj.Timezone))
                        txtfile.write('Zip: {}\n'.format(ipGeoLocObj.Zip))
                        txtfile.write('Google Maps: {}\n'.format(ipGeoLocObj.GoogleMapsLink))
                        txtfile.write('\n')
            return True
        except:
            return False
        
        
    def __ExportToXML(self, ipGeoLocObjs, filename):
        try:
            root = etree.Element('Results')
            
            for ipGeoLocObj in ipGeoLocObjs:
                if ipGeoLocObj:
                    orderedData = OrderedDict(sorted(ipGeoLocObj.ToDict().items()))
                    self.__add_items(etree.SubElement(root, 'IPGeolocation'),
                      ((key.replace(' ', ''), value) for key, value in orderedData.items()))
        
                    tree = etree.ElementTree(root)

            tree.write(filename, xml_declaration=True, encoding='utf-8')
                        
            return True
        except:
            return False
        
        
    def __ExportToCSV(self, ipGeoLocObjs, filename):
        try:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['Results', 'IPGeolocation'])
                for ipGeoLocObj in ipGeoLocObjs:
                    if ipGeoLocObj:
                        writer.writerow(['Target', ipGeoLocObj.Query])
                        writer.writerow(['IP', ipGeoLocObj.IP])
                        writer.writerow(['ASN', ipGeoLocObj.ASN])
                        writer.writerow(['City', ipGeoLocObj.City])
                        writer.writerow(['Country', ipGeoLocObj.Country])
                        writer.writerow(['Country Code', ipGeoLocObj.CountryCode])
                        writer.writerow(['ISP', ipGeoLocObj.ISP])
                        writer.writerow(['Latitude', ipGeoLocObj.Latitude])
                        writer.writerow(['Longtitude', ipGeoLocObj.Longtitude])
                        writer.writerow(['Organization', ipGeoLocObj.Organization])
                        writer.writerow(['Region', ipGeoLocObj.Region])
                        writer.writerow(['Region Name', ipGeoLocObj.RegionName])
                        writer.writerow(['Timezone', ipGeoLocObj.Timezone])
                        writer.writerow(['Zip', ipGeoLocObj.Zip])
                        writer.writerow(['Google Maps', ipGeoLocObj.GoogleMapsLink])
                        writer.writerow([])
            return True
        except:
            return False
        
    
    def __add_items(self, root, items):
        for name, text in items:
            elem = etree.SubElement(root, name)
            elem.text = text

