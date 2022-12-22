#!/bin/bash
#!/bin/bash

# Set the color variable
green='\033[0;32m'
# Clear the color after that
clear='\033[0m'

echo "============initilization============="
git add .

git commit -m "Initializing"

git push

echo -e "${green}===================Deployed===================${clear}"
