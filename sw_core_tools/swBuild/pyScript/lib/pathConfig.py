# the DOT is very important here!!!
from .fileHelper import FileHelper

class Path_Project:
    def __init__(self):
        self.fileHelper = FileHelper()
        
        # define top level directories
        self.project_path       = self.fileHelper.get_upLevel_path(4)  
        self.sw_core_tools_path = self.fileHelper.get_upLevel_path(3)
        self.swBuild_path       = self.fileHelper.get_upLevel_path(2) 
        
        
        # define project build path
        self.project_build_path                 = self.project_path                 + "\\build"    
        
        self.project_build_include_path         = self.project_build_path           + "\\include"
        self.project_build_source_path          = self.project_build_path           + "\\source"
        
        self.project_build_product_path         = self.project_build_path           + "\\product"
        self.project_build_product_cache_path   = self.project_build_product_path   + "\\cache"
        
        self.project_build_debug_path           = self.project_build_path           + "\\debug"
        self.project_build_debug_cache_path     = self.project_build_debug_path     + "\\cache"        
       
        # define cmake tools path
        self.cmake_bin_path = self.sw_core_tools_path   + "\\cmake-3.30.4-windows-x86_64\\bin"
        self.cmake_exe      = self.cmake_bin_path       + "\\cmake.exe"
        
        self.cmake_path  = self.swBuild_path        + "\\cmake"
        self.CMakeLists  = self.cmake_path          + "\\CMakeLists.txt"
        self.toolchain   = self.cmake_path          + "\\toolchain.cmake"
        # self.compiler    = self.cmake_path          + "\\compiler_config.cmake"        

        # define ninja tools path
        self.ninja_path = self.sw_core_tools_path   + "\\ninja"
        self.ninja_exe  = self.ninja_path           + "\\ninja.exe"
        
        
        # define src/inc folder paths
        self.project_bk_path     = self.project_path + "\\bk" 
        self.project_var_path    = self.project_path + "\\var" 

        self.project_libraries      = self.project_path + "\\Libraries" 
        self.project_configurations = self.project_path + "\\Configurations" 


        self.product_ext_name_list = [  ".elf", 
                                        ".map", 
                                        ".hex",
                                        ".mdf",
                                        ".bin",
                                        ".sre"]

# Path_Tasking is not used yet
class Path_Tasking:
    def __init__(self):
        
        #define tasking toolchain path
        self.folder_bin = "C:\\_SoftwareBuildSetup\\Tasking\\TriCoreV6.2r2p2AddOnV2\\ctc\\bin"
        self.control        = self.folder_bin + "\\cctc.exe"
        self.compiler_c     = self.folder_bin + "\\ctc.exe"
        self.make           = self.folder_bin + "\\amk.exe"
        self.archiver       = self.folder_bin + "\\artc.exe"
        # self.compiler_cpp   = self.folder_bin + "\\cptc.exe"      # not used
        
        self.assembler      = self.folder_bin + "\\astc.exe"
        # self.seembler_old   = self.folder_bin + "\\mktc.exe"      # obsoleted
        
        self.linker         = self.folder_bin + "\\ltc.exe"
                
        # self.elf_dump       = self.folder_bin + "\\elfdump.exe"
        # self.elf_patch      = self.folder_bin + "\\elfpatch.exe"
        # self.elf_size       = self.folder_bin + "\\elfsize.exe"
        
        # self.expire_cache   = self.folder_bin + "\\expiretc.exe"
        # self.HLL_dump       = self.folder_bin + "\\hldumptc.exe"
        # self.safety_checker = self.folder_bin + "\\ichk.exe"   # no license
        # self.profiling      = self.folder_bin + "\\proftool.exe"
        pass
        
        
class Path_Src:
    def __init__(self):
        
        pass