AlphaDisplay
============
The AlphaDisplay block will display a character string onto the display of the RainbowHat.

Properties
----------
- **words**: String, can only display four characters at a time.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Signals pass through block unmodified.

Commands
--------
None

***

Button
======
The Button block will notify a signal at the push of a button on the RainbowHat.

Properties
----------
None

Inputs
------
- **none**: 

Outputs
-------
- **channel**: The channel of the button that has been pressed or released (A, B, or C).
- **value**: True, if the button has been pressed. False, if the button has been released.

Commands
--------
None

***

Buzzer
======
The Buzzer block will play a sound at a specified frequency and duration.

Properties
----------
- **duration**: The time in seconds for the note to play.
- **frequency**: The frequency in Hz of the note.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Signals pass through block unmodified.

Commands
--------
None

***

FloatDisplay
============
The FloatDisplay block will display a float onto the display of the RainbowHat.

Properties
----------
- **numbers**: Float, can only display four numbers at a time.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Signals pass through block unmodified.

Commands
--------
None

***

LedStrip
========
The LedStrip block will control the 7 leds of the RainbowHat.

Properties
----------
- **pixelrgb0**: Red, Green, Blue value to display on pixel 0.
- **pixelrgb1**: Red, Green, Blue value to display on pixel 1.
- **pixelrgb2**: Red, Green, Blue value to display on pixel 2.
- **pixelrgb3**: Red, Green, Blue value to display on pixel 3.
- **pixelrgb4**: Red, Green, Blue value to display on pixel 4.
- **pixelrgb5**: Red, Green, Blue value to display on pixel 5.
- **pixelrgb6**: Red, Green, Blue value to display on pixel 6.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Signals pass through block unmodified.

Commands
--------
None

***

TemperatureSensor
=================
The TemperatureSensor block will notify a signal containing the temperature and pressure of the RainbowHat.

Properties
----------
- **enrich**: 

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **pressure_Pa**: The pressure of the RainbowHat in Pascal.
- **temp_C**: The temperature of the RainbowHat in Celsius.

Commands
--------
None

