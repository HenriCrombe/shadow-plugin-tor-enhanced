FILE(REMOVE_RECURSE
  "pcap_replay-main.c.bc"
  "pcap_replay.c.bc"
  "shadow-plugin-pcap_replay-bitcode.bc"
  "shadow-plugin-pcap_replay.bc"
  "shadow-plugin-pcap_replay.hoisted.bc"
  "shadow-plugin-pcap_replay.hoisted.bc"
  "shadow-plugin-pcap_replay.bc"
  "shadow-plugin-pcap_replay-bitcode.bc"
  "pcap_replay-main.c.bc"
  "pcap_replay.c.bc"
  "libshadow-plugin-pcap_replay.pdb"
  "libshadow-plugin-pcap_replay.so"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/shadow-plugin-pcap_replay.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
