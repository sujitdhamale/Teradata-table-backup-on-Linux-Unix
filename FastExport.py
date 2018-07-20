import pandas as pd
import os


host="#############"
user="#######"
password="#######"
db_name="#########"



logon_string=r".logon "+host+"/"+user+","+password+";\n"

df = pd.read_csv('list.txt',header=None)
print(df.index)
for i in df.index:
    name=df[df.columns[0]][i]
    ctl_file=os.getcwd()+r"/out/"+name+".ctl"
    export_file=os.getcwd()+r"/out/"+name+".dat"
    mlod_file=os.getcwd()+r"/out/"+name+".mload"
    print("########################### EXPORTING {0} ###############################".format(name))
    file = open(ctl_file,"w")
    file.write(logon_string)
    file.write(".LOGTABLE CDW_SPOOL.td_"+name+";\n")
    file.write(".BEGIN EXPORT\n")
    file.write("SESSIONS 16;\n")
    file.write(".EXPORT OUTFILE "+export_file+"\n")
    file.write("FORMAT FASTLOAD\n")
    file.write("MLSCRIPT "+mlod_file+";\n")
    file.write("SELECT * from "+db_name+"."+name+";\n")
    file.write(".END EXPORT;\n")
    file.close()
    cmd="fexp < "+ctl_file
    os.system(cmd)
