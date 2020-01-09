################ imports ################
import os
import time

################ vars ################
DownloadsDir="/home/tayf/Downloads/"

filter=[["Apps",".exe",".msi",".bin"],
["Archives",".zip",".rar",".tar",".bz2",".gz"],
["Pics",".jpg",".png",".svg",".drawio"],
["Torrents",".torrent"],
["Docs",".pdf",".xlsx",".docx",".ods",".csv",".rtf"],
["Media",".avi"],
["Subs",".srt"],
["Etc",".txt",".xml",".sql",".kdbx",".key",".ino",".log",".cap",".crt",".ovpn",".py",".pcap",".conf"],
["ISO",".iso",".img"],]

################ defs ################
def get_downloads_content():
    return os.listdir(DownloadsDir)

def sort_downloads_content(filter, content):
    for file in content:
        moved=False
        fullpath=DownloadsDir+file
        if os.path.isdir(fullpath):
            continue
        else:
            for x in filter:
                if os.path.splitext(fullpath)[1].lower() in x:
                    newpath=DownloadsDir+x[0]+'/'+file
                    move_files(fullpath,newpath)
                    moved=True
        if not moved:
            print("SKIPPING: "+fullpath)

def move_files(original,new):
    if os.path.isfile(new):
        new=os.path.splitext(new)[0]+" (COPY)"+os.path.splitext(new)[1]
        os.rename(original,new)
    else:
        os.rename(original,new)

def create_downloads_folders(filter):
    print("Folders:")
    for x in filter:
        fullpath=DownloadsDir+x[0]
        print(fullpath)
        try:
            os.mkdir(fullpath)
        except OSError:
            pass
    print("ALL folders created")

################################################################
create_downloads_folders(filter)

while True:
    print("New loop")
    sort_downloads_content(filter,get_downloads_content())
    time.sleep(10)
