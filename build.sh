#!/usr/bin/env bash
set -e

echo "Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Installing ffmpeg..."
apt-get update
apt-get install -y ffmpeg

echo "Build complete!"