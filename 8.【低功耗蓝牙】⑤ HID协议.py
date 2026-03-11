from machine import Pin
import ubluetooth #导入BLE功能模块
from bluetooth import UUID

ble = ubluetooth.BLE()  #创建BLE设备
ble.active(True)  #打开BLE

ble.config(gap_name="ESP Mouse")
ble.config(mtu=23)

HIDS = (                              # Service description: describes the service and how we communicate
    UUID(0x1812),                     # Human Interface Device
    (
        (UUID(0x2A4A), ubluetooth.FLAG_READ),       # HID information
        (UUID(0x2A4B), ubluetooth.FLAG_READ),       # HID report map
        (UUID(0x2A4C), ubluetooth.FLAG_WRITE),      # HID control point
        (UUID(0x2A4D), ubluetooth.FLAG_READ | ubluetooth.FLAG_NOTIFY, ((UUID(0x2908), 1),)),  # HID report / reference
        (UUID(0x2A4D), ubluetooth.FLAG_READ | ubluetooth.FLAG_WRITE,  ((UUID(0x2908), 1),)),  # HID report / reference
        (UUID(0x2A4E), ubluetooth.FLAG_READ | ubluetooth.FLAG_WRITE), # HID protocol mode
    ),
)

services = (HIDS,)
handles = ble.gatts_register_services(services)

MOUSE_REPORT = bytes([    # Report Description: describes what we communicate
            0x05, 0x01,   # USAGE_PAGE (Generic Desktop)
            0x09, 0x02,   # USAGE (Mouse)
            0xa1, 0x01,   # COLLECTION (Application)
            0x85, 0x01,   #   REPORT_ID (1)
            0x09, 0x01,   #   USAGE (Pointer)
            0xa1, 0x00,   #   COLLECTION (Physical)
            0x05, 0x09,   #         Usage Page (Buttons)
            0x19, 0x01,   #         Usage Minimum (1)
            0x29, 0x03,   #         Usage Maximum (3)
            0x15, 0x00,   #         Logical Minimum (0)
            0x25, 0x01,   #         Logical Maximum (1)
            0x95, 0x03,   #         Report Count (3)
            0x75, 0x01,   #         Report Size (1)
            0x81, 0x02,   #         Input(Data, Variable, Absolute); 3 button bits
            0x95, 0x01,   #         Report Count(1)
            0x75, 0x05,   #         Report Size(5)
            0x81, 0x03,   #         Input(Constant);                 5 bit padding
            0x05, 0x01,   #         Usage Page (Generic Desktop)
            0x09, 0x30,   #         Usage (X)
            0x09, 0x31,   #         Usage (Y)
            0x09, 0x38,   #         Usage (Wheel)
            0x15, 0x81,   #         Logical Minimum (-127)
            0x25, 0x7F,   #         Logical Maximum (127)
            0x75, 0x08,   #         Report Size (8)
            0x95, 0x03,   #         Report Count (3)
            0x81, 0x06,   #         Input(Data, Variable, Relative); 3 position bytes (X,Y,Wheel)
            0xc0,         #   END_COLLECTION
            0xc0          # END_COLLECTION
        ])

#设置BLE广播数据并开始广播
ble.gap_advertise(100, adv_data = b'\x02\x01\x05'
                                + b'\x03\x03\x12\x18' #HID UUID
                                + b'\x03\x19\xC2\x03' #设备外观为鼠标
                                + b'\x0A\x09' + "ESP Mouse".encode("UTF-8"))

(h_info, h_map, _, h_repin, h_d1, h_repout, h_d2, h_model,) = handles[0]
# Write service characteristics
ble.gatts_write(h_info, b"\x01\x01\x00\x02")     # HID info: ver=1.1, country=0, flags=normal
ble.gatts_write(h_map, MOUSE_REPORT)    # HID input report map
ble.gatts_write(h_d1, b"\x01\x01")  # HID reference: id=1, type=input
ble.gatts_write(h_d2, b"\x01\x02")  # HID reference: id=1, type=output
ble.gatts_write(h_model, b"\x01")   # HID Protocol Model: 0=Boot Model, 1=Report Model


key = Pin(0,Pin.IN)#IO 0 用作按键
while True:
  if key.value() == 0:
    while key.value() == 0:
      pass
    ble.gatts_notify(0, h_repin, b'\x00\x0A\xF6\x00')#X正方向和Y的负方向各移动10像素
    ble.gatts_notify(0, h_repin, b'\x00\x00\x00\x00')#