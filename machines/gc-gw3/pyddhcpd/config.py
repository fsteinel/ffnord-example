from ipaddress import IPv4Address, IPv4Network

config = {

    ### DDHCP Config

    # Multicast UDP Port
    "mcport": 1234,

    # Multicast Group
    "mcgroup": "ff02::1234",

    # Interface for communication with other nodes
    "mcif": "ffgc-mvpn",

    # Subnet used as DHCP Pool
    "prefix": IPv4Network("10.0.0.0/27"),

    # Number of IPs per blocks
    "blocksize": 4,

    # Try to keep at least this many IPs ready
    "spares": 4,

    # A list of blocks that should not be used (may be [])
    "blocked": list(range(0, 2)),

    # Leasetime for blocks (inter-ddhcp, seconds)
    "blocktimeout": 30,

    # For how long blocks aren't touch when another nodes sends an inquiry (seconds)
    "tentativetimeout": 15,

    # Broadcast all claims every n seconds
    "claiminterval": 3,


    ### Config for clients

    # Interface on which clients will send requests
    "clientif": "ffgc-mvpn",

    # Server address (must be present on clientif)
    "siaddr": IPv4Address("172.19.1.1"),

    # A list of IPv4 addreses announced as default gateways to clients
    "routers": [IPv4Address("172.19.1.1")],

    # A list of DNS servers announcet to clients
    "dns": [IPv4Address("10.130.0.255"), IPv4Address("10.130.0.254")],

    # Subnetmask announced to clients
    "prefixlen": 20,

    # Leasetime for clients (seconds)
    "leasetime": 10
}
