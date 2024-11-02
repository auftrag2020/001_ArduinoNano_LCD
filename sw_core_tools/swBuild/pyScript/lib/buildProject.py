# the DOT is very important here!!!
import subprocess
from .fileHelper import FileHelper
from .pathConfig import Path_Project
from colorama import init, Fore, Style

class Build_Project:
    def __init__(self):
        self.fileHelper = FileHelper()
        self.prjPathConfig = Path_Project()
        
        self.output_path_dict = self.get_output_path()
    
    def get_output_path(self):
        # init an empyt dict for output paths as dict
        output_path_dict = {'cache'     :"", 
                            'product'   :""}
        
        output_path_dict['cache']    = self.prjPathConfig.project_build_product_cache_path
        output_path_dict['product']  = self.prjPathConfig.project_build_product_path

        return output_path_dict
    
    def build_process(self, step:int, process_name:str, prev_job_status:list, cb_job):
        self.build_process_start_printout(step, process_name, prev_job_status[0])
        local_previous_job_status = prev_job_status[0]  # previous job status is recorded before it got changed
        if prev_job_status[0] == "OK":
            prev_job_status[0] = cb_job()           # job status is updated and will be sent out to next job handler
        else:                                       # if previous job is not ok, all next jobs will be aborted
            prev_job_status[0] = "NOK"              # job status is updated and will be sent out to next job handler
        local_current_job_status = prev_job_status[0]
        self.build_process_result_printout(step, process_name, local_previous_job_status, local_current_job_status)
    
    # define all jobs for build
    def job_check_duplicates_in_var(self):
    # any duplicates .h/.c in var is prohibitted
        job_status = ""        
        duplicates = {} #init a dict
        
        print("Check duplicated .h/.c in var folders - Duplicates are prohibitted!")
        duplicates.update(self.fileHelper.check_for_selected_duplicate_filenames(self.prjPathConfig.project_var_path, ".c"))
        duplicates.update(self.fileHelper.check_for_selected_duplicate_filenames(self.prjPathConfig.project_var_path, ".h"))

        if duplicates:          # Duplicates found
            for file, paths in duplicates.items():
                print(f"{Fore.RED}File Name: {file} have duplicates{Fore.RESET}")
                for path in paths:
                    print(f" - {path}")
            job_status = "NOK"
        else:
            print("No duplicates .h/.c files was found in var")
            job_status = "OK"
        return job_status

    def job_incrementBuild_startup(self):
    # print build startup info - increment build
        job_status = ""
        print("Start increment building project")
        job_status = "OK"
        return job_status 
        
    def job_completetBuild_startup(self):
    # print build startup info - complete build        
        job_status = ""
        print("Start complete building project")
        # To-Do: it would be nice to consider the fileHelper function status
        print("Clean all files in build (incl. cache folder)")
        self.fileHelper.clean_folder(self.prjPathConfig.project_build_path)
        job_status = "OK"
        return job_status       
    
    def job_cmake(self):
        # use cmake.exe to generate makefiles for ninja
        job_status = ""            
        returncode = self.cmake_build(self.get_output_path()['cache'])        
        if returncode == 0:     # returncode is an attribute from subprocess.run, 0 means process ok
            job_status = "OK"
        else:
            job_status = "NOK"
        return job_status        
    
    def job_ninja(self):
        # use ninja.exe to build project
        job_status = ""            
        returncode = self.ninja_build(self.get_output_path()['cache'])                
        if returncode == 0:     # returncode is an attribute from subprocess.run, 0 means process ok
            job_status = "OK"
        else:
            job_status = "NOK"        
            print()
        return job_status        

    def job_output_product(self):
        # copy relevant output files (.elf/.hex/.map...) to product folder        
        job_status = ""
        for ext_name in self.prjPathConfig.product_ext_name_list:
            self.fileHelper.copy_all_files(self.get_output_path()['cache'], self.get_output_path()['product'], ext_name, self.prjPathConfig.project_build_path)               
        job_status = "OK"
        return job_status                        
   
    def cmake_build(self, output_path):
    # cmake is using for generate executable makefile to build  
        status = [] # list is mutable, like pointer variable in c, play a roll for in/out paramter
        command = [
            self.prjPathConfig.cmake_exe,
            f"-DCMAKE_TOOLCHAIN_FILE={self.prjPathConfig.toolchain}",
            f"-S{self.prjPathConfig.cmake_path}",                       #-S is where CMakeLists.txt locates, not for .h/.c files!!!
            f"-B{output_path}",                                         #-B is where build output with many overbloated cache files
            "-DCMAKE_VERBOSE_MAKEFILE=OFF",                             # this must be set as off, otherwise huge amount compiler -I flags over flooded terminal screen
            "-G Ninja",
            f"-DCMAKE_MAKE_PROGRAM={self.prjPathConfig.ninja_exe}"      # Explicitly set the path to ninja.exe
        ]            
        self.run_command(command, "CMake", status)
        return status[0]
        
    def ninja_build(self, output_path):       
    # ninja is using for build final output files (elf, hex, map...) due to existing makefile
        status = [] # list is mutable, like pointer variable in c, play a roll for in/out paramter
        command = [
            self.prjPathConfig.ninja_exe,
            "-C", output_path,
            # "-v"
            # "--quiet"
            # "-w dupbuild=warn"
        ]                    
        self.run_command(command, "Ninja", status)        
        return status[0]

    def run_command(self, command, command_name:str, status:list):
        print(f"Running: {command[0]}")
        print("\n".join(command))
        
        # if status is empty,       add a value 1 
        # if status is not empty,   always replace first element in status with 1
        # all none zero number in status means process failed
        status[0] = 1 if status else status.append(1)
        
        try:
            result = subprocess.run(command, check=True)
            # result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(f"{command_name} launch successful!")
            status[0] = result.returncode # CAUTION: only the first element of list is used
            # print(result.stdout)
            # print(result.stderr)
        except subprocess.CalledProcessError as e:
            print(f"{command_name} launch failed!")
            status[0] = e.returncode # all non-zero means subprocess failed
            print("Error code is: ", status[0])
            # print("Output:", e.stdout)
            # print("Errors:", e.stderr)
        except PermissionError as e:
            print("Permission error! Try running the script with elevated permissions.")
            status[0] = e.errno # [Errno 13] Permission denied
            print("Error code is: ", status[0])
            # print("Error message:", e)       

    def build_process_start_printout(self, step, process_name, previous_status):
        if previous_status == "OK":
            print(f"Build_process {step} - {process_name} is started...")
        else:
            # do nonting, because previous process already failed
            pass

    def build_process_result_printout(self, step, process_name, previous_status, current_build_status):
        if previous_status == "OK":            
            if current_build_status == "OK":
                print(f"{Fore.GREEN}Build process {step} - {process_name} succeed{Fore.RESET}")
            else:
                print(f"{Fore.RED}Build process {step} - {process_name} failed{Fore.RESET}")
        else:
            print(f"{Fore.RED}Previous process failed, build process {step} - {process_name} aborted{Fore.RESET}")
            pass    
        # print split line
        print("----------------------------------------------------------------------------------------------")
        print()
        print("----------------------------------------------------------------------------------------------")

    def run(self, build_mode):
        previous_status = ["OK"]
        
        if build_mode == "increment":
            self.build_process(1, "increment build startup",    previous_status, self.job_incrementBuild_startup)
        elif build_mode == "complete":
            self.build_process(1, "complete build startup",     previous_status, self.job_completetBuild_startup)
        else:
            previous_status = ["NOK"]
            print("Error, invalid build mode input. Valid build mode: <-i>|<-c>")
            
        self.build_process(2, "check duplicates in var",    previous_status, self.job_check_duplicates_in_var)                
        self.build_process(3, "cmake",                      previous_status, self.job_cmake)
        self.build_process(4, "ninja",                      previous_status, self.job_ninja)
        self.build_process(5, "output product files",       previous_status, self.job_output_product)    
            
        if previous_status[0] == "OK":
            print(f"{Fore.GREEN}Congratulation, all build processes succeed, have a nice day!{Fore.RESET}")
        else: 
            print(f"{Fore.RED}Unfortunately, build process failed, please fix problem and try again...{Fore.RESET}")        
