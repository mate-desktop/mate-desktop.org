---
title: Troubleshooting
weight: 5
---

Common issues and solutions for MATE Desktop.

## Display Issues

### Screen resolution not detected correctly

If your monitor resolution isn't detected properly:

1. Open **System → Preferences → Hardware → Displays**
2. Select your monitor and choose the correct resolution
3. Click **Apply** to test the settings

For persistent issues, you may need to create an Xorg configuration file:

```bash
sudo nano /etc/X11/xorg.conf.d/10-monitor.conf
```

### Compositing issues

If you experience screen tearing or visual glitches:

1. Open **System → Preferences → Look and Feel → Windows**
2. Try toggling the compositor on/off
3. Experiment with different compositing backends

To disable compositing via command line:

```bash
gsettings set org.mate.Marco.general compositing-manager false
```

## Panel Problems

### Panel disappeared

To reset panels to default:

```bash
mate-panel --reset
```

Or delete the panel settings and log out:

```bash
dconf reset -f /org/mate/panel/
```

### Applets not loading

Try removing and re-adding the applet:

1. Right-click on the panel
2. Select **Add to Panel**
3. Find and add the desired applet

## Caja Issues

### Caja crashes or freezes

Clear the Caja cache:

```bash
rm -rf ~/.cache/caja/
```

Reset Caja settings:

```bash
dconf reset -f /org/mate/caja/
```

### Thumbnails not generating

Install thumbnail generators:

```bash
# Ubuntu/Debian
sudo apt install tumbler ffmpegthumbnailer

# Fedora
sudo dnf install tumbler ffmpegthumbnailer
```

Clear thumbnail cache:

```bash
rm -rf ~/.cache/thumbnails/
```

## Audio Problems

### No sound

1. Check that MATE Volume Control shows the correct output device
2. Ensure the volume isn't muted
3. Check PulseAudio/PipeWire is running:

```bash
# For PulseAudio
pulseaudio --check && echo "Running" || pulseaudio --start

# For PipeWire
systemctl --user status pipewire
```

## Session Issues

### MATE won't start

If MATE fails to start from your display manager:

1. Try starting from a TTY (Ctrl+Alt+F2):

```bash
export XDG_SESSION_TYPE=x11
dbus-launch mate-session
```

2. Check for errors in logs:

```bash
journalctl --user -b | grep -i mate
cat ~/.xsession-errors
```

### Reset all MATE settings

To completely reset MATE to defaults:

```bash
dconf reset -f /org/mate/
```

**Warning:** This will reset ALL MATE settings. Log out and back in for changes to take effect.

## Performance Issues

### Desktop feels slow

1. **Disable compositing** if not needed:
   - System → Preferences → Windows → disable compositor

2. **Reduce animations**:
   - Some themes have animation effects that can slow things down

3. **Check system resources**:
   - Open MATE System Monitor to check CPU/memory usage

4. **Disable unused startup applications**:
   - System → Preferences → Startup Applications

## Getting Help

If your issue isn't covered here:

- Check the [MATE Wiki](https://wiki.mate-desktop.org)
- Ask on IRC: #mate on irc.libera.chat
- Ask on Matrix: #mate:libera.chat
- Search or open an issue on [GitHub](https://github.com/mate-desktop)
