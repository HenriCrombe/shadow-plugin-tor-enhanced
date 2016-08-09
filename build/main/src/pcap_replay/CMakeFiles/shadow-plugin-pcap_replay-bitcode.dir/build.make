# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/tor/shadow-plugin-tor

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/tor/shadow-plugin-tor/build/main

# Utility rule file for shadow-plugin-pcap_replay-bitcode.

# Include the progress variables for this target.
include src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay-bitcode.dir/progress.make

src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay-bitcode: src/pcap_replay/shadow-plugin-pcap_replay-bitcode.bc

src/pcap_replay/shadow-plugin-pcap_replay-bitcode.bc: src/pcap_replay/pcap_replay-main.c.bc
src/pcap_replay/shadow-plugin-pcap_replay-bitcode.bc: src/pcap_replay/pcap_replay.c.bc
	$(CMAKE_COMMAND) -E cmake_progress_report /home/tor/shadow-plugin-tor/build/main/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Linking LLVM bitcode shadow-plugin-pcap_replay-bitcode.bc"
	cd /home/tor/shadow-plugin-tor/build/main/src/pcap_replay && /usr/bin/llvm-link -o /home/tor/shadow-plugin-tor/build/main/src/pcap_replay/shadow-plugin-pcap_replay-bitcode.bc pcap_replay-main.c.bc pcap_replay.c.bc

src/pcap_replay/pcap_replay-main.c.bc: ../../src/pcap_replay/pcap_replay-main.c
src/pcap_replay/pcap_replay-main.c.bc: ../../src/pcap_replay/pcap_replay-main.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/tor/shadow-plugin-tor/build/main/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Building LLVM bitcode pcap_replay-main.c.bc"
	cd /home/tor/shadow-plugin-tor/build/main/src/pcap_replay && /usr/bin/clang -emit-llvm -DDEBUG -g -fno-inline -fno-strict-aliasing -Wno-unknown-attributes -Wno-unused-command-line-argument -Wno-unknown-warning-option -fPIC -fno-inline -fno-strict-aliasing -U_FORTIFY_SOURCE -lpcap -I/home/tor/.shadow/include -I/home/tor/.shadow/share/cmake/Modules -I/home/tor/shadow-plugin-tor/cmake -I/home/tor/.shadow/include -I/home/tor/.shadow/include/glib-2.0 -I/home/tor/.shadow/lib/glib-2.0/include -c /home/tor/shadow-plugin-tor/src/pcap_replay/pcap_replay-main.c -o pcap_replay-main.c.bc

src/pcap_replay/pcap_replay.c.bc: ../../src/pcap_replay/pcap_replay.c
src/pcap_replay/pcap_replay.c.bc: ../../src/pcap_replay/pcap_replay.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/tor/shadow-plugin-tor/build/main/CMakeFiles $(CMAKE_PROGRESS_3)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Building LLVM bitcode pcap_replay.c.bc"
	cd /home/tor/shadow-plugin-tor/build/main/src/pcap_replay && /usr/bin/clang -emit-llvm -DDEBUG -g -fno-inline -fno-strict-aliasing -Wno-unknown-attributes -Wno-unused-command-line-argument -Wno-unknown-warning-option -fPIC -fno-inline -fno-strict-aliasing -U_FORTIFY_SOURCE -lpcap -I/home/tor/.shadow/include -I/home/tor/.shadow/share/cmake/Modules -I/home/tor/shadow-plugin-tor/cmake -I/home/tor/.shadow/include -I/home/tor/.shadow/include/glib-2.0 -I/home/tor/.shadow/lib/glib-2.0/include -c /home/tor/shadow-plugin-tor/src/pcap_replay/pcap_replay.c -o pcap_replay.c.bc

shadow-plugin-pcap_replay-bitcode: src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay-bitcode
shadow-plugin-pcap_replay-bitcode: src/pcap_replay/shadow-plugin-pcap_replay-bitcode.bc
shadow-plugin-pcap_replay-bitcode: src/pcap_replay/pcap_replay-main.c.bc
shadow-plugin-pcap_replay-bitcode: src/pcap_replay/pcap_replay.c.bc
shadow-plugin-pcap_replay-bitcode: src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay-bitcode.dir/build.make
.PHONY : shadow-plugin-pcap_replay-bitcode

# Rule to build all files generated by this target.
src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay-bitcode.dir/build: shadow-plugin-pcap_replay-bitcode
.PHONY : src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay-bitcode.dir/build

src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay-bitcode.dir/clean:
	cd /home/tor/shadow-plugin-tor/build/main/src/pcap_replay && $(CMAKE_COMMAND) -P CMakeFiles/shadow-plugin-pcap_replay-bitcode.dir/cmake_clean.cmake
.PHONY : src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay-bitcode.dir/clean

src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay-bitcode.dir/depend:
	cd /home/tor/shadow-plugin-tor/build/main && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/tor/shadow-plugin-tor /home/tor/shadow-plugin-tor/src/pcap_replay /home/tor/shadow-plugin-tor/build/main /home/tor/shadow-plugin-tor/build/main/src/pcap_replay /home/tor/shadow-plugin-tor/build/main/src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay-bitcode.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay-bitcode.dir/depend

