from contextlib import redirect_stderr
import datetime
import time

#date till block
end_time = datetime.datetime(2021,12,04)
#sites to block
site_block=["abc.com","fb.com"]
#
host_path="C:/windows/system32/drivers/etc/hosts"
redirect="127.0.0.1"

while True:
    if datetime.datetime.now()<end_time:
        print("start blocking`")
        with open(host_path,"r+") as host_file:
            content=host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect+" "+website+"\n")
                else:
                    pass
    else:
        with open(host_path,"r+") as host_file:
            content=host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)
            
            host_file.truncate()
            time.sleep(5)