#!/bin/bash

case "$1" in
    build_generator)
        docker build -t data-generator ./generator ;;
    run_generator)
        docker run --rm -v "$(pwd)/data:/data" data-generator /data ;;
    create_local_data)
        python generator/generate.py ./data ;;
    build_reporter)
        docker build -t data-reporter ./reporter ;;
    run_reporter)
        docker run --rm -v "$(pwd)/data:/data" data-reporter ;;
    *)
        echo "Usage: $0 {build_generator|run_generator|create_local_data|build_reporter|run_reporter}"
        exit 1 ;;
esac