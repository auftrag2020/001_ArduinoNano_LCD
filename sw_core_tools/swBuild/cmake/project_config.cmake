include("${CMAKE_SOURCE_DIR}/Lib_Root.cmake")
# include("${CMAKE_SOURCE_DIR}/Lib_Infineon.cmake")
# include("${CMAKE_SOURCE_DIR}/Lib_Proj_sdk.cmake")
include("${CMAKE_SOURCE_DIR}/Lib_Proj_var.cmake")

# include("${CMAKE_SOURCE_DIR}/Lib_Exclude.cmake")
include("${CMAKE_SOURCE_DIR}/function.cmake")

# define project variables
set(project_name    "001_ArduinoNano_LCD")
set(sw_version      "A01")
set(sw_name         "${project_name}_${sw_version}")
set(sw_product      "${project_name}_${sw_version}.elf")

# Define the directories to exclude
# set(project_exlcude_dirs
#     ${exclude_01_AppLyr}
#     ${exclude_02_Rte}
#     ${exclude_03_SrvLyr}
#     ${exclude_04_EcuAbLyr}
#     ${exclude_05_McuAbLyr}
#     ${exclude_06_CmplxDrv}
# )

filter_out_exclude_dirs(proj_var_c_files proj_var_c_files_filtered "${project_exlcude_dirs}")

# only for debug
# foreach(dirs IN LISTS proj_var_c_files_filtered)
#     message(STATUS ${dirs})    
# endforeach()

set(project_source
    ${proj_var_c_files}
    # ${proj_var_c_files_filtered}
)

# include all subdirectories for header files
set(project_include
    ${LIB_var_subdirs_unique}   # no duplicated directories
    # ${LIB_Infineon_reldirs}     # some iLLD components have relative #include path, e.g. #include "EVADC/Ifx_Adc.h"
)

# set(project_linker_script
#     "${PROJECT_ROOT_DIR}/var/09_Startup/Linker/Lcf_Tasking_Tricore_Tc.lsl"
# )