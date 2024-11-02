# Why Use Generic?
# Custom Platforms: When you are targeting a custom platform or an embedded system that does not match standard operating systems.
# Experimental Builds: When you are experimenting with new or unconventional build environments where predefined CMake configurations might interfere.
# Minimal Configurations: When you want to avoid any automatic configurations that CMake might apply for known systems and prefer to specify everything manually.
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR TC162)
set(CMAKE_C_COMPILER_WORKS TRUE CACHE INTERNAL "")

set(CMAKE_C_COMPILER_FORCED TRUE CACHE INTERNAL "")
set(CMAKE_C_COMPILER_ID_RUN TRUE CACHE INTERNAL "")

set(CMAKE_CXX_COMPILER_WORKS TRUE CACHE INTERNAL "")
set(CMAKE_CXX_COMPILER_FORCED TRUE CACHE INTERNAL "")
set(CMAKE_CXX_COMPILER_ID_RUN TRUE CACHE INTERNAL "")

set(CMAKE_C_COMPILER            "C:/_SoftwareBuildSetup/Tasking/TriCoreV6.2r2p2AddOnV2/ctc/bin/cctc.exe" CACHE PATH "TASKING CTC")
set(CMAKE_CXX_COMPILER          "C:/_SoftwareBuildSetup/Tasking/TriCoreV6.2r2p2AddOnV2/ctc/bin/cctc.exe" CACHE PATH "TASKING CC")

