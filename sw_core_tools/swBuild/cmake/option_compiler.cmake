#define project compiler flags
# set (project_c_compiler_flags "")
list(APPEND project_c_compiler_flags
    "--align=0"                     # default value 0
    # --branch-target-align
    # --cache
    # --cert
    # --check
    "--core=tc1.6.2"
    # --code-core-association=share"

    "--optimize=0"              # default value 2 - No optimization for better debugging
    "--default-near-size=0"     # default value 8 - CAUTION: the most badass trick all the time!!! with default value 8, linking error
                                # https://community.infineon.com/t5/AURIX/syntax-error-absolute-location-in-memory-for-group-does-not-map-to-space-mpe-vtc/td-p/398596
    "--default-a0-size=0"       # default value 0
    "--default-a1-size=0"       # default value 0

    "--debug-info=all"          # it must be set as all, otherwise debugger will not get full symbol information

    "--integer-enumeration"     # CAUTION: Normally the compiler treats enumerated types as the smallest data type possible 
                                # (char or short instead of int).
                                # if this compiler option not defined, the size of enum variables will be 1-byte, it will cause
                                # big pointer address alignment problem

    # "--define=__TASKING__=1"

    # "--define=__CPU__=tc36x"
    # "-Wa-Hsfr/regtc36x.def"
    # "-Hsfr/regtc36x.sfr"

    # "--verbose"               # detail compiling information 
    "--tradeoff=0"               # default value 4
    # "--warnings-as-errors"
)

# Join the linker flags into a single string
string(JOIN " " FULL_COMPILER_FLAGS ${project_c_compiler_flags})

set(CMAKE_C_FLAGS ${FULL_COMPILER_FLAGS})