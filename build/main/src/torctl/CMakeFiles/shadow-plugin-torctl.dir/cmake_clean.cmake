file(REMOVE_RECURSE
  "torctl-main.c.bc"
  "torctl.c.bc"
  "shadow-plugin-torctl-bitcode.bc"
  "shadow-plugin-torctl.bc"
  "shadow-plugin-torctl.hoisted.bc"
  "shadow-plugin-torctl.hoisted.bc"
  "shadow-plugin-torctl.bc"
  "shadow-plugin-torctl-bitcode.bc"
  "torctl-main.c.bc"
  "torctl.c.bc"
  "libshadow-plugin-torctl.pdb"
  "libshadow-plugin-torctl.so"
)

# Per-language clean rules from dependency scanning.
foreach(lang)
  include(CMakeFiles/shadow-plugin-torctl.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
