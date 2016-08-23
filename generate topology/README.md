# generate_edited.py

This script is a modified version of the generate script provided with shadow. This new version of the script supports the pcap_replay plugin. Basically, the purpose of the script is to facilitate the generation of topologies based on the replay of traces between some clients and servers. In the case of our thesis, it has been used for the generation of the IRC and the SSH topology.   

# Setup and install

+ Make sure that you have already build shadow-plugin-tor using './setup build'.
+ Don't forget to export your path.

```bash

export PATH=${PATH}:~/shadow-plugin-tor/build/tor/src/or:~/shadow-plugin-tor/build/tor/src/tools

```
+ Place the script inside ~/shadow-plugin-tor/tools/

# Example

This example depicts the generation of a simplified version of our IRC topology. 

```bash
mkdir mytor
cd mytor
python ~/shadow-plugin-tor/tools/generate_edited.py  --nauths 1 --nrelays 10 --nclients 3 --nservers 3 --firc 1.0 --traces irc_traces/ --ipsrc 10.0.1.37 --portsrc 50935 --ipdst 130.89.149.132 --portdst 6669 alexa-top-1000-ips.csv consensuses-2016-02/01/2016-02-01-03-00-00-consensus server-descriptors-2016-02 extra-infos-2016-02 clients.csv

```

+ As you can observe, this version of the script also relies on Tor metrics data. You need to download those files if you want to generate your own network topology. You can refer to https://github.com/shadow/shadow-plugin-tor/wiki to grab the full list of mandatory files.

# Parameters

The script supports those additional parameters:
+ --firc: always followed by 1.0 to generate a topology of IRC clients.
+ --fssh:: always followed by 1.0 to generate a topology of SSH clients.
+ --traces: followed by a folder containing the traces to replay.
+ --ipsrc: followed by the source ip address belonging to the first peer of the trace(s).
+ --portsrc: followed by the port number belonging to the first peer of the trace(s).
+ --ipdst: followed by the source ip address belonging to the second peer of the trace(s).
+ --portdst: followed by the port number belonging to the second peer of the trace(s).


# Notes

+ Always Make sure that the amount of clients and servers in your topology is balanced. For example, a topology with 10 clients requires 10 servers in order to properly synchronize the packets exchange between a client-server pair.

+ This script has been developed to generate a topology replaying a single type of traffic. Therefore, it is not suitable for generating topologies in which different types of traffics are mixed. 



