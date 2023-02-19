#!/usr/bin/env python3

import subprocess

NETWORK_CONFIG = {
    "R1": "1.1.1.1",
    "R2": "2.2.2.2",
    "R3": "3.3.3.3",
    "R4": "4.4.4.4"
}

def check_connectivity(source: str, destination: str) -> bool:
    response = subprocess.run(["docker", "exec", source, "ping", "-I", NETWORK_CONFIG[source], NETWORK_CONFIG[destination], "-c", "1"], capture_output=True)
    return False if response.returncode else True

def check_path(source: str, destination: str, target_path: list[str]) -> bool:
    response = subprocess.run(["docker", "exec", source, "traceroute", NETWORK_CONFIG[destination]], capture_output=True)
    records = response.stdout.decode("utf-8").strip().split("\n")[1:]
    paths = [line.strip().split(" ")[2].split(".")[3] for line in records]
    print(f"Path {source} -> {destination}: {source[1]} -> {' -> '.join(paths)}")
    return paths == target_path

if __name__ == "__main__":
    done = True
    for source in NETWORK_CONFIG.keys():
        print(f"{source} -> ", end="") 
        for destination in NETWORK_CONFIG.keys():
            connected = check_connectivity(source, destination)
            done &= connected
            print(f"{destination}: {connected} ", end="")
        print("")

    if done:
        print("Pass Connectivity Test")
    else:
        print("Fail Connectivity Test")
        exit(1)

    if not check_path("R1", "R4", ['3', '4']):
        print("Path R1 -> R4 is not correct")
        exit(1)

    print("Pass Path Test")
    exit(0)