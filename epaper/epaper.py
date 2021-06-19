DIN = 23
CLK = 18
CS = 5
DC = 22
RST = 21
BUSY = 4

sck = Pin(CLK)
miso = Pin(19)
mosi = Pin(DIN)
dc = Pin(DC)
cs = Pin(CS)
rst = Pin(RST)
busy = Pin(BUSY)
spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=sck, miso=miso, mosi=mosi)
e = epaper1in54.EPD(spi,cs,dc,rst,busy)
e.init()

w = 200
h = 200
x = 0
y = 0
import framebuf
buf = bytearray(w * h // 8)
fb = framebuf.FrameBuffer(buf, w, h, framebuf.MONO_HLSB)
black = 0
white = 1
fb.fill(white)