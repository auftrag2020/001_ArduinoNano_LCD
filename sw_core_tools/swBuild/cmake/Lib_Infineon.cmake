include("${CMAKE_SOURCE_DIR}/Lib_Root.cmake")

# CAUTION: very tricky configuration here!!!    
# We need to add extra Infineon Libs to project include path, only the .h directories is not enough
# Reason: Many #include path in iLLD have contain relative path, 
# if only header files directories are included, the compiler cannot find the header files
# We must try to keept the #include path as CLEAN as possible, don't use relative path anymore!!!
set(LIB_Infineon "${PROJECT_ROOT_DIR}/var/07_Lib/Infineon")
set(LIB_Infineon_reldirs
# define all necessary infineon relative lib path
    "${LIB_Infineon}/Libraries/iLLD/TC36A"
    "${LIB_Infineon}/Libraries/iLLD/TC36A/Tricore"
    
    "${LIB_Infineon}/Libraries/Infra/Platform"
    "${LIB_Infineon}/Libraries/Infra/Platform/Ssw/TC36A"
    "${LIB_Infineon}/Libraries/Infra/Platform/Ssw/TC36A/Tricore"
    "${LIB_Infineon}/Libraries/Service/CpuGeneric"
    "${LIB_Infineon}/Configurations"    
)