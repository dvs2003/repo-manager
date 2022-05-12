# -*- coding: utf-8 -*-
"""
Created on Mon May  9 10:23:47 2022

@author: singh
"""

import subprocess

distro = 'fedora'

#{<repo_id>:<repo_name>}
repositories = {}
ids = []
gpg_keys = {'OFFICIAL':[], 'UNOFFICIAL':[]}

def list_all_repos():
    global repositories
    c = 0
    for i in subprocess.run(['dnf', 'repolist'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n'):#remiove pipe and see
        if c >= 1:
            a = i.find(' ')
            i.replace(' ', '')
            repositories[i[:a].replace(' ', '')] = i[a:].replace(' ', '')
            
        c += 1
    
    for i in repositories:
        ids.append(i)
        
    print(max(repositories))
    lngst = len(max(repositories, key=len)) + 4
            
    count = 0
    for i in repositories:
        print(f'{count} >> {i}{" "*(lngst-len(i))}:\t{repositories[i]}')
    count += 1
    
    
def list_all_gpg():
    gpg_keys['OFFICIAL'] = subprocess.run(['ls', '/etc/pki/rpm-gpg/'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    gpg_keys['UNOFFICIAL'] = subprocess.run(["rpm", "-q", "gpg-pubkey", "--qf", "'%{NAME}-%{VERSION}-%{RELEASE}\t%{SUMMARY}\n'"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    
    print('OFFICIAL')
    print(gpg_keys['OFFICIAL'])
    print('UNOFFICIAL')
    print(gpg_keys['UNOFFICIAL'])

def delete_gpg(gpgkey):
    subprocess.run(['rpm', '-e', gpgkey], stdout=subprocess.PIPE).stdout.decode('utf-8')
    
def enable_repo(repo):
    subprocess.run(['rpm', 'config-manager', '--set-enabled', repositories[ids[repo]]], stdout=subprocess.PIPE).stdout.decode('utf-8')
    
def disable_repo(repo):
    subprocess.run(['rpm', 'config-manager', '--set-disabled', repositories[ids[repo]]], stdout=subprocess.PIPE).stdout.decode('utf-8')

def delete_repo(repo):
    subprocess.run(['rm', '-f', '/etc/yum.repos.d/', repositories[ids[repo]]], stdout=subprocess.PIPE).stdout.decode('utf-8')

#conversion to some form of OOP

class gpg_keys():
    def __init__(self):
        pass

class repos():
    def __init__(self):
        pass
list_all_repos()
"""
find the longest repo id
add it by 4 then : then 4 then name
"""
#implement ids in gpg and call it ids_repo and ids_gpg
#select id to delete
#implement a way to add repo and gpg
#list dependency as gpg-pubkey
#delete/enable/disable <index_no>