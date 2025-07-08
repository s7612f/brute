#!/usr/bin/env python3

import subprocess
import argparse
import json

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

    config = load_config(args.config)

    target = config['target']
    username = config['username']
    password_list = config['password_list']
    protocol = config['protocol']
    params = config['params']

    brute_force(target, username, password_list, protocol, params)

if __name__ == '__main__':
    main()
