import os
import hashlib
import shutil
import glob
import configparser
import stat
from collections import defaultdict
from datetime import datetime
from functools import partial

class FileHelper:
    def __init__(self):
        pass
        
    # get parent dir path, depends how far <upLevel> from current file path 
    def get_upLevel_path(self, upLevel):       
        current_path = os.path.dirname(os.path.abspath(__file__))
        for i in range (upLevel):
            # Define the parent directory of the script directory
            current_path = os.path.abspath(os.path.join(current_path, os.pardir))
        return current_path 

    def copy_file(self, src_file_path, des_file_path):
        # os.makedirs(des_file_path, exist_ok=True)
        shutil.copy2(src_file_path, des_file_path)

    def copy_files_to_folder(self, src_file_path_list, des_folder_path):
        if isinstance(src_file_path_list, list):
            pass
        else:
            src_file_path_list = [src_file_path_list]
            pass
        
        for file_path in src_file_path_list:
            # Check if the file exists
            if not os.path.isfile(file_path):
                print(f"Error: The file '{file_path}' does not exist.")
            else:                
                # Check if the folder exists
                if not os.path.isdir(des_folder_path):       
                    os.makedirs(des_folder_path, exist_ok=True)             
                    
                else:
                    file_name = os.path.basename(file_path)
                    destination_path = os.path.join(des_folder_path, file_name)
                    shutil.copy2(file_path, des_folder_path)                
                    print(f"Copied {file_path} to {des_folder_path}")

    # copy all FILES (no DIRs) from source directory to destination directory
    def copy_files(self, src_dir, des_dir, dot_ext_name):
        os.makedirs(des_dir, exist_ok=True)
        
        # Iterate through the files in the source directory
        for item in os.listdir(src_dir):                
            # Construct the full path of the source item
            source_item = os.path.join(src_dir, item)
        
            # Check if the item is a file (not a directory)
            if os.path.isfile(source_item) and source_item.endswith(dot_ext_name):
                # Construct the full path of the destination item
                destination_item = os.path.join(des_dir, item)
                
                # Copy the file to the destination directory
                shutil.copy2(source_item, destination_item)
                print(f"Copied {source_item} to {destination_item}")

    # copy single/multiple folders to another folder
    def copy_folders(self, src_folder_path_list, des_folder_path, cb_handler):
        if isinstance(src_folder_path_list, list):
            pass
        else:
            src_folder_path_list = [src_folder_path_list]
            
        for src_folder_path in src_folder_path_list:            
            if os.path.exists(src_folder_path):
                try: 
                    shutil.copytree(src_folder_path, os.path.join(des_folder_path, os.path.basename(src_folder_path)))          
                    cb_handler()
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print(f"Folder {src_folder_path} doesn't exist")
                pass   
        
    # Calculate the SHA256 hash of the file
    def calculate_file_hash(self, file_path):
        hash_sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                hash_sha256.update(byte_block)
        return hash_sha256.hexdigest()

    # copy all FILES (recursively) from <src_folder> (incl. all sub-folders) to <des_folder> with extension name
    def copy_all_files(self, src_path, des_path, dot_ext_name, shortcut_path):
        # Ensure the destination directory exists
        os.makedirs(des_path, exist_ok=True)

        # Walk through the source directory
        for root, _, files in os.walk(src_path):
            for file in files:
                # Check if the file has the desired extension
                if file.endswith(dot_ext_name):
                    src_file_path = os.path.join(root, file)  # Full path of source file
                    des_file_path = os.path.join(des_path, file)  # Full path of destination file
                    
                    # Copy the file to the destination directory
                    shutil.copy2(src_file_path, des_file_path)
                    # print(f"Copied {src_file_path} to {des_file_path}")    
                    short_src_file_path = str(src_file_path).replace(shortcut_path, '')
                    short_des_file_path = str(des_file_path).replace(shortcut_path, '')
                
                    text1 = "Copied .."   + short_src_file_path
                    text2 = "to .."       + short_des_file_path
                    self.print_fixed_len_txt(text1, 150, text2, 75)
                    
    # rename files due to <file_label> in <config_file>
    def rename_file(self,  src_path, file_label, config_file):
        # Read the product.ini file
        config = configparser.ConfigParser()
        config.read(config_file)
        
        # Get the label under [FILE_STP_PRERUN]
        new_file_label = config.get(file_label, 'label')
        
        # List all files in the output directory
        files_to_rename = glob.glob(os.path.join(src_path, "*"))
        
        renamed_paths = []
        
        for file_path in files_to_rename:
            # Get the file extension
            file_ext = os.path.splitext(file_path)[1]
            
            # Construct the new file name with the label and same extension
            new_file_name = f"{new_file_label}{file_ext}"
            
            # Construct the new file path
            new_file_path = os.path.join(src_path, new_file_name)
            
            # Rename the file
            os.rename(file_path, new_file_path)
            
            # Append the new file path to the list
            renamed_paths.append(new_file_path)
            
            
            print("change file/dir name to", new_file_name)
    
    # remove file <file_path>
    def remove_file(self, file_path):
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"{file_path} has been removed successfully.")
            else:
                print(f"{file_path} does not exist.")
        except OSError as e:
            print(f"Error: {e.strerror}. {file_path}")
            
    def remove_folder(self, folder_path_list):
        if isinstance(folder_path_list, list):
            pass
        else:
            folder_path_list = [folder_path_list]
            
        for folder_path in folder_path_list:            
            if os.path.exists(folder_path):
                try: 
                    shutil.rmtree(folder_path)
                    print(f"Folder {folder_path} has been removed")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print(f"Folder {folder_path} doesn't exist")
                pass        
    
    def clean_folder(self, folder_path_list):
        if isinstance(folder_path_list, list):
            pass
        else:
            folder_path_list = [folder_path_list]

        for folder_path in folder_path_list:   
            # Change permissions of the folder and its contents
            for root, dirs, files in os.walk(folder_path):
                for dir in dirs:
                    os.chmod(os.path.join(root, dir), stat.S_IRWXU)
                for file in files:
                    os.chmod(os.path.join(root, file), stat.S_IRWXU)                             
            shutil.rmtree(folder_path, onerror=os.chmod(folder_path, stat.S_IWRITE))
            os.makedirs(folder_path)
            print(f"Folder {folder_path} has been cleaned")        
                
        
    # scan all files in a folder incl. all sub-folders, write all files paths to a output file <output_file_path>           
    def scan_folder_and_write_paths_to_file(self, folder_path_list, output_file_path):
        file_path_list = self.scan_folder_get_file_paths(folder_path_list)
        file_counter = 0
        time_entry = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(output_file_path, 'a') as output_file:
            output_file.write(f"{time_entry} scan folders:\n")
            for i in range(len(folder_path_list)):
                output_file.write(f"{folder_path_list[i]}: \n")
            output_file.write("Files: \n")
            for file_path in file_path_list:
                file_counter += 1
                output_file.write(file_path + '\n')
            output_file.write(f"Total files number: {file_counter}\n\n")
    
    # get all file paths from a folder incl. all sub-folders
    def scan_folder_get_file_paths(self, folder_path_list):
        file_path_list = []        
        for folder_path in folder_path_list:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_path_list.append(file_path)
        
        return file_path_list
   
    # check all files from a <folder_list>, which contain multiple folders (not inside of eachother as sub-folder) 
    # return file path which has duplicated names
    def check_for_duplicate_filenames(self, folder_path_list):
        if isinstance(folder_path_list, list):
            pass
        else:
            folder_path_list = [folder_path_list]
        
        # Dictionary to store file names and their paths
        filenames_dict = defaultdict(list)

        # Walk through each folder and its subfolders
        for folder in folder_path_list:
            for root, _, files in os.walk(folder):
                for file in files:
                    # Add the file path to the dictionary
                    filenames_dict[file].append(os.path.join(root, file))

        # Check for duplicates
        duplicates = {file: paths for file, paths in filenames_dict.items() if len(paths) > 1}
        return duplicates        

    # check all files from a <folder_list>, which contain multiple folders (not inside of eachother as sub-folder) 
    # return file path which has duplicated names
    def check_for_selected_duplicate_filenames(self, folder_path_list, dot_ext_name):
        if isinstance(folder_path_list, list):
            pass
        else:
            folder_path_list = [folder_path_list]
        
        # Dictionary to store file names and their paths
        filenames_dict = defaultdict(list)

        # Walk through each folder and its subfolders
        for folder in folder_path_list:
            for root, _, files in os.walk(folder):
                for file in files:
                    if file.endswith(dot_ext_name):
                    # Add the file path to the dictionary
                        filenames_dict[file].append(os.path.join(root, file))
                    else:
                        pass

        # Check for duplicates
        duplicates = {file: paths for file, paths in filenames_dict.items() if len(paths) > 1}
        return duplicates    

    # check if any file absence in src_folder files compare to des_folder
    def get_all_absence_selected_files(self, src_path, des_path, dot_ext_name):
        src_c_filenames = self.get_all_selected_file_names(src_path, dot_ext_name)
        des_c_filenames = self.get_all_selected_file_names(des_path, dot_ext_name)
        
        # if file(s) in des but not in src -> return collection of these file names
        # if file(s) in res but not in des -> return empty (not negative)
        # all other scenarios              -> return empty
        absent_files = des_c_filenames - src_c_filenames        
        return absent_files
    
    # put all files hashes from a src folder into a dict
    def get_selected_file_hash(self, src_folder_path, dot_ext_name):
        hashes = {}
        for root, dirs, files in os.walk(src_folder_path):
            for file_name in files:
                if file_name.endswith(dot_ext_name):
                    file_path = os.path.join(root, file_name)
                    file_hash = self.calculate_file_hash(file_path)
                    hashes[file_hash] = file_name
        return hashes
    
    def get_file_extension(self, file_name):
        return os.path.splitext(file_name)[1]
    
    # Compare the content of two files, if same, return <True>, else return <False>
    def compare_file_content(self, file1, file2):
        with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
            return f1.read() == f2.read()      
        
    def write_duplicates_to_file(self, duplicates, output_file_path):
        with open(output_file_path, 'w') as output_file:
            if duplicates:
                output_file.write("Duplicate file names found:\n")
                for file, paths in duplicates.items():
                    output_file.write(f"\nFile Name: {file}\n")
                    for path in paths:
                        output_file.write(f" - {path}\n")
                        # print(path)  # Print each path on a new line
                    
                    # Check if the contents of the files are the same
                    content_matched = all(self.compare_file_content(paths[0], p) for p in paths[1:])
                    output_file.write(f"Content matched: {'yes' if content_matched else 'no'}\n")
                    # print(f"Content matched: {'yes' if content_matched else 'no'}")
            else:
                output_file.write("No duplicate file names found.\n")
                # print("No duplicate file names found.")  # Print message if no duplicates found
     
    # copy <file_name> from <src_folder_path> to <des_folder_path>
    # if file_name doesn't exit or duplicated in <src_folder_path> -> cb_file_handler_list[0]
    # if file_name doesn't exit or duplicated in <des_folder_path> -> cb_file_handler_list[1]
    def copy_to_same_named_location(self, file_name, src_folder_path, des_folder_path, shortcut_path):                
        src_file_path = self.get_file_path(file_name, src_folder_path)
        des_file_path = self.get_file_path(file_name, des_folder_path)
        
        # check if file exist or duplicated in <src_file_path>
        if (src_file_path == 'not found') or (src_file_path == 'duplicates found'):            
            # print()
            # print("Error, file not found or duplicated files found in src path, copy failed!")
            pass
        else:            
            # Check for duplicate file names in the destination folder            
            if des_file_path == 'duplicates found':
                # print()
                # print("Error, duplicated files found in des path, copy failed!")
                pass
            elif des_file_path == 'not found':
                # print()
                # print("Error, duplicated files found in des path, copy failed!")
                pass
            else:                        
                # Copy the source file to the destination file path
                shutil.copy(src_file_path, des_file_path)
                short_src_file_path = str(src_file_path).replace(shortcut_path, '')
                short_des_file_path = str(des_file_path).replace(shortcut_path, '')
                
                text1 = "Copied .."   + short_src_file_path
                text2 = "to .."       + short_des_file_path
                self.print_fixed_len_txt(text1, 100, text2, 150)               

                               
    def get_folder_path(self, file_path):
        folder_path = os.path.dirname(file_path)
        return folder_path
                    
    def get_file_path(self, file_name, folder_path):
        single_file_path = None
        
        # List to store paths of files with the given name
        file_paths = []

        # Walk through the folder and its subfolders
        for root, _, files in os.walk(folder_path):
            if file_name in files:
                # Construct the full path of the file
                file_paths.append(os.path.join(root, file_name))

        # Check the number of files found
        if len(file_paths) == 0:
            # print(f"<{file_name}> file not found in {folder_path}")            
            single_file_path = 'not found'
        elif len(file_paths) > 1:
            for path in file_paths:
                pass
                # print(f"<{file_name}> duplicated files found in {path}")
            single_file_path = 'duplicates found'
        else:
            single_file_path = file_paths[0]
            
        return single_file_path      
    
    def get_all_selected_file_names(self, src_path, dot_ext_name:str):
        selected_files = set()
        for root, _, files in os.walk(src_path):
            for file in files:
                if file.endswith(dot_ext_name):
                    selected_files.add(file)
        return selected_files            
        
    def print_fixed_len_txt(self, txt1, len1, txt2, len2):
        if len(txt1) > len1:
            txt1 = txt1[:len1]
        else:
            txt1 = txt1.ljust(len1)
        
        if len(txt2) > len2:
            txt2 = txt2[:len2]
        else:
            txt2 = txt2.ljust(len2)
        
        print(f"{txt1} {txt2}")

    def get_fixed_len_txt(self, text:str, length:int):
        if len(text) > length:
            fix_len_text = text[:length]
        else:
            fix_len_text = text.ljust(length)
        
        return fix_len_text

    def format_fixed_len_data(self, text_data, field_length: int) -> str:
        formatted_data = []

        if isinstance(text_data, dict):
            # Format only values for a dictionary (ignoring keys)
            for value in text_data.values():
                fixed_value = self.get_fixed_len_txt(str(value), field_length)
                formatted_data.append(fixed_value)
        
        elif isinstance(text_data, list):
            # Format each element for a list
            for item in text_data:
                fixed_item = self.get_fixed_len_txt(str(item), field_length)
                formatted_data.append(fixed_item)
        
        elif isinstance(text_data, str):
            # Format the string with fixed length
            formatted_data.append(self.get_fixed_len_txt(text_data, field_length))
        
        else:
            # Handle any other data type by converting it to a string
            formatted_data.append(self.get_fixed_len_txt(str(text_data), field_length))
        
        # Concatenate all formatted data without adding any separator
        return "".join(formatted_data)   
        
    