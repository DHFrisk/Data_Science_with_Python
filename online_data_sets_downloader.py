# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
This script is for download datasets from a specific url and export to another format
"""
import csv, urllib3, pandas

class DownloadDataSet:
    
    def __init__(self, url, exportFormat, filePath, fileName, separator, lineSeparator):
        byteFile= self.Download(url)
        dataFrameDictionary= self.Format(byteFile, separator)
        self.Export(dataFrameDictionary)
    
    
    def Download(self, url):
        http= urllib3.PoolManager()
        try:
            response= http.request('POST', url)    
            print("File obtained successfully! Your file type is: "+ str(type(response)))
            return response.data
        except Exception as e:
            print("HTTP response error! {0}".format(e))
            exit()
    
    
    def Format(self, byteFile, separator):
        #I know this is not needed in python but I like to follow OOP, so... :D
        decodedFile=''
        fileToList=[]
        colList=[]
        rowList=[]        
        dataFrameDictionary= {}
        
        #decode the byteFile to utf-8
        decodedFile= byteFile.decode('utf-8')
        #convert decodedFile to a list
        fileToList= decodedFile.split(lineSeparator)
        #get column names
        colList= fileToList[0].split(separator)
        #delete column names from the list
        fileToList.pop(0)
        #get rows
        for i in fileToList:
            rowList.append(i.split(','))
        #build dict
        for i in range(len(colList)):
            for j in rowList:
                dataFrameDictionary[colList[i]].append(j[i])
        return dataFrameDictionary
    
    
    def Export(self, dictionary):
        fileName2= '/'+ fileName
        if exportFormat == 'json':
            pandas.DataFrame(dictionary).to_json(filePath+fileName2+'.json')
            print("Done!")
        if exportFormat == 'csv':
            pandas.DataFrame(dictionary).to_csv(filePath+fileName2+'.csv')
            print("Done!")
        if exportFormat == 'xlsx':
            pandas.DataFrame(dictionary).to_excel(filePath+fileName2+'.xlsx')
            print("Done!")
        if exportFormat == 'sql':
            #add sql export here
            print("Haven't added SQL export yet!")
        if exportFormat == 'numpy':
            #add numpy export here
            print("Haven't added numpy export yet!")


print('================================================================================================= \n This little script is for download datasets from a url                                         \n===============================================================================================')
print("Eneter the following values please: ")
url= str(input("URL: "))
exportFormat= str(input("Export format (json, csv, xlsx): "))
filePath= str(input("Path where you want to save your file: "))
fileName= str(input("Your filename: "))
separator= str(input("Define the field separator (usually is a comma (,)): "))
lineSeparator= str(input("Define the row/line separator (usually is a \n): "))
downloadDataSet= DownloadDataSet(url, exportFormat, filePath, fileName, separator, lineSeparator)
