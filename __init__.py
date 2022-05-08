"""
Fedora : 
LIST GPG KEYS
ALL IMPORTED SIGNING KEYS : rpm -q gpg-pubkey --qf '%{NAME}-%{VERSION}-%{RELEASE}\t%{SUMMARY}\n'
OFFICIAL ARCHIVE SIGNING KEYS : ls /etc/pki/rpm-gpg/
rpm -e gpg-pubkey-b6792c39-53c4fbdd#keyname
REPO LIST
sudo dnf repo list
ENABLING
dnf config-manager --set-enabled repository_url
set the above disabled
sudo dnf config-manager --set-disabled <reponame>
delete repo rm -f /etc/yum.repos.d/<name-of-repository-file>

now for ubuntu, arch, gentoo PaIn
"""