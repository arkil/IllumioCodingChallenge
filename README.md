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
* Radix Tree can be used to compressed common nodes in Trie
* Interval Tree and Segment Tree are also feasible and more optimized to query over range (since query doesn't have ranges for port and ip, Trie is equally efficient)
* Mapping port and IP will help to reduce space complexity



# Teams
1) Data team.
2) Platform team.
3) Policy team.