# [ENGLISH] Accessing LED
Raspberry Pi 3 comes with a LED to indicate SD card activity. With MATLAB we can control it for other purposes such as indicating input by user or other conditions. Firstly we want to know LEDs that are available, and we can do it by running the commands below.

```matlab
rpi = raspi() %initializing Raspberry Pi connection
showLEDs(rpi) %show available LEDs on Raspberry Pi
```

The output should be as below.

<img src="/images/leds.jpg" height="300">

After knowing that available LED is ```'led0'```, we can now try to blink it by running the commands below.

```matlab
for i = 1:5
  writeLED(rpi, 'led0', true)
  pause(1)
  writeLED(rpi, 'led0', false)
  pause(1)
end
```

## The topics which will be included in this project are:
* [Accessing LED](/11_MATLAB_Support_Package).
* [Accessing GPIO](/11_MATLAB_Support_Package).
* [Controlling Servo](/11_MATLAB_Support_Package).