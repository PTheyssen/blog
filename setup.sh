#!/bin/bash

set -e

echo "Setting up Hakyll blog environment..."

# Check if we're on a supported system
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    DISTRO=$(lsb_release -si 2>/dev/null || echo "Unknown")
elif [[ "$OSTYPE" == "darwin"* ]]; then
    DISTRO="macOS"
else
    echo "Unsupported OS: $OSTYPE"
    exit 1
fi

echo "Detected: $DISTRO"

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Install system dependencies
install_system_deps() {
    if [[ "$DISTRO" == "Ubuntu" ]] || [[ "$DISTRO" == "Debian" ]]; then
        sudo apt-get update
        sudo apt-get install -y build-essential zlib1g-dev curl
    elif [[ "$DISTRO" == "macOS" ]]; then
        if ! command_exists brew; then
            echo "Installing Homebrew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        brew install zlib
    else
        echo "Please install build tools and zlib manually for your distribution"
    fi
}

# Install GHCup and Haskell toolchain
install_haskell() {
    if ! command_exists ghcup; then
        echo "Installing GHCup..."
        curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh
        source ~/.ghcup/env
    fi

    if ! command_exists ghc; then
        echo "Installing GHC..."
        ghcup install ghc recommended
        ghcup set ghc recommended
    fi

    if ! command_exists cabal; then
        echo "Installing Cabal..."
        ghcup install cabal recommended
        ghcup set cabal recommended
    fi
}

# Main setup
echo "Installing system dependencies..."
install_system_deps

echo "Installing Haskell toolchain..."
install_haskell

# Source GHCup environment
if [ -f ~/.ghcup/env ]; then
    source ~/.ghcup/env
fi

echo "Building the blog..."
cabal update
cabal new-install --overwrite-policy=always

echo ""
echo "Setup complete! 🎉"
echo ""
echo "To build the site: ./site build"
echo "To preview the site: ./site watch (then visit localhost:8000)"
echo ""
echo "Note: You may need to restart your shell or run 'source ~/.ghcup/env' to use the Haskell tools."