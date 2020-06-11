import  os
from os.path import join
import time
import csv


def modification_date(filename):
        t = os.path.getmtime(filename)
        t_1=time.ctime(t)
        return t_1

def creation_date(filename):
    from PIL import Image

    im = Image.open(filename)
    exif = im.getexif()
    creation_time = exif.get(36867)
    if creation_time==None:
        creation_time="Timeless Memory"
    creation_time=str.split(creation_time)
    return creation_time
rows=[]
for root, dirs, files in os.walk("."):
        for name in files:

           rows.append([join(name), creation_date(join(root, name))])
fields=["Name","Date","Time"]
filename="Images,DateTime"
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)
