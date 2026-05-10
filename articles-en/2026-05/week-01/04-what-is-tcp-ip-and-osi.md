# What is TCP/IP and OSI?

Source: private course page  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 03  
Tags: tcp-ip, osi, models, layers, networking fundamentals

## Summary

The TCP/IP and OSI models help explain how network communication is broken into layers. Instead of treating networking as one giant mystery, these models split the process into smaller responsibilities.

Main idea: models are not the network itself. They are mental maps that help you understand, troubleshoot and talk about networking clearly.

## Key Points

- TCP/IP is the practical model used for modern networking.
- OSI is a reference model often used for learning and troubleshooting.
- Layered models break communication into smaller parts.
- Each layer has a role.
- Encapsulation adds information as data moves down the stack.
- Decapsulation removes information as data moves back up.
- The models help identify where a problem may be happening.

## Notes

### Why Models Matter

Without a model, network communication feels like one huge process. With layers, we can ask better questions:

- Is the cable working?
- Does the device have an IP address?
- Is routing correct?
- Is the application responding?

### OSI Model

The OSI model has seven layers:

```text
7 Application
6 Presentation
5 Session
4 Transport
3 Network
2 Data Link
1 Physical
```

### TCP/IP Model

The TCP/IP model is usually shown with fewer layers and maps more directly to how the internet works.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| OSI | Seven-layer reference model. |
| TCP/IP | Practical networking model used by the internet. |
| Encapsulation | Adding headers as data moves down the stack. |
| Decapsulation | Removing headers as data moves up the stack. |

## Questions

### Why learn network models?

They give you a structured way to understand and troubleshoot communication.

### Is OSI a real protocol stack?

It is mostly a reference model for learning and discussion.

## What To Review Later

- OSI layers.
- TCP/IP layers.
- Encapsulation.
- Troubleshooting by layer.
