# Determine the current directory
set(CURRENT_DIR ${CMAKE_SOURCE_DIR})

# WARNING - This setup is required cmake file locates in a directory under 2-level of project root
# e.g.  project_root/sw_core_tools/swBuild/cmake
# if you change the cmake folder place, the <NUM_LEVELS_UP> must be aligned
set(NUM_LEVELS_UP 2)

# Initialize the PROJECT_ROOT_DIR with the CURRENT_DIR
set(PROJECT_ROOT_DIR ${CURRENT_DIR})
# Loop to move up the directory hierarchy
foreach(i RANGE ${NUM_LEVELS_UP})
    get_filename_component(PROJECT_ROOT_DIR ${PROJECT_ROOT_DIR} DIRECTORY)
endforeach()

