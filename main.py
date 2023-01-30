###################################################################
#!/usr/bin/python3

import os
import subprocess
import sys
import re
import glob

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

untar_filename = subprocess.run(["tar","-xf",unxz_tar_file_name.split(".xz",1)[0]])
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

#### Messages greping section #################

options = {1: "To fetch error related to file system and disk", 2: "To fetch the error related to Memory", 3: "To fetch the error related to softlock CPU and kernel panic", 4: "To fetch possible error related to Antivirus issues and endpoint security daemon", 5: "To fetch all possible error related to the messages", 6: "Exit option selected to come out of this script"}

print("Select an option , i.e provide the input as number for the option:")
for key, value in options.items():
    print(key, value)

selected_option = int(input())

if selected_option == 1:
        
        print("You selected Option 1 , which fetch error related to file system and disk")
        # Find all .txt files in the current directory
        txt_files = glob.glob('/var/log/messages*')
        # List of strings to search for
        strings_to_search = ['fsck','XFS internal error','xfs_force_shutdown','I/O error','xfs_do_force_shutdown','Corruption detected','xfs_buf_ioend','xfs_trans_read_buf','xfs_inode block','io_schedule_timeout','xfs_inode','xfs_inactive_ifree','xfs_iunlink_remove','xfs_imap_to_bp','EXT4-fs error','EXT4-fs warning','JBD: Spotted dirty metadata buffer','EXT3-fs error','blk_update_request','Buffer I/O error']
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

elif selected_option == 2:
    print("You selected Option 2, which fetch error related to Memory")
    
    # Find all .txt files in the current directory
    txt_files = glob.glob('/var/log/messages*')
    # List of strings to search for
    strings_to_search = ['lowmem_reserve','Out of memory:','Killed process','oom-killer','check_panic_on_oom','oom_score_adj','do_page_fault']
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
    

    # perform action for Option 2

elif selected_option == 3:
    print("You selected Option 3, which fetch error related to softlock CPU and kernel panic")
    
    # Find all .txt files in the current directory
    txt_files = glob.glob('/var/log/messages*')
    # List of strings to search for
    strings_to_search = ['BUG: soft lockup','__do_softirq','RIP:','_raw_spin_unlock_irqrestore','unable to handle kernel paging request','unable to handle kernel NULL pointer dereference','Oops:','BUG:','PGD','Oops:','segfault at','do_page_fault','Kernel panic - not syncing','Fatal exception']
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
                            
    # perform action for Option 3

elif selected_option == 4 :
    print("To fetch possible error related to Antivirus issues and endpoint security daemon")
    
    # Find all .txt files in the current directory
    txt_files = glob.glob('/var/log/messages*')
    # List of strings to search for
    strings_to_search = ['falcon_lsm_serviceable','twnotify_sys_close','twnotify','tmhook_invoke','tmhook_handler','dsa_filter','core_pkt_filter','core_pkt_hook','symev_rh_','symev_hook']
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
                            
    # perform action for Option 4
elif selected_option == 5 :
    print("To fetch all possible error related to the messages")
    
    # Find all .txt files in the current directory
    txt_files = glob.glob('/var/log/messages*')
    # List of strings to search for
    strings_to_search = ['fsck','XFS internal error','xfs_force_shutdown','I/O error','xfs_do_force_shutdown','Corruption detected','xfs_buf_ioend','xfs_trans_read_buf','xfs_inode block','io_schedule_timeout','xfs_inode','xfs_inactive_ifree','xfs_iunlink_remove','xfs_imap_to_bp','EXT4-fs error','EXT4-fs warning','JBD: Spotted dirty metadata buffer','EXT3-fs error','blk_update_request','Buffer I/O error''lowmem_reserve','Out of memory:','Killed process','oom-killer','check_panic_on_oom','oom_score_adj','do_page_fault','BUG: soft lockup','__do_softirq','RIP:','_raw_spin_unlock_irqrestore','unable to handle kernel paging request','unable to handle kernel NULL pointer dereference','Oops:','BUG:','PGD','Oops:','segfault at','do_page_fault','Kernel panic - not syncing','Fatal exception','falcon_lsm_serviceable','twnotify_sys_close','twnotify','tmhook_invoke','tmhook_handler','dsa_filter','core_pkt_filter','core_pkt_hook','symev_rh_','symev_hook']
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
        # perform action for Option 5
        
elif selected_option == 6 :
    print("Exit option selected to come out of this script")
    exit()
        # perform action for Option 6
else:
    print("Invalid option selected")

