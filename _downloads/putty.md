---
layout: downloadpage
permalink: /downloads/putty/
name: PuTTY
file_type: download
title: PuTTY
description: >-
  PuTTY is the classic free SSH and telnet client for Windows: lightweight, reliable, and endlessly configurable.
tags: [Telnet]
category: Network tools
sort_order: 100
rating: 100
changefreq: monthly
priority: 0.5
published: true
create_date: "2026-09-15"
modified_date: "2026-09-15"
created_by:
modified_by:
comments: true
redirect_url:
faq:
  - q: "Is PuTTY still maintained?"
    a: "Yes, Simon Tatham still releases updates with modern key exchange and cipher support."
  - q: "Where does PuTTY store sessions?"
    a: "In the Windows registry. Export them via regedit or use the portable trick of a settings file wrapper if you need portability."
  - q: "PuTTY or Windows' built-in OpenSSH?"
    a: "The built-in ssh command covers quick connections. PuTTY adds saved sessions, serial console support, and the Pageant key agent."
###
version: Latest
size: 
downloadurl: https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-installer.msi
response: 200
by: Simon Tatham
by_link: https://www.chiark.greenend.org.uk/~sgtatham/putty/
license: Open Source
os: Windows
---

{% include download-header.html download=page%}

PuTTY is the SSH client that generations of admins grew up on. It is tiny, rock-solid and covers SSH, telnet, serial and raw connections, with the companion tools PSCP, PSFTP, Plink, Pageant and PuTTYgen included in the installer.

Key features:

* SSH-2 with modern key exchange and ciphers
* Telnet, rlogin, serial and raw protocols
* Session profiles, port forwarding, X11 forwarding
* Pageant SSH agent and PuTTYgen key generator
* Command-line file transfer with PSCP/PSFTP
* Free, open source, no installation required
