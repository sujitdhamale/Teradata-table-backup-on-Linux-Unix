# Python based tool for taking Teradata backup on Unix or Linux


* This tool will help To Avoid space issue in Teradata and use Unix Space to backup table this tool helpful 
* It will export table data in Unix using fast export
* Easy to retrieve data 


## Steps to Execute

1. Copy script **(One time)**
		Copy python script FastExport.py from git
1. Update below in script FastExport.py
  	* host
  	* user
  	* password
  	* db_name
1.	Create file **list.txt**  and add the table name 
		one table name each line
1.	create folder **out** and provide write permission to it 
1.	Execute the script using below command
  	* Python FastExport.py
1.	This script will create below output 
  	*	Create ctl file using this ctl data is will be export on Unix/Linux
  	*	Create data files  to store exported data 
  	*	Create mlod file which will be useful for reloading data into terada 
	 
	
---------------------------------------------------------------------------------------
#### Relaod data (to retrive backup into  original table )
###### Using mload command data can be relaoded 

