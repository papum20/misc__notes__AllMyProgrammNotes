# EXAMPLES

## ssh tunnel
Create an **ssh tunnel**: a way to pass info from A to C passing through B.  
Assume A can reach B and B can reach C.  
(Some) uses:  
*	encrypt traffic (like vpn)
*	avoid firewall or other restrictions
*	connect to hostC if hostA can only access hostB

Different ways to do it:
1.	port forwarding, with `-L` : 
	*	`ssh [-f] -L portA:hostC:portC userB@hostB -N` : create a tunnel, i.e. bind hostA:portA to hostC:portC passing thorugh userB@hostB
		*	`-N` : don't execute remote command (otherwise would also connect via ssh, besides establishing a tunnel)
		*	`-f` : execute the ssh command in background
	*	now you can connect in any way to hostC via hostA:portA
		*	e.g.: `ssh [userC@]localhost:portA` : ssh
		*	e.g.: `git clone ssh://git@localhost:3333/user/repo.git` : git clone, from hostC connected to (proxy) hostB
	*	src:
		*	https://randyfay.com/content/git-over-ssh-tunnel-through-firewall-or-vpn
		*	https://www.revsys.com/writings/quicktips/ssh-tunnel.html
2.	jump with `-J` : 
	*	`ssh -J hostB hostC` :  
