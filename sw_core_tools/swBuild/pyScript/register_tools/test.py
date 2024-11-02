import sys
import os
import re

lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the lib directory to the Python path
sys.path.append(lib_path)

from lib.pathConfig import *
from lib.fileHelper import *

from registerFile import *
from registerTools import *

fileHelper = FileHelper()
regFile = Register_File()

regdef_EVADC_path = regFile.TC36x_Evadc_regdef_file

regTools_EVADC = Register_Tools(regdef_EVADC_path)

def print_module(module:dict):
    print(module['module_name'])
    print(fileHelper.format_fixed_len_data(module['titles'], 30))
    for each in module['members']:
        print(fileHelper.format_fixed_len_data(each, 30))    

def main():

    # evadc_reg_file_path      = regFile.TC36x_Evadc_reg_file
    evadc_regdef_file_path   = regFile.TC36x_Evadc_regdef_file
    output_file_path         = regFile.output_file_path    

    # print_module()
    
    # regdef1 = regTools_EVADC.get_reg_typedef("Ifx_EVADC_G")
    # regdef2 = regTools_EVADC.get_reg_typedef("Ifx_EVADC_CLC_Bits")    
    # print(regdef1)    
    # print(regdef2)

    # root_reg = regTools_EVADC.get_root_reg()
    # root_reg_extraction = regTools_EVADC.extract_root_reg(root_reg, 0)

    root_reg_type = regTools_EVADC.get_root_reg_type()    
        
    root_reg_data = regTools_EVADC.get_reg_data(root_reg_type)    
    print_module(root_reg_data)
    
    root_reg_extraction = regTools_EVADC.extract_root_reg(root_reg_data, 0)
    print_module(root_reg_extraction)   
    
    # extract_depth_list = [0]
    # is_recursive_needed = [True]
    # root_reg_extraction_recursive = regTools_EVADC.extract_root_reg_recursive(root_reg_data, extract_depth_list, is_recursive_needed)    
    # print_module(root_reg_data)s

main()