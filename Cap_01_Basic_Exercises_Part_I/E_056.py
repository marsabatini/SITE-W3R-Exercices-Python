
    # The program gets the height and width of the window console.

def terminalSize():
    import fcntl, termios, struct

    th, tw, hp, wp = struct.unpack('HHH',
                                   fcntl.ioctl(0, termios.TIOCGWINSZ,
                                               struct.pack('HHH', 0, 0, 0, 0)))

    return tw, th

print("Number: ", terminalSize())
