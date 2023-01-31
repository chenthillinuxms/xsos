AUTOMATED SOSREPORT ANALYSIS

This python Script has been designed to read the sosreport for RHEL 8 version and extract data from sosreport for log analysis . This script pull the latest version of 
xsos open source tool and will use them for extracting sosreport data and also performs important error string analysis from the messages files . 

More information on Xsos : 
https://access.redhat.com/discussions/469323
https://access.redhat.com/solutions/511753

How to use this script :-

kindly download the main.py script on RHEL 8 VM and add execute permission and trigger as the script as given below . 


#./main.py sosreport-RHEL8LAB-2023-01-30-qxhbofe.tar.xz


Error String Analysis :-

This script provide 5 different option to perform a error string analysis for the messages file present inside the sosreport . 

Case 1 :-
1 To fetch error related to file system and disk


Case 2 :-
2 To fetch the error related to Memory

Case 3:-
3 To fetch the error related to softlock CPU and kernel panic

Case 4:-
4 To fetch possible error related to Antivirus issues and endpoint security daemon

Case 5:-
5 To fetch all possible error related to the messages

Case 6:-
6 Exit option selected to come out of this script












Future Plan :
We are planning to extend the AUTOMATED SOSREPORT ANALYSIS for differnet version on RHEL and SUSE distro also . 
https://snapcraft.io/install/xsos/opensuse
