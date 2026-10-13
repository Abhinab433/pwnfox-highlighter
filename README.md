# PwnFox Highlighter

A Burp Suite extension designed to improve HTTP traffic visibility by highlighting requests associated with PwnFox during web application penetration testing.

## Overview

When testing applications with multiple browser identities or security contexts, distinguishing HTTP requests can make traffic analysis easier. PwnFox Highlighter aims to help security testers identify relevant traffic directly within Burp Suite.

## Features

- Integrates with Burp Suite.
- Supports PwnFox-related HTTP traffic highlighting.
- Helps distinguish relevant requests during web application security assessments.
- Improves traffic visibility and analysis within the Burp Suite workflow.

## Requirements

- [Burp Suite](https://portswigger.net/burp)
- [PwnFox](https://github.com/yeswehack/PwnFox)
- Python support for Burp Suite extensions, if required by the implementation.

## Installation

1. Clone or download this repository:

   ```bash
   git clone https://github.com/Abhinab433/pwnfox-highlighter.git
   ```

2. Open Burp Suite.
3. Navigate to **Extensions → Installed**.
4. Click **Add**.
5. Select the appropriate extension type and provide the extension file, `pwnfox_highlighter.py`, if supported by your Burp Suite configuration.
6. Click **Next** and check the extension output for errors.

**Note:** The exact extension type and Python runtime requirements depend on the implementation and the Burp Suite version. Verify these before loading the extension.

## Usage

1. Start Burp Suite and ensure the extension is loaded successfully.
2. Configure PwnFox in your browser as required.
3. Browse the target application through Burp Suite.
4. Observe the HTTP traffic and identify the highlighting behavior provided by the extension.

## Use Cases

- Web application penetration testing.
- Analyzing HTTP requests from different browser identities.
- Improving request visibility during authenticated security testing.
- Supporting workflows involving PwnFox and Burp Suite.

## Disclaimer

This extension is intended for educational purposes and authorized security testing only. Use it only against systems for which you have permission to perform security assessments.

## Author

**Abhinab Shrestha**

- GitHub: [@Abhinab433](https://github.com/Abhinab433)
- Repository: [pwnfox-highlighter](https://github.com/Abhinab433/pwnfox-highlighter)

