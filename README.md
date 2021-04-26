HOW TO USE THIS:

    this file change the name of the all ".txt.wx" extention file with deleting provided string from the filename.
    this works in recursive file

    example:

    if the file is '1111.txt.wx'
    if you want to remove the character 1 from the file

    you can run the file 
        "python3 delete_files.py 1"
    the corresponding output will be
        '111.txt.wx'

    if the file contains alpha numeric values
    it make space between alpha and numbers, for example.
    
    "02ma.txt.wx" to "02 ma.txt.wx"

    syntax:

    python3 delete_files.py <number to delete> <path to files directory>

    if the script file in files contained directory

    python3 delete_files.py <number to delete>

    you can change the extension from "txt.wx" to any other extention by changing EXTENSION variable.

    if you want to remove the same character recursively from the filename, you can use following line code in 29th line of delete_files.py instead of old line

    out_filename = stripped_file_name.replace(search,'')

