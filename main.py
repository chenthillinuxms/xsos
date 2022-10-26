###################################################################

#!/usr/bin/python3

import os
import subprocess
import sys

print('cmd entry:', sys.argv)


xsos_download = subprocess.run(["curl","-Lo","/usr/local/bin/xsos","bit.ly/xsos-direct"])
xsos_download_status = xsos_download.returncode

if ( xsos_download_status == 0 ):
        print("xsos downloaded sucessfully.")
else:
        print("xsos failed to get download.")

xsos_execute_permission = subprocess.run(["chmod","+x","/usr/local/bin/xsos"])
xsos_execute_permission_returcode = xsos_execute_permission.returncode

if ( xsos_execute_permission_returcode == 0 ):
        print("xsos execute granded .")
else:
        print("xsos execute premission granting failed")


sosreport_unxz = subprocess.run(["unxz",sys.argv[1]])
sosreport_unxz_status = sosreport_unxz.returncode

if ( sosreport_unxz_status == 0 ):
        print("sosreport extracted sucessfully.")
else:
        print("sosreport extraction failed")

unxz_tar_file_name = sys.argv[1]
sosreport_directory = unxz_tar_file_name.split(".tar",1)[0]
tar_file_name  = unxz_tar_file_name.split(".xz",1)[0]
print(tar_file_name)
print(sosreport_directory)

untar_filename = subprocess.run(["tar","-xvf",unxz_tar_file_name.split(".xz",1)[0]])
untar_filename_status = untar_filename.returncode

if ( untar_filename_status == 0 ):
        print("tar  extracted sucessfully.")
else:
        print("tar extraction failed")

xsos_execution =  subprocess.run(["/usr/local/bin/xsos","--all",unxz_tar_file_name.split(".tar",1)[0]])
xsos_execution_status = xsos_execution.returncode

if ( untar_filename_status == 0 ):
        print("xsos analysis sucessfully created.")
else:
        print("xsos analysis failed")
