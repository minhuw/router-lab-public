#!/usr/bin/env bash

set -eou pipefail

if [[ $# -eq 0  || -z $1 ]];
then
    echo "please provide your student ID: ./pack.sh <student_id>"
    exit 1
fi

mkdir -p ./solution
for node in ./clab-topo/*/ ; do
    cp $node/flash/startup-config ./solution/$(basename $node).conf
done

containerlab save -t start.clab.yaml && tar czvf "router_submit_$1.tar.gz" ./clab-topo/*/flash/startup-config