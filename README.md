# shadow-plugin-tor-enhanced

This repository holds a modified version of the Shadow-tor plugin. The Tor implementation that is used in this version of Shadow-tor has been altered to unveil circuits anonymity by passing additional information during the circuit construction protocol (IP and Circuit ID of the circuit origin). The additional information the relays receive are stored by the mean of the Tor controller upon CELL_STATS events. The Python script 'analyze_circuits.py' has been writen to perform and verify the results of correlation attacks against Tor circuits with the help of the information stored in the Tor controller log files.

Furthermore, this modified version of Shadow-tor includes a new plugin, called the pcap_replay. The plugin allows to run clients that "replay" traffic TCP stored in pcap files ([More here](https://github.com/shadow/shadow-plugin-extras/tree/master/pcap_replay). The script 'generate_topology.py' can be used to generate Shadow topologies including pcap_replay entities (modified version of the 'generate.py' script written by Rob Jansen. 

IMPORTANT NOTE:
This modified version of Shadow-tor plugin cannot be used to run hidden services !

## Dependencies
First, [Shadow and its dependencies have to be correctly installed](https://github.com/shadow/shadow)

When Shadow is smoothly running, install Shadow-tor plugin dependencies :


```
sudo apt-get -y install gcc automake autoconf zlib1g-dev

```

Then install libpcap library for the pcap_replay plugin :

```
sudo apt-get install libpcap-dev
```

## Setup and install

```
git clone https://github.com/HenriCrombe/shadow-plugin-tor-enhanced.git
cd shadow-plugin-tor-enhanced
./setup build -c
./setup install
```

## Usage 

This version of the Shadow-tor plugin works as the original version ([see here](https://github.com/shadow/shadow-plugin-tor/wiki) and is ready to run the pcap-replay plugin ([see here](https://github.com/shadow/shadow-plugin-extras/tree/master/pcap_replay)). 


## License deviations

No deviation from LICENSE.


## Last known working version

+ Shadow 'v1.11.1-25-g9609e85 2016-08-04 running GLib v2.46.2 and IGraph v0.7.1'




