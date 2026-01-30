#!/bin/bash

# Helper script to set up proxy environment variables for V2Ray
# Usage: source enable_proxy.sh

# Default ports (Change these if your V2Ray config is different)
HTTP_PORT=10809
SOCKS_PORT=10808

echo "Setting up proxy variables for V2Ray..."

# Set HTTP Proxy
export HTTP_PROXY="http://127.0.0.1:$HTTP_PORT"
export HTTPS_PROXY="http://127.0.0.1:$HTTP_PORT"
export http_proxy="http://127.0.0.1:$HTTP_PORT"
export https_proxy="http://127.0.0.1:$HTTP_PORT"

# Set ALL_PROXY for tools that support it
export ALL_PROXY="socks5://127.0.0.1:$SOCKS_PORT"
export all_proxy="socks5://127.0.0.1:$SOCKS_PORT"

echo "Proxy variables set!"
echo "HTTP Proxy: http://127.0.0.1:$HTTP_PORT"
echo "SOCKS Proxy: socks5://127.0.0.1:$SOCKS_PORT"
echo ""
echo "To test connection, run: curl -I https://www.google.com"
echo "To launch Cursor with these settings, run: cursor ."
