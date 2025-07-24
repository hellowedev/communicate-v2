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

# ----------- Setup Tailwind -----------
log "Installing Tailwind CSS via npm..."
npm install tailwindcss @tailwindcss/cli -D
if [ $? -ne 0 ]; then
  error "npm install failed. Make sure you're in the correct project folder."
  exit 1
else
  success "Tailwind installed as a dev dependency."
fi

# ----------- Create Input CSS File -----------
CSS_INPUT=${1}
log "Creating Tailwind input file: $CSS_INPUT"
if [ -f "$CSS_INPUT" ]; then
  warn "File $CSS_INPUT already exists. Skipping creation."
else
  touch "$CSS_INPUT"
  echo -e '@import "tailwindcss"; @plugin "daisyui"; input[type="text"] { @apply bg-green-100 outline-none p-2 border border-transparent hover:border-green-500;}' > "$CSS_INPUT"
  success "Created $CSS_INPUT with Tailwind directives."
fi
