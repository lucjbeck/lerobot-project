# Finding USB Ports

Identify the serial port for each arm. Run once per arm.

```bash
lerobot-find-port
```

Ports found for this setup (also in [../configs/environment_template.env](../configs/environment_template.env)):
- Follower: `/dev/tty.usbmodem5B415316401`
- Leader:   `/dev/tty.usbmodem5B415320881`

Ports can change on reboot/replug — re-run if a connection fails.
