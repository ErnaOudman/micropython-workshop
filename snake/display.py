from machine import SPI, Pin, SoftSPI
import st7789

BL_Pin = 4  # backlight pin
SCLK_Pin = 18  # clock pin
MOSI_Pin = 19  # mosi pin
MISO_Pin = 2  # miso pin
RESET_Pin = 23  # reset pin
DC_Pin = 16  # data/command pin
CS_Pin = 5  # chip select pin

Pin(BL_Pin, Pin.OUT).on()

# spi = SPI()
spi = SoftSPI(
    baudrate=80000000,
    miso=Pin(MISO_Pin),
    mosi=Pin(MOSI_Pin, Pin.OUT),
    sck=Pin(SCLK_Pin, Pin.OUT),
)

display = st7789.ST7789(
    spi,
    135,
    240,
    cs=Pin(CS_Pin, Pin.OUT),
    dc=Pin(DC_Pin, Pin.OUT),
    reset=Pin(RESET_Pin, Pin.OUT),
)
display.init()
print("display initialized")

