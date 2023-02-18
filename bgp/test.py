#!/usr/bin/env python3

import subprocess

NETWORK_CONFIG = {
    "R1": "1.1.1.1",
    "R2": "2.2.2.2",
    "R3": "3.3.3.3"
}

def check_connectivity(source: str, destination: str) -> bool:
    response = subprocess.run(["docker", "exec", source, "ping", "-I", NETWORK_CONFIG[source], NETWORK_CONFIG[destination], "-c", "1"], capture_output=True)
    return False if response.returncode else True

if __name__ == "__main__":
    for source in NETWORK_CONFIG.keys():
        for destination in NETWORK_CONFIG.keys():
            print(f"{source} -> {destination}: {check_connectivity(source, destination)}")