include("${CMAKE_SOURCE_DIR}/Lib_Root.cmake")

include("${CMAKE_SOURCE_DIR}/function.cmake")

# define var source folder path
set(var_path    "${PROJECT_ROOT_DIR}/var")

# This will collect all .c files in bk
file(GLOB_RECURSE  proj_var_c_files
    "${PROJECT_ROOT_DIR}/var/*.c"
)

# Set the base directory containing the headers
set(var_include_dir "${PROJECT_ROOT_DIR}/var")

# Gather all header files recursively
# CAUTION: in this step, there will be many duplicated dir names added into the list
# the duplicates must be deleted after then, otherwise it will waste time for ninja searching include paths 
file(GLOB_RECURSE HEADER_FILES "${var_include_dir}/*.h")
# Extract the directories from all header files
set(LIB_var_subdirs "")
foreach(header_file ${HEADER_FILES})
    get_filename_component(header_dir ${header_file} DIRECTORY)
    list(APPEND LIB_var_subdirs "${header_dir}")
endforeach()


# Remove duplicates from LIB_var_subdirs
remove_duplicates(LIB_var_subdirs LIB_var_subdirs_unique)

# only for debug - print out on terminal
# foreach(DIR IN LISTS LIB_var_subdirs_unique)
#     message(STATUS "${DIR}")
# endforeach()