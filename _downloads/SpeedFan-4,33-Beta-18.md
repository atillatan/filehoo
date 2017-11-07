---
layout: downloadpage
permalink: /downloads/SpeedFan-4,33-Beta-18/
name: SpeedFan 4.33 Beta 18
file_type: download
title: SpeedFan 4.33 Beta 18
description: >-
  SpeedFan - a small application that shows you fan speed, voltage and chip temerature.
tags: [System Info]
category: System
sort_order: 100
rating: 100
changefreq: monthly
priority: 0.5
published: true
create_date: 
modified_date: 03/11/2017
created_by: 
modified_by: 
comments: true
redirect_url: 
### 
version:  18
size: 1.23 MB
downloadurl: http://www.almico.com/sfbetaprogram.php
response: 200
by: 
by_link: 
licence: Freeware
os: Windows
---

{% include download-header.html download=page%}

<p style="fix-download-text !important">
<p><font size="2"><p>Themain viewing purpose of SpeedFan is to show its user what s reallygoing in their machine. When minimized, a temperature reading is showedon the button right of the desktop. When Speedfan is in an open windowyou can see a whole lot more. From Fan speed to total voltage, you canview any and all of the current fans. <br />
<br />
<span><strong>Here are some key features of "SpeedFan":</strong></span><br />
<br />
handle almost any number of South Bridges <br />
handle almost any number of hardware monitor chips <br />
handle almost any number of temperature readings <br />
handle almost any number of voltage readings <br />
handle almost any number of fan speed readings <br />
handle almost any number of PWMs .<br />
<br />
<br />
First of all, you have to identify which temperature sensor is which.SpeedFan strictly adheres to available datasheets for each sensor chip.Please remember that hardware monitors are chips that do have some pins(small connectors) which should be connected to some additionalhardware (temperature probes, thermistors or thermocouples) in order tobe able to read temperatures. <br />
<br />
Only a few hardware monitor chips do label their connectors with "CPU","System" and the like. Most of them use labels like "Temp1", "Local" or"Remote". The hardware manufacturers connect available pins todifferent temperature sensors basically according to the physicalplacement of components on the motherboard.<br />
<br />
This means that the same chip, an ITE IT8712F, for example, might beconnected to a sensor diode measuring CPU temperature on Temp2 and, ona different hardware, it might be connected on Temp1. If you have a"Local" sensor and a "Remote" labeled one, this usually means that"Local" is the temperature of the monitor chip itself and "Remote" isthe temperature read from a "remote" probe. <br />
<br />
When you have properly identified which temperature sensor is which,try to lower the speed of each fan and look at reported speed andtemperatures. If you do not allow SpeedFan to change any fan speed andset all the speeds too low, then SpeedFan won t be able to avoidoverheating. </p>
<div class="celltext_big"><br />
<br />
<strong>What s New</strong> in This Release:<br />
<br />
added a digitally signed 64 bit driver (fully tested under Vista 64 bit) <br />
added full support for INTEL CORE DUO internal temperature readings <br />
added full support for Andigilog aSC7621 <br />
added full support for Fintek F71882F <br />
added xAP support to publish temperatures and fan speeds <br />
improved support for Fintek F71782F <br />
improved support for IT8716F <br />
renamed temperatures readings for MAX6640 <br />
improved compatibility with Intel D975XBX2 <br />
reduced AD7416 and AD7417 false detections <br />
reduced MAX6650/6651 false detections <br />
improved Intel SMBus routines</div></p></p>
