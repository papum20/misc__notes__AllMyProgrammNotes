# BASICS  
  
## VIEW - COLUMNS:  
No.		: number of pkg (first=1)  
Time		: time from first pkg, seconds broken down to nanoseconds (first=0)  
Source	: source address (IPv4, IPv6 or Ethernet address)  
Destination	:	//  
Protocol	:   
Length	: length of frame, bytes/bits  
type=nbns:  
Info …:  
shows host name  
GET /…	: requesting url  
… HTTP/…	: http type  
  
## VIEW - ROWS:  
### COLORS:  
light purple	= TCP traffic  
light blue	= UDP traffic  
black		= (TCP) packets with problems (e.g. delivered out of order)  
green		= HTTP traffic  
light yellow	= Windows-specific traffic,  
including Server Message Blocks (SMB) and NetBIOS  
dark yellow	= Routing  
dark gray	= TCP SYN, FIN and ACK traffic  
dark blue	= (light blue) DNS traffic  
  
## TYPES:  
dhcp	:   
	can help identify hosts for almost any type of computer connected to your network  
nbns	:   
	nbns traffic is generated (primarily) by computers running Windows or MacOS  
  
## FILTERS:  
### SYNTAX:  
and	:   
!	:   
eq	: equals  
### FUNCTIONS:  
“str1” contains “str2”	:    
“str1” matches <regexp> :   
### FILTERS:  
bootp		: dhcp (dhcp for wireshark 3.0)  
dhcp		: dhcp  
dns		: dns  
frame		: frame, pkt?  
frame.comment : comments in pkts  
http.content_type : type  
http.request	:  
to find domains used in HTTP traffic  
ip.addr	:   
ip.dst		:   
ip.src		:   
kerberos.CNameString	: find pkgs containing kerberos.CNameString ?  
nbns		: nbns  
pkt_comment	 : comments  
ssl.handshake.type==1 :   
			to find domains used in encrypted HTTPS traffic  
tcp.ack	:   
tcp.len==int	: data len  
FILTERS - COMBINED:  
http.request and !(ssdp)	: ?  
  
## FRAME DETAILS:  
type=http:  
Hypertext Transfer Protocol -> Host: … : http domain  
type=https:  
Transport Layer Security / Secure Sockets Layer -> TLS … Handshake Protocol: … -> Handshake Protocol: … -> Extension: server_name (...) -> Server Name Indication extension -> Server Name: … : server name  
type=dhcp Request:  
Ethernet … :  
Src/Dest : source/dest mac  
Internet Protocol …:  
Src/Dest : source/dest ip  
note: you can correlate ip/mac from here  
Dynamic Host Configuration Protocol (Request) / Bootstrap Protocol (Request) ->  
-> Option …: Client identifier	: Client MAC address  
-> Option …: Host name		: Host Name  
filtered with=kerberos.CNameString:  
Kerberos -> as-req -> req-body -> cname -> cname-string: …  
	-> CNameString	: hostname (or) Windows user name  
				hostname	ends with $  
				username	doesn’t end with $  
	note: so, you can find usernames with filter  
“kerberos.CNameString and !(kerberos.CNameString contains $)”  
type=nbns:  
NetBIOS Name Service -> Additional records -> <host name> … ->  
	-> Name	: host name  
	-> Addr	: ip  
  
## FOLLOW - TCP STREAM - DETAILS:  
type=http:  
User-Agent:  
Browser used  
(if Windows host) Os used	:   
Windows NT 5.1	: Windows XP  
Windows NT 6.0	: Windows Vista  
Windows NT 6.1	: Windows 7  
Windows NT 6.2	: Windows 8  
Windows NT 6.3	: Windows 8.1  
Windows NT 10.0	: Windows 10  
(if Android host) OS used			:   
(if Android host) brand name			:   
(if Android host) device model		:   
(if Apple mobile device host) OS used	:   
(if Apple mobile device host) device type	: (i.e. iPhone, iPad or iPod)  
  
## COLORS :  
red = client request  
blue = client receiving  
  
## SETTINGS:  
TOP MENUS:  
View:  
Time display format  
Colorize packet list	: toggle colors for rows  
Coloring rules	:   
OTHER - COLUMNS:  
Right click on any column :  
align left / center / right  
hide columns  
remove this column  
column preferences : add, remove, hide, manage  
Right click on a frame detail row:  
Apply as column  
OTHER - ROWS:  
Right click on row :   
Follow -> TCP Stream :   

## README.md  
*	[README.md](./README.md)  

