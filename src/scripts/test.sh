#!/bin/bash

# Set install flag to false
install_flag=false

# Print help message
print_help() {
    echo "Run Pytest on all test files."
    echo " "
    echo "Usage: ./test.sh [options]"
    echo " "
    echo "Options:"
    echo "-h        show brief help"
    echo "-i        intall dependencies"
    exit 0
}

# Parse command line arguments
while getopts 'ih' flag; do
    case "${flag}" in
    i) install_flag=true ;;
    h) print_help ;;
    *) print_help ;;
    esac
done

# Move to src directory
cd "$(dirname "$(readlink -f "$0")")/.."

# Run the install script with dev dependencies if the flag is set
if [ "$install_flag" = true ]; then
    echo "Running install script..."
    ./scripts/install.sh -d
fi

# Run Pytest
echo "Running Pytest..."
pipenv run python -m pytest tests/
