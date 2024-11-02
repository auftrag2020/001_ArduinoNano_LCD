cmake_minimum_required(VERSION 3.30)

# all project paths defined in project_path.cmake
include("${CMAKE_SOURCE_DIR}/project_config.cmake")

# Include the compiler/assembler/linker options
include("${CMAKE_SOURCE_DIR}/option_compiler.cmake")
include("${CMAKE_SOURCE_DIR}/option_assembler.cmake")
include("${CMAKE_SOURCE_DIR}/option_linker.cmake")

message(STATUS "----------------------------------------------------------")
# Print the project root directory (optional, for debugging)
message(STATUS "Project root directory: ${PROJECT_ROOT_DIR}")
# Print the project sw output name (optional, for debugging)
message(STATUS "Project sw product name: ${sw_name}")
message(STATUS "----------------------------------------------------------")

project(${project_name})

# set(CMAKE_VERBOSE_MAKEFILE OFF)

# add all .c files to target <sw_product>
add_executable(             "${sw_product}" ${project_source})

# define all libraries to target <sw_product>
target_include_directories( "${sw_product}" PRIVATE ${project_include} )

# define all linker options to target <sw_product>
set_target_properties(      "${sw_product}" PROPERTIES LINK_FLAGS       ${FULL_LINK_FLAGS}) 

# Very tricky CMake<->Taskingincompatible problem
# Cmake generated the *.rsp file always using @ but this is not accepted by tasking compiler. 
# Tasking compiler expects -f instead of @. So, to read *.rsp file add
# See https://discourse.cmake.org/t/tasking-compiler-linking-error-cctc-e205-don-t-know-what-to-do-with-cmakefiles-sample-rsp/5110
set(CMAKE_C_RESPONSE_FILE_LINK_FLAG "-f")

