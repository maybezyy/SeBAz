# count of total score
from subprocess import Popen, PIPE
total_score = 85 # till 2.3.5

# calling subprocess function


def call(execute, pos = 0):
    return Popen(execute, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True).communicate()[pos].decode('utf-8')


# 1.1.1 Disable unused filesystems
unused_filesystems = ['cramfs', 'freevxfs',
                      'jffs2', 'hfs', 'hfsplus', 'squashfs', 'udf']

# 1.1.2 -> 1.1.5 /tmp options
tmp_options = ['nodev', 'nosuid', 'noexec']

# 1.4.1 GRUB root permissions
root_permissions = ['004', '040', '044', '400', '404', '440', '444']

# 2.1 inetd services
inetd_services = ['chargen', 'daytime',
                  'discard', 'echo', 'time', 'telnet', 'tftp']

# 2.2.1.2 ntp restrict
ntp_restrict = ['default', 'kod', 'nomodify', 'notrap', 'nopeer', 'noquery']

# 2.2.3 -> 2.2.14 ; 2.2.16 ; 2.2.17 ( - 2.2.7 ) time sync services
time_sync = ['avahi-daemon', 'cups', 'dhcpd', 'slapd', 'named',
             'vsftpd', 'httpd', 'dovecot', 'smb', 'squid', 'snmpd', 'rsyncd', 'ypserv']

# 2.3.1 -> 2.3.4 service clients
service_clients = ['ypbind', 'rsh', 'talk', 'telnet']