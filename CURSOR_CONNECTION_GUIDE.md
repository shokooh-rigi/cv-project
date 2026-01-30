# Cursor AI Connection Guide for V2Ray Users in Iran

If you are experiencing connection issues with Cursor AI due to internet restrictions, you need to configure Cursor to route its traffic through your V2Ray proxy.

## Step 1: Find your V2Ray Local Port

First, identify which port your V2Ray core is listening on locally.
- Typically, V2Ray uses **10808** for SOCKS5 and **10809** for HTTP.
- Check your V2Ray configuration file (often `config.json`) for the `inbounds` section to confirm the port.

## Step 2: Configure Proxy in Cursor Settings (Recommended)

This is the most reliable method to ensure Cursor's AI features use the proxy.

1. Open Cursor.
2. Go to **Settings** (File > Preferences > Settings, or press `Ctrl + ,`).
3. In the search bar, type `proxy`.
4. Look for **Http: Proxy**.
5. Enter your local proxy address.
   - If using HTTP: `http://127.0.0.1:10809`
   - If using SOCKS5: `socks5://127.0.0.1:10808`
   *(Replace ports with your actual V2Ray ports)*
6. Ensure **Http: Proxy Support** is set to `on` or `override`.
7. **Restart Cursor** to ensure changes take effect.

## Step 3: Configure System/Environment Variables

If the settings above don't fully resolve the issue, you can launch Cursor with proxy environment variables defined.

1. Close Cursor completely.
2. Open a terminal.
3. specific the proxy variables (replace ports as needed):

```bash
export HTTP_PROXY="http://127.0.0.1:10809"
export HTTPS_PROXY="http://127.0.0.1:10809"
# Or for SOCKS
# export ALL_PROXY="socks5://127.0.0.1:10808"
```

4. Launch Cursor from that same terminal:
```bash
cursor .
```

## Additional Troubleshooting

- **Strict SSL**: If you get certificate errors, try unchecking **Http: Proxy Strict SSL** in Cursor settings.
- **V2Ray Config**: Ensure "Sniffing" is enabled in your V2Ray configuration for better traffic routing.
- **Connection Test**: Verify your proxy works by running `curl -x http://127.0.0.1:10809 https://www.google.com` in your terminal.
