# Generated by h2py from /usr/include/termios.h

# Included from features.h
_FEATURES_H = 1
_GNU_SOURCE = 1
__USE_ANSI = 1
__FAVOR_BSD = 1
_BSD_SOURCE = 1
_SVID_SOURCE = 1
_POSIX_SOURCE = 1
_POSIX_C_SOURCE = 2
__USE_POSIX = 1
__USE_POSIX2 = 1
__USE_MISC = 1
__USE_BSD = 1
__USE_SVID = 1
__USE_GNU = 1
__GNU_LIBRARY__ = 1

# Included from sys/cdefs.h
_SYS_CDEFS_H = 1
def __P(args): return args	 

def __P(args): return args

def __P(args): return ()	 

def __STRING(x): return #x

def __STRING(x): return "x"


# Included from sys/types.h

# Included from linux/types.h
__FD_SETSIZE = 256

# Included from asm/types.h
def __FD_ZERO(fdsetp): return \


# Included from sys/bitypes.h

# Included from linux/termios.h

# Included from asm/termios.h
TCGETS = 0x5401
TCSETS = 0x5402
TCSETSW = 0x5403
TCSETSF = 0x5404
TCGETA = 0x5405
TCSETA = 0x5406
TCSETAW = 0x5407
TCSETAF = 0x5408
TCSBRK = 0x5409
TCXONC = 0x540A
TCFLSH = 0x540B
TIOCEXCL = 0x540C
TIOCNXCL = 0x540D
TIOCSCTTY = 0x540E
TIOCGPGRP = 0x540F
TIOCSPGRP = 0x5410
TIOCOUTQ = 0x5411
TIOCSTI = 0x5412
TIOCGWINSZ = 0x5413
TIOCSWINSZ = 0x5414
TIOCMGET = 0x5415
TIOCMBIS = 0x5416
TIOCMBIC = 0x5417
TIOCMSET = 0x5418
TIOCGSOFTCAR = 0x5419
TIOCSSOFTCAR = 0x541A
FIONREAD = 0x541B
TIOCINQ = FIONREAD
TIOCLINUX = 0x541C
TIOCCONS = 0x541D
TIOCGSERIAL = 0x541E
TIOCSSERIAL = 0x541F
TIOCPKT = 0x5420
FIONBIO = 0x5421
TIOCNOTTY = 0x5422
TIOCSETD = 0x5423
TIOCGETD = 0x5424
TCSBRKP = 0x5425
TIOCTTYGSTRUCT = 0x5426
FIONCLEX = 0x5450
FIOCLEX = 0x5451
FIOASYNC = 0x5452
TIOCSERCONFIG = 0x5453
TIOCSERGWILD = 0x5454
TIOCSERSWILD = 0x5455
TIOCGLCKTRMIOS = 0x5456
TIOCSLCKTRMIOS = 0x5457
TIOCSERGSTRUCT = 0x5458
TIOCSERGETLSR = 0x5459
TIOCSERGETMULTI = 0x545A
TIOCSERSETMULTI = 0x545B
TIOCPKT_DATA = 0
TIOCPKT_FLUSHREAD = 1
TIOCPKT_FLUSHWRITE = 2
TIOCPKT_STOP = 4
TIOCPKT_START = 8
TIOCPKT_NOSTOP = 16
TIOCPKT_DOSTOP = 32
NCC = 8
NCCS = 19
VINTR = 0
VQUIT = 1
VERASE = 2
VKILL = 3
VEOF = 4
VTIME = 5
VMIN = 6
VSWTC = 7
VSTART = 8
VSTOP = 9
VSUSP = 10
VEOL = 11
VREPRINT = 12
VDISCARD = 13
VWERASE = 14
VLNEXT = 15
VEOL2 = 16
INIT_C_CC = "\003\034\177\025\004\0\1\0\021\023\032\0\022\017\027\026\0"
IGNBRK = 0000001
BRKINT = 0000002
IGNPAR = 0000004
PARMRK = 0000010
INPCK = 0000020
ISTRIP = 0000040
INLCR = 0000100
IGNCR = 0000200
ICRNL = 0000400
IUCLC = 0001000
IXON = 0002000
IXANY = 0004000
IXOFF = 0010000
IMAXBEL = 0020000
OPOST = 0000001
OLCUC = 0000002
ONLCR = 0000004
OCRNL = 0000010
ONOCR = 0000020
ONLRET = 0000040
OFILL = 0000100
OFDEL = 0000200
NLDLY = 0000400
NL0 = 0000000
NL1 = 0000400
CRDLY = 0003000
CR0 = 0000000
CR1 = 0001000
CR2 = 0002000
CR3 = 0003000
TABDLY = 0014000
TAB0 = 0000000
TAB1 = 0004000
TAB2 = 0010000
TAB3 = 0014000
XTABS = 0014000
BSDLY = 0020000
BS0 = 0000000
BS1 = 0020000
VTDLY = 0040000
VT0 = 0000000
VT1 = 0040000
FFDLY = 0100000
FF0 = 0000000
FF1 = 0100000
CBAUD = 0010017
B0 = 0000000
B50 = 0000001
B75 = 0000002
B110 = 0000003
B134 = 0000004
B150 = 0000005
B200 = 0000006
B300 = 0000007
B600 = 0000010
B1200 = 0000011
B1800 = 0000012
B2400 = 0000013
B4800 = 0000014
B9600 = 0000015
B19200 = 0000016
B38400 = 0000017
EXTA = B19200
EXTB = B38400
CSIZE = 0000060
CS5 = 0000000
CS6 = 0000020
CS7 = 0000040
CS8 = 0000060
CSTOPB = 0000100
CREAD = 0000200
PARENB = 0000400
PARODD = 0001000
HUPCL = 0002000
CLOCAL = 0004000
CBAUDEX = 0010000
B57600 = 0010001
B115200 = 0010002
B230400 = 0010003
CIBAUD = 002003600000
CRTSCTS = 020000000000
ISIG = 0000001
ICANON = 0000002
XCASE = 0000004
ECHO = 0000010
ECHOE = 0000020
ECHOK = 0000040
ECHONL = 0000100
NOFLSH = 0000200
TOSTOP = 0000400
ECHOCTL = 0001000
ECHOPRT = 0002000
ECHOKE = 0004000
FLUSHO = 0010000
PENDIN = 0040000
IEXTEN = 0100000
TIOCM_LE = 0x001
TIOCM_DTR = 0x002
TIOCM_RTS = 0x004
TIOCM_ST = 0x008
TIOCM_SR = 0x010
TIOCM_CTS = 0x020
TIOCM_CAR = 0x040
TIOCM_RNG = 0x080
TIOCM_DSR = 0x100
TIOCM_CD = TIOCM_CAR
TIOCM_RI = TIOCM_RNG
TIOCSER_TEMT = 0x01
TCOOFF = 0
TCOON = 1
TCIOFF = 2
TCION = 3
TCIFLUSH = 0
TCOFLUSH = 1
TCIOFLUSH = 2
TCSANOW = 0
TCSADRAIN = 1
TCSAFLUSH = 2
N_TTY = 0
N_SLIP = 1
N_MOUSE = 2
N_PPP = 3
def CTRL(ch): return ((ch)&0x1F)

IBSHIFT = 16
CNUL = 0
CDEL = 0177
CESC = ord('\\')
CINTR = 0177
CQUIT = 034
CERASE = ord('#')
CKILL = ord('@')
CEOT = 04
CEOL = 0
CEOL2 = 0
CEOF = 4
CSTART = 021
CSTOP = 023
CSWTCH = 032
NSWTCH = 0
CSUSP = CTRL(ord('Z'))
CDSUSP = CTRL(ord('Y'))
CRPRNT = CTRL(ord('R'))
CFLUSH = CTRL(ord('O'))
CWERASE = CTRL(ord('W'))
CLNEXT = CTRL(ord('V'))
