---
title: "Arduino Sound Alarm"
date: 2012-12-06
categories: 
  - "arduino"
  - "codingsoftware"
  - "geeky"
tags: 
  - "alarm"
  - "arduino-2"
  - "sound"
slug: "arduino-sound-alarm"
---

I've just completed my second Arduino project, a sound level detector which sets off an "alarm" when there's the sound level is to high for too long.  I built it for use in a school that wants to provide visual feedback to students when they are being too loud.  The "alarm" is a string of flashing LEDs that's controlled by an IR-remote, which I reverse engineered using the the arduino itself and the excellent [IRremote](https://github.com/shirriff/Arduino-IRremote) library to figure out which codes activate the LED string. The IRremote library includes an example that [dumps the codes and code types](https://github.com/shirriff/Arduino-IRremote/blob/master/examples/IRrecvDump/IRrecvDump.ino) that remotes typically use.  So I just ran that example with my arduino hooked up to an [IR detector from adafruit](http://adafruit.com/products/157).  It was really quite easy to do.

It's been a fun project because it's quite flexible and configurable.  Here's a short video of the finished product:

http://www.youtube.com/watch?v=ZhZH9\_8INj4

For anyone who wants to build one of these here's a bread-board diagram that I made using the very cool [Fritzing](http://fritzing.org/) package:

[![](/blog/images/sound_alarm_breadboard1.png "Sound Alarm Breadboard")](http://eehb.harris-braun.com/blog/wp-content/uploads/2012/12/sound_alarm_breadboard1.png)

The Adruino sketch that powers this is [available on github](https://github.com/zippy/sound_alarm).

Here are some details on the circuitry.  The sound detector is based on the [ZX-Sound board](http://www.inexglobal.com/downloads/ZX-sound_e.pdf). Here's a [nice post on the arduino.cc](http://arduino.cc/forum/index.php?topic=83641.0) site that I used as my starting place for building the sound part of this board.  The video helpfully includes a parts list which I sourced from [Allied electronics](http://www.alliedelec.com/), all except for the mic.  The [LCD is the $10 16x2](http://adafruit.com/products/181) from Adafruit ([their tutorial on wiring it up](http://learn.adafruit.com/character-lcds/wiring-a-character-lcd) was great), and I also used their [electret microphone](http://adafruit.com/products/1064).  One note about the microphone is that it's polarity matters.  If you get it in backwards, it's much less sensitive.  I found this out purely by accident!  I also used [their IR LED](https://www.adafruit.com/products/387).

Here are some photos of assembling the project.

First the prototyping phase:

[![](/blog/images/prototyping1.png "prototyping")](http://eehb.harris-braun.com/blog/wp-content/uploads/2012/12/prototyping1.png)

Then building the connector for the LCD:

[![](/blog/images/lcd_header_11.jpg "lcd_header_1")](http://eehb.harris-braun.com/blog/wp-content/uploads/2012/12/lcd_header_11.jpg)

[![](/blog/images/lcd_header_21.jpg "lcd_header_2")](http://eehb.harris-braun.com/blog/wp-content/uploads/2012/12/lcd_header_21.jpg)

[![](/blog/images/lcd_header_311.jpg "lcd_header_3")](http://eehb.harris-braun.com/blog/wp-content/uploads/2012/12/lcd_header_311.jpg)

Then drilling holes and installing the configuration controls (push-button and pot)

[![](/blog/images/setup_controls_11.png "setup_controls_1")](http://eehb.harris-braun.com/blog/wp-content/uploads/2012/12/setup_controls_11.png)

[](http://eehb.harris-braun.com/blog/wp-content/uploads/2012/12/setup_controls_11.png)[![](/blog/images/setup_controls_21.png "setup_controls_2")](http://eehb.harris-braun.com/blog/wp-content/uploads/2012/12/setup_controls_21.png)

Then assembling and soldering the board with the sound circuit and the trim pot for the LCD as well as the resistor for the IR LED.

[![](/blog/images/sound_board1.png "sound_board")](http://eehb.harris-braun.com/blog/wp-content/uploads/2012/12/sound_board1.png)

[![](/blog/images/sound_board_plus_lcd1.png "sound_board_plus_lcd")](http://eehb.harris-braun.com/blog/wp-content/uploads/2012/12/sound_board_plus_lcd1.png)

Finally, just before enclosing..

[![](/blog/images/just_before_enclosing1.png "just_before_enclosing")](http://eehb.harris-braun.com/blog/wp-content/uploads/2012/12/just_before_enclosing1.png)

The completed project.  Note that I left the mic and IR LED lose because I'm not sure exactly where the alarm is going to be installed and the way they face could matter.

[![](/blog/images/sound_alarm1.png "Completed Arduino Sound Alarm")](http://eehb.harris-braun.com/blog/wp-content/uploads/2012/12/sound_alarm1.png)

**Some lessons learned:**

1. When soldering a header for an LCD remember to take into account that if you copy the wiring order as you have plugged it into the bread-board, you will actually be doing it backwards because the connecter will be attached upside-down!
2. You will need to drill a little extra hole in your case to accept the tab on the pot that keeps it from rotating when you spin the shaft.
3. Electret microphones have a polarity.
4. Hot-glue is great for attaching push-buttons.
5. Ask you children for UI advice!  Will had the excellent idea of using the setup-pot to spin between the different settings.  In the original code I had it so you had to press the button to toggle between the setup parameters and then do a long-press to actually set one.  The way it ended up is much better.

**Parts List:**

Arduino Uno: https://www.adafruit.com/products/50 ($29.95)

Makershed Arduino Enclosure:  http://www.makershed.com/Clear\_Enclosure\_for\_Arduino\_p/mkad40.htm ($15.00)

9V powersupply: https://www.adafruit.com/products/63 ($6.95)

100K Potentiometer: Radioshack ($1.69)

pushbutton switch: Radioshack ($.99)

Breadboard PCB: https://www.adafruit.com/products/589 ($3.00)

Electret Mic: https://www.adafruit.com/products/1064 ($1.50)

IR LED: https://www.adafruit.com/products/387 ($.75)

LCD 2x16: https://www.adafruit.com/products/181 ($9.95)

Components: (~$5)

- resistors: 1k ohm x 2; 100k ohm x 2; 12 ohm; 39k ohm; 22k ohm; 230 ohm (for IR led)
- capacitors: 470uf 16v; 0.1uf 50v; 22uf 25v
- Dual op amp IC: TLC272

**Total Price: ~$70**
