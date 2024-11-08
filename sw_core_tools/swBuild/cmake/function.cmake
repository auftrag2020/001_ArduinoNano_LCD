# Function to filter out files from multiple directories
function(filter_out_exclude_dirs input_list output_list exclude_dirs)
    set(result "")
    foreach(file IN LISTS ${input_list})
        set(exclude_file FALSE)
        foreach(exclude_dir IN LISTS exclude_dirs)
            if(file MATCHES "^${exclude_dir}.*")
                set(exclude_file TRUE)
                break()
            endif()
        endforeach()
        if(NOT exclude_file)
            list(APPEND result "${file}")
        endif()
    endforeach()
    set(${output_list} "${result}" PARENT_SCOPE)
endfunction()

# Helper function to filter out files from the exclude directory
function(filter_out_exclude_dir input_list output_list exclude_dir)
    set(result "")
    foreach(file IN LISTS ${input_list})
        if(NOT file MATCHES "^${exclude_dir}.*")
            list(APPEND result "${file}")
        endif()
    endforeach()
    set(${output_list} "${result}" PARENT_SCOPE)
endfunction()

# Helper function to remove duplicates from a list
function(remove_duplicates input_list output_list)
    set(seen "")
    set(result "")
    foreach(item IN LISTS ${input_list})
        if(NOT "${item}" IN_LIST seen)
            list(APPEND seen "${item}")
            list(APPEND result "${item}")
        endif()
    endforeach()
    set(${output_list} "${result}" PARENT_SCOPE)
endfunction()