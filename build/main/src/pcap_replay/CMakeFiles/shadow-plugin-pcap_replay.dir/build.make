# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.2

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
CMAKE_SOURCE_DIR = /home/blik/shadow-plugin-tor-enhanced

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/blik/shadow-plugin-tor-enhanced/build/main

# Include any dependencies generated for this target.
include src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/depend.make

# Include the progress variables for this target.
include src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/progress.make

# Include the compile flags for this target's objects.
include src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/flags.make

src/pcap_replay/shadow-plugin-pcap_replay.hoisted.bc: src/pcap_replay/shadow-plugin-pcap_replay.bc
src/pcap_replay/shadow-plugin-pcap_replay.hoisted.bc: /home/blik/.shadow/lib/LLVMHoistGlobals.so
	$(CMAKE_COMMAND) -E cmake_progress_report /home/blik/shadow-plugin-tor-enhanced/build/main/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Hoisting globals from shadow-plugin-pcap_replay.bc to shadow-plugin-pcap_replay.hoisted.bc"
	cd /home/blik/shadow-plugin-tor-enhanced/build/main/src/pcap_replay && /usr/bin/opt -load=/home/blik/.shadow/lib/LLVMHoistGlobals.so -hoist-globals shadow-plugin-pcap_replay.bc -o shadow-plugin-pcap_replay.hoisted.bc

src/pcap_replay/shadow-plugin-pcap_replay.bc: src/pcap_replay/shadow-plugin-pcap_replay-bitcode.bc
	$(CMAKE_COMMAND) -E cmake_progress_report /home/blik/shadow-plugin-tor-enhanced/build/main/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Linking LLVM bitcode shadow-plugin-pcap_replay.bc"
	cd /home/blik/shadow-plugin-tor-enhanced/build/main/src/pcap_replay && /usr/bin/llvm-link -o shadow-plugin-pcap_replay.bc /home/blik/shadow-plugin-tor-enhanced/build/main/src/pcap_replay/shadow-plugin-pcap_replay-bitcode.bc

src/pcap_replay/shadow-plugin-pcap_replay-bitcode.bc: src/pcap_replay/pcap_replay-main.c.bc
src/pcap_replay/shadow-plugin-pcap_replay-bitcode.bc: src/pcap_replay/pcap_replay.c.bc
	$(CMAKE_COMMAND) -E cmake_progress_report /home/blik/shadow-plugin-tor-enhanced/build/main/CMakeFiles $(CMAKE_PROGRESS_3)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Linking LLVM bitcode shadow-plugin-pcap_replay-bitcode.bc"
	cd /home/blik/shadow-plugin-tor-enhanced/build/main/src/pcap_replay && /usr/bin/llvm-link -o /home/blik/shadow-plugin-tor-enhanced/build/main/src/pcap_replay/shadow-plugin-pcap_replay-bitcode.bc pcap_replay-main.c.bc pcap_replay.c.bc

src/pcap_replay/pcap_replay-main.c.bc: ../../src/pcap_replay/pcap_replay-main.c
src/pcap_replay/pcap_replay-main.c.bc: ../../src/pcap_replay/pcap_replay-main.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/blik/shadow-plugin-tor-enhanced/build/main/CMakeFiles $(CMAKE_PROGRESS_4)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Building LLVM bitcode pcap_replay-main.c.bc"
	cd /home/blik/shadow-plugin-tor-enhanced/build/main/src/pcap_replay && /usr/bin/clang -emit-llvm -DDEBUG -g -fno-inline -fno-strict-aliasing -Wno-unknown-attributes -Wno-unused-command-line-argument -Wno-unknown-warning-option -fPIC -fno-inline -fno-strict-aliasing -U_FORTIFY_SOURCE -lpcap -I/home/blik/.shadow/include -I/home/blik/.shadow/share/cmake/Modules -I/home/blik/shadow-plugin-tor-enhanced/cmake -I/home/blik/.shadow/include -I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include -c /home/blik/shadow-plugin-tor-enhanced/src/pcap_replay/pcap_replay-main.c -o pcap_replay-main.c.bc

src/pcap_replay/pcap_replay.c.bc: ../../src/pcap_replay/pcap_replay.c
src/pcap_replay/pcap_replay.c.bc: ../../src/pcap_replay/pcap_replay.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/blik/shadow-plugin-tor-enhanced/build/main/CMakeFiles $(CMAKE_PROGRESS_5)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Building LLVM bitcode pcap_replay.c.bc"
	cd /home/blik/shadow-plugin-tor-enhanced/build/main/src/pcap_replay && /usr/bin/clang -emit-llvm -DDEBUG -g -fno-inline -fno-strict-aliasing -Wno-unknown-attributes -Wno-unused-command-line-argument -Wno-unknown-warning-option -fPIC -fno-inline -fno-strict-aliasing -U_FORTIFY_SOURCE -lpcap -I/home/blik/.shadow/include -I/home/blik/.shadow/share/cmake/Modules -I/home/blik/shadow-plugin-tor-enhanced/cmake -I/home/blik/.shadow/include -I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include -c /home/blik/shadow-plugin-tor-enhanced/src/pcap_replay/pcap_replay.c -o pcap_replay.c.bc

# Object files for target shadow-plugin-pcap_replay
shadow__plugin__pcap_replay_OBJECTS =

# External object files for target shadow-plugin-pcap_replay
shadow__plugin__pcap_replay_EXTERNAL_OBJECTS = \
"/home/blik/shadow-plugin-tor-enhanced/build/main/src/pcap_replay/shadow-plugin-pcap_replay.hoisted.bc"

src/pcap_replay/libshadow-plugin-pcap_replay.so: src/pcap_replay/shadow-plugin-pcap_replay.hoisted.bc
src/pcap_replay/libshadow-plugin-pcap_replay.so: src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/build.make
src/pcap_replay/libshadow-plugin-pcap_replay.so: /usr/lib/x86_64-linux-gnu/libglib-2.0.so
src/pcap_replay/libshadow-plugin-pcap_replay.so: /usr/lib/x86_64-linux-gnu/libgthread-2.0.so
src/pcap_replay/libshadow-plugin-pcap_replay.so: /usr/lib/x86_64-linux-gnu/libgmodule-2.0.so
src/pcap_replay/libshadow-plugin-pcap_replay.so: src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking C shared library libshadow-plugin-pcap_replay.so"
	cd /home/blik/shadow-plugin-tor-enhanced/build/main/src/pcap_replay && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/shadow-plugin-pcap_replay.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/build: src/pcap_replay/libshadow-plugin-pcap_replay.so
.PHONY : src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/build

src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/requires:
.PHONY : src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/requires

src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/clean:
	cd /home/blik/shadow-plugin-tor-enhanced/build/main/src/pcap_replay && $(CMAKE_COMMAND) -P CMakeFiles/shadow-plugin-pcap_replay.dir/cmake_clean.cmake
.PHONY : src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/clean

src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/depend: src/pcap_replay/shadow-plugin-pcap_replay.hoisted.bc
src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/depend: src/pcap_replay/shadow-plugin-pcap_replay.bc
src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/depend: src/pcap_replay/shadow-plugin-pcap_replay-bitcode.bc
src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/depend: src/pcap_replay/pcap_replay-main.c.bc
src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/depend: src/pcap_replay/pcap_replay.c.bc
	cd /home/blik/shadow-plugin-tor-enhanced/build/main && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/blik/shadow-plugin-tor-enhanced /home/blik/shadow-plugin-tor-enhanced/src/pcap_replay /home/blik/shadow-plugin-tor-enhanced/build/main /home/blik/shadow-plugin-tor-enhanced/build/main/src/pcap_replay /home/blik/shadow-plugin-tor-enhanced/build/main/src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/pcap_replay/CMakeFiles/shadow-plugin-pcap_replay.dir/depend

