import sys
import os
import re

lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the lib directory to the Python path
sys.path.append(lib_path)

from lib.pathConfig import *
from lib.fileHelper import *

class Register_File:
    def __init__(self):
        self.pathConfig = Path_Project()
        self.fileHelper = FileHelper()
        self.output_file_path = self.pathConfig.project_build_path + r"\RegisterMap\RegisterMap.xlsx"
        self.TC36x_register_root_path   = self.pathConfig.project_var_path + r"\07_Lib\Infineon\Libraries\Infra\Sfr\TC36A\_Reg"
        self.TC36x_Evadc_reg_file       = self.TC36x_register_root_path + r"\IfxEvadc_reg.h"
        self.TC36x_Evadc_regdef_file    = self.TC36x_register_root_path + r"\IfxEvadc_regdef.h"      
    
    def count_registers_in_files(self, folder_path):
        register_pattern = re.compile(r'\(\*.*0x[0-9A-Fa-f]+u\)')
        
        for file_name in os.listdir(folder_path):
            if file_name.endswith('_reg.h'):
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'r') as file:
                    content = file.read()
                    
                    # Count occurrences of the register pattern
                    register_count = len(register_pattern.findall(content))                    
                    self.fileHelper.print_fixed_len_txt(f"{file_name}", 30, f"Total number: {register_count}", 20)                                     
    
    def extract_registers_and_addresses(self, folder_path):
        register_pattern = re.compile(r'#define\s+(\w+)\s+\/\*.*\(\*.*(0x[0-9A-Fa-f]+u)\)')

        for file_name in os.listdir(folder_path):
            if file_name.endswith('_reg.h'):
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'r') as file:
                    content = file.read()
                    
                    # Find all matches of the register pattern
                    matches = register_pattern.findall(content)
                    
                    # Print the file name and the total count
                    self.fileHelper.print_fixed_len_txt(f"{file_name}", 30, f"Total number: {len(matches)}", 20)
                    
                    # Print each register and its address
                    for match in matches:
                        register_name, register_address = match
                        self.fileHelper.print_fixed_len_txt(f"{register_name}", 30, register_address, 20)                                        
                    print("\n")
                    


        