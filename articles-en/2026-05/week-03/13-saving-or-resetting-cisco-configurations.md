# Saving or Resetting Cisco Configurations

Source: closed course page  
Date added: 2026-05-16  
Related plan item: Week 3 / Saving and resetting Cisco configurations  
Tags: cisco, running-config, startup-config, nvram, ram, write erase, reload, reset, configuration
Language: English
Translation pair: articles/2026-05/week-03/13-saving-or-resetting-cisco-configurations.md

## Summary

To save or reset a Cisco device correctly, you need to understand the difference between running configuration and startup configuration. Running config lives in RAM and shows what the device is doing right now. Startup config is stored in NVRAM/flash and loads during boot. If you erase only startup config, the current running config continues working until reload.

Main idea: factory reset usually requires two steps: erase the saved startup config, then reload without saving the current running config.

## Key Points

- Running configuration is the active configuration in RAM.
- Startup configuration is the saved configuration loaded at boot.
- `show running-config` displays the current active config.
- `show startup-config` displays the saved boot config.
- Running and startup configs can be different.
- Erasing startup config does not immediately erase the live running config.
- `write erase` erases the saved startup configuration.
- `erase startup-config` is another common way to erase the saved configuration.
- `reload` reboots the device.
- After startup config is erased, reload brings the device up without the old saved configuration.
- If prompted to save before reload during a wipe, choose `no`.
- Saying `yes` before reload can copy the old running config back into startup config.
- Always verify both before and after reset.
- Reset workflow is useful for labs, staging and decommissioning.

## Notes

### Why Resetting Can Be Confusing

Resetting a Cisco switch or router is not difficult.

The confusion comes from memory:

- what is active right now;
- what is saved for next boot;
- what gets erased;
- what survives until reload.

If you erase one place but forget the other, old configuration may appear to "come back."

### RAM and Running Configuration

RAM holds the active state while the device is powered on.

In Cisco configuration terms:

```text
RAM = running configuration
```

Running configuration is what the device is using right now.

If you change hostname, passwords or interface settings, those changes enter running config first.

If power is lost before saving, unsaved running config changes disappear.

### NVRAM and Startup Configuration

Startup configuration is the saved configuration the device loads during boot.

Traditionally, Cisco describes this as stored in NVRAM:

```text
NVRAM = startup configuration
```

On many modern devices, NVRAM may be emulated by flash storage, but the concept remains:

```text
startup-config = what the device remembers for next boot
```

### Boot Behavior

When a Cisco device boots:

```text
Load IOS
Find startup-config
Apply saved commands into running configuration
Start operating with that config
```

The startup config is like a saved script of commands.

The device applies it so the switch or router wakes up with hostname, passwords, interfaces and other settings.

### show running-config

Command:

```text
show running-config
```

Short form:

```text
show run
```

This shows what is active right now in RAM.

Use it to verify:

- current hostname;
- active passwords and line settings;
- current interface configuration;
- management IP;
- descriptions;
- other live settings.

### show startup-config

Command:

```text
show startup-config
```

This shows what the device will load next time it boots.

If startup config is missing, the device may report that startup configuration is not present.

### Why Running and Startup Can Differ

Running and startup configs can be different.

Example:

```text
Change hostname in running config
Forget to save
show running-config shows new hostname
show startup-config shows old hostname
Reload device
Old hostname returns
```

Another example:

```text
Erase startup config
Running config still has old hostname
Reload without saving
Device boots clean/default
```

This is the core reset concept.

### Reset Commands

Common ways to erase saved configuration:

```text
write erase
```

or:

```text
erase startup-config
```

Both target the saved configuration, not the live running configuration.

Some platforms also let you delete config files manually from flash, but for CCNA-level workflow, `write erase` and `erase startup-config` are the key commands.

### Why Hostname May Still Appear After Erase

After:

```text
write erase
```

the prompt may still show the old hostname.

That is expected.

Why?

```text
Startup config is erased.
Running config is still active in RAM.
```

You erased what the device will remember next boot, not what it is doing right now.

### reload

Command:

```text
reload
```

This reboots the device.

After startup config is erased, reload forces the device to boot again.

During boot:

- IOS loads;
- device looks for startup config;
- no startup config is found;
- device starts in default/unconfigured state.

That is the practical factory reset behavior.

### The Save Prompt Trap

When reloading, IOS may ask if you want to save the running configuration.

If you are trying to wipe the device:

```text
Do not save.
```

If you answer `yes`, IOS copies the current running config back into startup config.

That means the old settings return after reboot.

The reset fails because you re-saved what you meant to erase.

### Safe Reset Workflow

Practical workflow:

1. Verify current active config:

```text
show running-config
```

2. Verify saved config:

```text
show startup-config
```

3. Erase saved config:

```text
write erase
```

or:

```text
erase startup-config
```

4. Confirm startup config is gone:

```text
show startup-config
```

5. Reload:

```text
reload
```

6. If prompted to save, choose:

```text
no
```

7. Confirm device boots without old config.

### Lab and Decommissioning Use Cases

Resetting is useful in labs:

- configure;
- break;
- test;
- erase;
- reload;
- repeat.

It is also useful when decommissioning:

- remove old hostnames;
- remove passwords;
- remove VLANs;
- remove management IPs;
- avoid leaking business configuration.

For NetworkChuck Coffee, wiping old config matters before reusing or handing off hardware.

### Main Takeaway

Remember the difference:

```text
Startup config = what the device remembers
Running config = what the device is doing right now
```

To truly reset:

```text
Erase startup config.
Reload.
Do not save running config when prompted.
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Running configuration | Active configuration currently in RAM. |
| Startup configuration | Saved configuration loaded during boot. |
| RAM | Temporary memory where running config lives. |
| NVRAM | Non-volatile memory concept where startup config is stored. |
| Flash | Persistent storage that may emulate NVRAM on modern devices. |
| `show running-config` | Displays the current active configuration. |
| `show run` | Short form of `show running-config`. |
| `show startup-config` | Displays the saved configuration used on next boot. |
| `write erase` | Erases the saved startup configuration. |
| `erase startup-config` | Erases the saved startup configuration. |
| `reload` | Reboots the device. |
| Factory reset | Returning device to default/unconfigured state. |
| Decommissioning | Removing a device from service, often wiping old configuration. |

## Questions

### 1. Where does running configuration live?

In RAM.

### 2. Where does startup configuration live conceptually?

In NVRAM, though modern devices may emulate that storage with flash.

### 3. What does `show running-config` display?

The configuration active right now.

### 4. What does `show startup-config` display?

The saved configuration the device will load at next boot.

### 5. Why can old hostname still appear after `write erase`?

Because `write erase` removes startup config, but running config is still active in RAM.

### 6. What command reboots the device?

`reload`.

### 7. What happens after erasing startup config and reloading?

The device boots without the old saved configuration and returns to a default/unconfigured state.

### 8. What should you answer if IOS asks to save before reload during a wipe?

Answer `no`.

### 9. Why is answering `yes` dangerous during reset?

It saves the current running config back into startup config, bringing old settings back after reboot.

### 10. Why reset devices in a lab?

To get a clean slate after configuring, breaking, testing and learning.

### 11. Why reset devices before decommissioning?

To remove hostnames, passwords, VLANs, management IPs and other business configuration.

### 12. What is the simple memory rule?

Startup config is what the device remembers; running config is what it is doing now.

## What To Review Later

- Running config vs startup config.
- RAM vs NVRAM.
- Flash emulating NVRAM on modern devices.
- `show running-config`.
- `show startup-config`.
- `write erase`.
- `erase startup-config`.
- `reload`.
- Save prompt during reload.
- Reset workflow for labs and decommissioning.
