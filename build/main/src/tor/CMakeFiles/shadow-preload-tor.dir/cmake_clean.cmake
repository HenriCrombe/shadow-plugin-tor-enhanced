FILE(REMOVE_RECURSE
  "shadowtor-main.c.bc"
  "networkstatus.c.bc"
  "hibernate.c.bc"
  "onion.c.bc"
  "dircollate.c.bc"
  "command.c.bc"
  "confparse.c.bc"
  "statefile.c.bc"
  "circuitbuild.c.bc"
  "connection_edge.c.bc"
  "rendcommon.c.bc"
  "main.c.bc"
  "dirserv.c.bc"
  "keypin.c.bc"
  "rendclient.c.bc"
  "status.c.bc"
  "connection.c.bc"
  "directory.c.bc"
  "channeltls.c.bc"
  "dnsserv.c.bc"
  "ext_orport.c.bc"
  "circuitstats.c.bc"
  "transports.c.bc"
  "rephist.c.bc"
  "onion_fast.c.bc"
  "connection_or.c.bc"
  "torcert.c.bc"
  "entrynodes.c.bc"
  "circuitmux_ewma.c.bc"
  "rendservice.c.bc"
  "circpathbias.c.bc"
  "rendmid.c.bc"
  "routerlist.c.bc"
  "reasons.c.bc"
  "scheduler.c.bc"
  "routerset.c.bc"
  "config.c.bc"
  "routerparse.c.bc"
  "cpuworker.c.bc"
  "channel.c.bc"
  "buffers.c.bc"
  "routerkeys.c.bc"
  "addressmap.c.bc"
  "fp_pair.c.bc"
  "nodelist.c.bc"
  "policies.c.bc"
  "circuitlist.c.bc"
  "microdesc.c.bc"
  "replaycache.c.bc"
  "circuitmux.c.bc"
  "router.c.bc"
  "dirvote.c.bc"
  "control.c.bc"
  "dns.c.bc"
  "onion_ntor.c.bc"
  "onion_tap.c.bc"
  "geoip.c.bc"
  "circuituse.c.bc"
  "relay.c.bc"
  "rendcache.c.bc"
  "util_format.c.bc"
  "compat_libevent.c.bc"
  "crypto_ed25519.c.bc"
  "torgzip.c.bc"
  "backtrace.c.bc"
  "compat.c.bc"
  "di_ops.c.bc"
  "workqueue.c.bc"
  "procmon.c.bc"
  "log.c.bc"
  "address.c.bc"
  "compat_threads.c.bc"
  "crypto.c.bc"
  "aes.c.bc"
  "crypto_s2k.c.bc"
  "container.c.bc"
  "sandbox.c.bc"
  "crypto_curve25519.c.bc"
  "memarea.c.bc"
  "util_process.c.bc"
  "compat_pthreads.c.bc"
  "crypto_pwbox.c.bc"
  "util.c.bc"
  "tortls.c.bc"
  "crypto_format.c.bc"
  "readpassphrase.c.bc"
  "csiphash.c.bc"
  "eventdns.c.bc"
  "curve25519-donna-c64.c.bc"
  "ge_precomp_0.c.bc"
  "fe_sq2.c.bc"
  "ge_p3_dbl.c.bc"
  "fe_frombytes.c.bc"
  "fe_tobytes.c.bc"
  "ge_p3_to_cached.c.bc"
  "fe_sq.c.bc"
  "ge_p1p1_to_p2.c.bc"
  "fe_0.c.bc"
  "ge_p3_to_p2.c.bc"
  "ge_msub.c.bc"
  "ge_p2_dbl.c.bc"
  "sign.c.bc"
  "fe_mul.c.bc"
  "sc_muladd.c.bc"
  "fe_add.c.bc"
  "fe_sub.c.bc"
  "ge_add.c.bc"
  "fe_invert.c.bc"
  "keypair.c.bc"
  "ge_double_scalarmult.c.bc"
  "keyconv.c.bc"
  "fe_isnonzero.c.bc"
  "ge_frombytes.c.bc"
  "open.c.bc"
  "ge_p2_0.c.bc"
  "ge_sub.c.bc"
  "ge_scalarmult_base.c.bc"
  "fe_pow22523.c.bc"
  "sc_reduce.c.bc"
  "ge_p3_tobytes.c.bc"
  "ge_p3_0.c.bc"
  "fe_copy.c.bc"
  "fe_1.c.bc"
  "ge_tobytes.c.bc"
  "ge_madd.c.bc"
  "ge_p1p1_to_p3.c.bc"
  "fe_neg.c.bc"
  "fe_isnegative.c.bc"
  "fe_cmov.c.bc"
  "blinding.c.bc"
  "ed25519_tor.c.bc"
  "pwbox.c.bc"
  "link_handshake.c.bc"
  "ed25519_cert.c.bc"
  "trunnel.c.bc"
  "shadow-plugin-tor-bitcode.bc"
  "shadow-plugin-tor.bc"
  "shadow-plugin-tor.hoisted.bc"
  "CMakeFiles/shadow-preload-tor.dir/shadowtor-preload.c.o"
  "libshadow-preload-tor.pdb"
  "libshadow-preload-tor.so"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang C)
  INCLUDE(CMakeFiles/shadow-preload-tor.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
