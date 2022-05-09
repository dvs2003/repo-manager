# -*- coding: utf-8 -*-
"""
Created on Mon May  9 10:23:47 2022

@author: singh
"""

import subprocess

distro = 'fedora'

repositories = ''
gpg_keys = {'OFFICIAL':[], 'UNOFFICIAL':[]}

def list_all_repos():
    global repositories
    repositories = subprocess.run(['dnf', 'repolist'], stdout=subprocess.PIPE).stdout.decode('utf-8')#remiove pipe and see
    print(repositories)
    
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
    subprocess.run(['rpm', 'config-manager', '--set-enabled', repo], stdout=subprocess.PIPE).stdout.decode('utf-8')
    
def disable_repo(repo):
    subprocess.run(['rpm', 'config-manager', '--set-disabled', repo], stdout=subprocess.PIPE).stdout.decode('utf-8')

def delete_repo(repo):
    subprocess.run(['rm', '-f', '/etc/yum.repos.d/', repo], stdout=subprocess.PIPE).stdout.decode('utf-8')