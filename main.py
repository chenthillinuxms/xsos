###################################################################

#!/usr/bin/python3

import os
import subprocess
import sys
import glob
import re


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

# Find all .txt files in the current directory
txt_files = glob.glob('/var/log/messages*')

# List of strings to search for
strings_to_search = ['xfs','I/O error','xfs_do_force_shutdown','Corruption detected','xfs_buf_ioend','xfs_trans_read_buf','xfs_inode block','io_schedule_timeout','xfs_inode','xfs_inactive_ifree','xfs_iunlink_remove','xfs_imap_to_bp']


# Iterate over the files
for txt_file in txt_files:
    with open(txt_file) as f:
        # Read the contents of the file into a string
        file_contents = f.read()
        # Iterate over the strings to search for
        for search_string in strings_to_search:
            # Search for the string in the file
            if re.search(search_string, file_contents):
                print(f'Found {search_string} in {txt_file}')
                # Print the lines containing the string
                for line in file_contents.split('\n'):
                    if search_string in line:
                        print(line)
