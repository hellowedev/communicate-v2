#!/bin/bash

# ----------- Constants -----------
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log() {
  echo -e "${BLUE}[INFO $(date +'%H:%M:%S')]${NC} $1"
}

success() {
  echo -e "${GREEN}[✔ SUCCESS]${NC} $1"
}

error() {
  echo -e "${RED}[✖ ERROR]${NC} $1"
}

warn() {
  echo -e "${YELLOW}[! WARNING]${NC} $1"
}

# ----------- Run Tailwind CLI -----------
CSS_OUTPUT=${2}
CSS_INPUT=${1}

log "Running Tailwind CLI to build CSS..."
npx @tailwindcss/cli -i $CSS_INPUT -o $CSS_OUTPUT --watch --minify
if [ $? -ne 0 ]; then
  error "Tailwind CLI failed to start. Is npx installed and working?"
  exit 2
else
  success "Tailwind build process started. Watching for changes..."
fi
