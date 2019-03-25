# ThermoPi

Raspberry Pi Climate Control

Physical Modules:
- Pi thermometer
- Pi IR LED

With the above modules connected to GPIO, this project allows a raspberry pi (or similar board)
to run as a climate control server.

Allows mobile access to temperature readings and AC control.

AC control requires raw IR codes to be recorded in lirc.conf, (with LIRC and irsend set up appropriately on
the board).

The system is used as follows:

- Go to \<pi url\>:8765/temp to get the current temperature.
- Go to \<pi url\>:8765/ac/1 to switch AC on.
- Go to \<pi url\>:8765/ac/0 to switch AC off.
- Go to \<pi url\>:8765/ac/\<x\> to switch AC on for x minutes.

For access on public networks, forward desired public port to 8765 on the pi.
