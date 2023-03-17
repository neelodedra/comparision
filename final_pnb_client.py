from filecmp import dircmp
import os
import shutil



def ignore_files(dir, files):
            return [f for f in files if os.path.isfile(os.path.join(dir, f))]

# Identifying the different file

def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print(name, dcmp.left, dcmp.right)
        diff_src = dcmp.left + '/' + name 
        print(diff_src)
        path_list = dcmp.left.split("\\")
        print (path_list)
        
        if len(path_list) == 4 :
            copy_path = '/build/worksace/hsbc-242914-minds/PNB-ORACLE/update/'+path_list[1]+'/'+path_list[2]+path_list[3]
        if len(path_list) == 3 :
            copy_path = '/build/worksace/hsbc-242914-minds/PNB-ORACLE/update/'+path_list[1]+'/'+path_list[2]
        elif len(path_list) == 2 :
            copy_path = '/build/worksace/hsbc-242914-minds/PNB-ORACLE/update/'+path_list[1]
        else :
            copy_path = '/build/worksace/hsbc-242914-minds/PNB-ORACLE/update/'

        try:
            shutil.copytree(dcmp.left,copy_path,ignore=ignore_files)
        
        except FileExistsError:
            print("folder already created")



        shutil.copy2(diff_src,copy_path)
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)

# Identifying the unique file

def print_left_files(dcmp):
    for filename in dcmp.left_only:
        print(filename, dcmp.left, dcmp.right)
        left_src = dcmp.left + '/' + filename
        left_path_list = dcmp.left.split("\\")
        print (left_path_list)

        if len(left_path_list) == 3 :
            left_copy_path = '/build/worksace/hsbc-242914-minds/PNB-ORACLE/update/'+left_path_list[1]+'/'+left_path_list[2]
        elif len(left_path_list) == 2 :
            left_copy_path = '/build/worksace/hsbc-242914-minds/PNB-ORACLE/update/'+left_path_list[1]
        else :
            left_copy_path = '/build/worksace/hsbc-242914-minds/PNB-ORACLE/update/'

        try:
            shutil.copytree(dcmp.left,left_copy_path,ignore=ignore_files)

        except FileExistsError:
            print("folder already created")

        shutil.copy2(left_src,left_copy_path)

    for sub_dir in dcmp.subdirs.values():
        print_left_files(sub_dir)

path = '/build/worksace/hsbc-242914-minds/PNB-ORACLE/'
dcmp = dircmp(path+'oat',path+'master')

print_diff_files(dcmp)
print_left_files(dcmp)


