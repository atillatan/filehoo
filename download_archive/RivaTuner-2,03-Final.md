---
layout: downloadpage
permalink: /downloads/RivaTuner-2,03-Final/
name: RivaTuner 2.03 Final
file_type: download
title: RivaTuner 2.03 Final
description: >-
  -
tags: [Video Tweak]
category: Tweak
sort_order: 100
rating: 100
changefreq: monthly
priority: 0.5
published: false
create_date: 
modified_date: 03/11/2017
created_by: 
modified_by: 
comments: true
redirect_url: 
### 
version:  Final
size: 2.16 MB
downloadurl: http://files2.guru3d.com/rivatuner/RivaTuner203 %5BGuru3D.com%5D.exe
response: -1
by: 
by_link: 
license: Freeware
os: Windows
---

{% include download-header.html download=page%}

<p style="fix-download-text !important">
<p><font size="2"><p>RivaTuneris the most powerful tweaking utility for NVIDIA display adaptersrunning under Windows 98 / Windows 98 SE / Windows ME / Windows 2000and Windows XP. <br />
<br />
The purpose of this utility is to give you access to all theundocumented features of the Detonator drivers. RivaTuner is a veryuseful video tweak utility.<br />
<br />
All versions of the Detonator drivers have a lot of undocumentedregistry entries. Some of them don’.t affect anything, but there aresome that are very useful. In general, they cannot give you bigperformance boost but they can improve image quality and solve somecompatibility problems. <br />
<br />
RivaTuner will help you to change all undocumented registry entries. </p>
<div class="celltext_big"><br />
<br />
<strong>What s New</strong> in This Release:<br />
<br />
Fixed "Enable LoadLibrary hooking" option in bundledRivaTunerStatisticsServer application, which was corrupted due tointernal hooking system changes introduced in the previous version.<br />
Fixed typo in PCI DeviceID database for certain AGP G71 GPU baseddisplay adapters, causing them to be improperly detected and handled asG73 based. <br />
Added workaround for internal MFC buffer overrun bug, causingLauncher tab to crash after adding launch item with a name containingmore than 256 characters. <br />
Minor UI and localization fixes.<br />
Added ForceWare 160.xx and 162.xx driver families support. <br />
Updated databases for Detonator and ForceWare drivers. Addeddatabases for ForceWare 158.22, 158.27, 160.03, 160.04 and 162.15. <br />
Added Catalyst 7.5 and 7.6 drivers detection. Please take a note thatCatalyst 7.5 and 7.6 driver files have the same file binary fileversions so both drivers will be detected as Catalyst 7.5 or newer inRivaTuner. <br />
Updated Catalyst 7.5 and 7.6 certified SoftR9x00 parch script (for Windows 2000/XP drivers only). <br />
Added ATI R600 GPU support. Now all RivaTuner s low-level featuresincluding overclocking, color correction, fan control and hardwaremonitoring are available on ATI RADEON 2900 family. Thanks to PeterYeung @ HIS for providing ATI RADEON 2900XT for testing. <br />
Added experimental ATI RV610 and RV630 GPUs support. Thanks to AndrewWorobiew for testing RivaTuner on ATI RADEON 2400XT, ATI RADEON 2600PROand ATI RADEON 2600XT. Please take a note that RV6xx support iscurrently in very early experimental stage and nothing but hardwaremonitoring and diagnostic report modules has been tested seriously withthese display adapter families. <br />
Updated RivaTunerStatisticsServer v2.3.0 bundled utility: <br />
Added framerate monitoring and OSD rendering support for Direct3D9applications using IDirect3DSwapChain9 interfaces for page flippingunder Vista (e.g. Tomb Raider: Legend). <br />
Improved hardware monitoring module: <br />
Now RivaTuner pauses hardware monitoring module before enteringsuspended mode and resumes monitoring when the system resumes. Thisimproves stability on certain hardware configurations, critical topolling in suspended mode. Power users may disable this feature usingPauseInSuspendedMode registry entry. <br />
Added description buffer overrun protection to all plugins with generic localization support. <br />
Added built-in provider for core temperature monitoring via RV610 and RV630 on-die thermal diodes. <br />
Added built-in provider for GPU usage monitoring on RV610 and RV630 graphics processors. <br />
Improved hardware monitoring plugins: <br />
Improved SMART.dll plugin. Now the plugin contains user customizableminimum hardware polling interval, which can be used to lowerperformance hit caused by slow S.M.A.R.T. hardware accessimplementations on certain combinations of ATA controllers and harddrive models. By default minimum hardware polling interval is set to 60seconds, however power users may redefine minimum polling interval forthis plugin by editing MinPollingInterval field in [Settings] sectionof SMART.cfg file. <br />
Improved VT1103.dll plugin: <br />
Added average current monitoring for VT1105 and VT1165 voltageregulators. Now the plugin is able to monitor average current for corevoltage regulators used on ATI display adapters equipped with VT1105and VT1165 (e.g. ATI RADEON 2900 family). <br />
Added programmable output voltage monitoring for VT1105 and VT1165voltage regulators. Now besides hardwired VID-based output voltages theplugin also able to monitor programmable output voltages on ATI displayadapters equipped with VT1105 and VT1165 (e.g. ATI RADEON 2900 family).Please take a note that output voltage programming implementationdepends on voltage regulator s circuit design and may differ dependingon the PCB. Currently the plugin s database contains programmable VIDto voltage mapping for reference design ATI RADEON 2900XT series only. <br />
Added temperature monitoring for VT1105 and VT1165 voltageregulators. Now the plugin is able to monitor temperature of voltageregulators used on ATI display adapters equipped with VT1105 and VT1165(e.g. ATI RADEON 2900 family). Please take a note that VT1165 ismultiphase voltage regulator and actually have multiple temperaturesensors installed in each slave chip. However to simplify understandingand visualization the plugin monitors just a single value read from thefirst slave chip. <br />
Added open source Everest.dll plugin. The plugin is able to importany monitoring data sources from Everest software and display them inRivaTuner Statistics Server s On-Screen Display. By default the pluginis configured to import CPU temperature , CPU fan speed , Systemtemperature , System fan speed , PSU fan speed , CPU voltage , PSU+3.3V voltage , PSU +5V voltage and PSU +12V voltage data sources,however you can customize the list of imported data sources by editingEverest.cfg file. Please take a note that Enable shared memory optionmust be ticked in Everest in File Preferences Hardware monitoringExternal applications tab to allow RivaTuner to import data from it.<br />
Improved diagnostic report module:<br />
Added new Intel chipsets to northbridges hardware database. <br />
Added PowerPlay table info to ATI VGA BIOS information diagnosticreport category. Now RivaTuner is able to decode PowerPlay statesdefining 2D/3D clocks and voltages in ATI RADEON 2400/2600/2900 displayadapters family. <br />
Added unified voltage table info to ATI VGA BIOS information diagnostic report category. Now RivaTuner is able to decode new ATivoltage table format and display information about voltage controllerI2C registers and VID encoding information for ATI RADEON 2900 displayadapters family. <br />
Improved low-level hardware overclocking module: <br />
Added PowerPlay based driver-level wrapper for 3D clock frequencyadjustment on ATI RADEON 2400/2600/2900 display adapters family. UnlikeOverdrive overclocking interface it doesn t require 8-pin power cableto be connected to card for proper functionality. Please take a notethat due to ATI Catalyst driver s PowerPlay programming issues it willreset current fan settings to defaults after applying new 3D clockfrequencies. It is recommended to reconfigure fan controls afterchanging 3D clock frequency until this issue is addressed in ATIdriver. <br />
Updated ATI VGA BIOS scripts parser. Added support for new tokens used in ATI RADEON 2900 VGA BIOS images. <br />
Now visual frequency clock testing is disabled on ATI cards if Overdrive or PowerPlay base driver-level wrapper is in use. <br />
Improved GUI for both driver-level and low-level hardwareoverclocking modules. Now to avoid confusing beginners RivaTuner hides Test button instead of disabling it when clock frequency testing isforcibly disabled or not available.<br />
Added Q and QUIT command line switches, allowing to unload RivaTunerfrom memory immediately either with hotkey or with desktop shortcut.<br />
Improved refresh overrider module. Now it is possible to overriderefresh rate during partial display mode change when the applicationdoesn t specify display mode bit depth explicitly (e.g. in Quake IIIwhen bit depth option is set to Default ).<br />
Improved numpad keys support for low-level keyboard hook based hotkey emulator.<br />
Rarely used ATIProble and NVInfo DOS tools are no longer supported and no longer bundled with RivaTuner.<br />
Improved Easter Eggs:<br />
Added new Easter Eggs. <br />
Improved built-in hardware emualtor. Added protections against incorrect MMIO emulation. <br />
Improved hidden ATI VGA BIOS decompiler: <br />
Added support for ATI RADEON 2x00 VGA BIOS specific script tokens. <br />
Now the decompiler analyzes code branching and doesn t stop decomipling a script when meeting the first RET token. <br />
Minor UI changes and improvements..</div></p></p>
