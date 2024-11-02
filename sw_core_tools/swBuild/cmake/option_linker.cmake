# all project paths defined in project_path.cmake
include("${CMAKE_SOURCE_DIR}/project_config.cmake")

set (project_linker_option "")
list(APPEND project_linker_option
    "-Wl-o${sw_name}.hex:IHEX:4"    # here is another suckass makefile syntax, if you write -Wl -o with an empty space, it will not work!!!
    "-Wl-o${sw_name}.sre:SREC:4"
    "--hex-format=s"

    "-Ctc36x"
    
    "--lsl-core=vtc"
    "--lsl-file=${project_linker_script}"
    # "--verbose"                   # usually, don't activate --verbose for linker 

    # CAUTION:
    # There are bunch of "external" tasking libraries locate here:
    # C:\_SoftwareBuildSetup\Tasking\TriCoreV6.2r2p2AddOnV2\ctc\lib\tc162
    # because we define it in toolchain.cmake
    # set(CMAKE_C_COMPILER "C:/_SoftwareBuildSetup/Tasking/TriCoreV6.2r2p2AddOnV2/ctc/bin/cctc.exe" CACHE PATH "TASKING CTC")
    # the cctc.exe seemed looking for "default" library from pre-installed tasking root folder automatically
    # if you change some library name, like libcs_fpu.a -> noname.a, the linker will report error
)

# Join the linker flags into a single string
string(JOIN " " FULL_LINK_FLAGS ${project_linker_option})

