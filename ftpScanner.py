try:
    from ftplib import FTP
except:
    print("Falta libreria ftplib \n pip install ftplib")
    exit()

def dir(host,user,password,anonymous):
    """
        **Dir**
        This Module find files in a given FTP Host
    """
    if user and password:
        ftp=FTP(host,user,password)
    elif anonymous:
        ftp=FTP(host,'anonymous','anonymous') 
    files=ftp.nlst()
    ftp.quit()
    return files
