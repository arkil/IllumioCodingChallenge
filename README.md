# Illumio-Coding-Challenge

# Implmentation


* Implemented Port Trie and Ip Trie for efficient searching. 
* Mapped Direction + protocol  to PortTrie
* Port Trie will generate IpTrie for each port.

* Constant time searching regardless of input size
* Port Trie if all ports given space of 2^16
* Ip Trie if all ip given space of 2^32

# Testing
* I used Python unittest to assert different test scenario. Program still worked for the case when there was a range in the port and also the ipAddress. 


# Refinements
* Radix Tree can be used to compressed 
* Merging of ranges will generate less Tries and space can be optimized.


# Teams
1) Data team.
2) Platform team.
3) Policy team.