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

import subprocess

distro = 'fedora'

def list_all_repos():
    subprocess.run(['dnf', 'repolist'], stdout=subprocess.PIPE).stdout.decode('utf-8')

def list_all_gpg():
    print('OFFICIAL')
    subprocess.run(['ls', '/etc/pki/rpm-gpg/'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    print('UNOFFICIAL')
    subprocess.run(["rpm", "-q", "gpg-pubkey", "--qf", "'%{NAME}-%{VERSION}-%{RELEASE}\t%{SUMMARY}\n'"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    

def delete_gpg(gpgkey):
    subprocess.run(['rpm', '-e', gpgkey], stdout=subprocess.PIPE).stdout.decode('utf-8')
    
def enable_repo(repo):
    subprocess.run(['rpm', 'config-manager', '--set-enabled', repo], stdout=subprocess.PIPE).stdout.decode('utf-8')
    
def disable_repo(repo):
    subprocess.run(['rpm', 'config-manager', '--set-disabled', repo], stdout=subprocess.PIPE).stdout.decode('utf-8')

def delete_repo(repo):
    subprocess.run(['rm', '-f', '/etc/yum.repos.d/', repo], stdout=subprocess.PIPE).stdout.decode('utf-8')
#if rpm can be replaced with deb and stuff
#CHECK THE DISTRO