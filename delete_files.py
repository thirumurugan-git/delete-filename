import glob
import os
import sys

EXTENTION = '.txt.wx'

def get_spaced_filename(filename):
    if filename.isalpha():
        return filename

    for char_ind in range(len(filename)):
        if filename[char_ind].isalpha():
            break
    return filename[:char_ind]+" "+filename[char_ind:]


def get_the_file_name(file):
    for char in range(len(file)-1,-1,-1):
        if file[char] == "/":
            break
    return file[char+1:],file[:char+1]

def check_the_input_number(filename,search):
    stripped_file_name = filename.replace(EXTENTION,'')
    out_filename = None
    if search in stripped_file_name:
        #check whether the filename has only numeric value
        if stripped_file_name.isnumeric():
            out_filename = stripped_file_name.replace(search,'',1)#remove the count if you remove all occurence
        else:
            #if the file is alpha numeric get spaced name
            out_filename = get_spaced_filename(stripped_file_name)

    #this manage the collision
    if out_filename:
        return out_filename + EXTENTION
    return None

def main():

    #cheking requirements given
    search = None
    path = None
    try:
        path = sys.argv[2]
        path = path+'/' if path[-1]!='/' else path
    except:
        path = ''
        print("checking on the current directory")

    try: 
        search = sys.argv[1]
    except:
        print("provide searching file")
        return


    #main function starts
    
    all_files = glob.glob('%s**/*%s'%(path,EXTENTION),recursive=True)
    for file in all_files:

        #getting filename and directory
        filename,directory = get_the_file_name(file)
        
        #check whether the file has input number 
        modified_filename = check_the_input_number(filename,search)
        
        if modified_filename:
            #rename the file
            os.rename(file,directory+modified_filename)
            
            #printing filename and modified filename 
            print(file,"=>",directory+modified_filename)


if __name__ == "__main__":
    main()