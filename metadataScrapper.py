from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image, ImageFilter
import os
from bs4 import BeautifulSoup
import requests
import urllib.request,io
import argparse

def decode_gps_info(exif):
    """
        **Decode GPS Info**
        This Module retrieves the gps data on a given exif info
    """
    temp = ""
    if 'GPSInfo' in exif:
        #Parse geo references.
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][3] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        lat = Nmult * (exif['GPSInfo'][2][0] + (exif['GPSInfo'][2][1] + exif['GPSInfo'][2][2]/60.0)/60.0) #Ndeg Nmin Nsec
        lng = Wmult * (exif['GPSInfo'][4][0] + (exif['GPSInfo'][4][1] + exif['GPSInfo'][4][2]/60.0)/60.0) #Wdeg Wmin Wsec
        temp =f"Latitude: {lat}, Longitude: {lng}"
    return temp

def get_exif_metadata(image_path):
    """
        **get_exif_metadata**
        This Module extract metadata from a given image
    """
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    return ret

def save_image(image_path,name):
    """
        **Save Image**
        This Module Saves Image from given url
    """
    image = Image.open(image_path)
    #print(name)
    image.save(f"{name}")
    

def Metadata(url):
    """
        **Metadata**
        This Module is the main module to start the extraction of the exif info
    """
    furl = []
    if not os.path.exists('images'):
        os.makedirs('images')
    temp = os.getcwd()
    os.chdir("images")
    if not os.path.exists('txt'):
        os.makedirs('txt')
    if "https://" in url :
        r  = requests.get(url.replace("https://","http://" ))
    elif not "http://" in url:
        r = requests.get("http://"+url)
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data,'html.parser')
    for link in soup.find_all('img'):
        if link is not None:
            furl.append(link.get('src'))
    for i in range(0,(len(furl) - 1),1):
        imgurl = furl[i]
        fpath = io.BytesIO(urllib.request.urlopen(imgurl).read())        
        #print(imgurl.split("/")[-1])
        save_image(fpath,imgurl.split("/")[-1])
        with open(f"txt/{imgurl.split('/')[-1].split('.')[0]}.txt","w+") as txt: 
            print (f"[+] Metadata for file: {imgurl}")
            try:
                exif = get_exif_metadata(fpath)
                coords = decode_gps_info(exif)
                txt.write(f"[+] Metadata for file: {imgurl}")
                for metadata in exif:
                    print(coords)
                    print (f"Metadata: {metadata} - Value: {exif[metadata]}\n")
                    txt.writelines(f"\n Metadata: {metadata} - Value: {exif[metadata]}\n {coords}")
            except:
                import sys, traceback, PIL
                traceback.print_exc(file=sys.stdout)
    os.chdir(temp)


