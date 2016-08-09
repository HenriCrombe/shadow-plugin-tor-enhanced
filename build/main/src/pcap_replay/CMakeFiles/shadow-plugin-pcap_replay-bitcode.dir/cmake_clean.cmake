FILE(REMOVE_RECURSE
  "pcap_replay-main.c.bc"
  "pcap_replay.c.bc"
  "shadow-plugin-pcap_replay-bitcode.bc"
  "shadow-plugin-pcap_replay.bc"
  "shadow-plugin-pcap_replay.hoisted.bc"
  "CMakeFiles/shadow-plugin-pcap_replay-bitcode"
  "shadow-plugin-pcap_replay-bitcode.bc"
  "pcap_replay-main.c.bc"
  "pcap_replay.c.bc"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/shadow-plugin-pcap_replay-bitcode.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
