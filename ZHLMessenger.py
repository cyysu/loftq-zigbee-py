# -*- coding: utf-8 -*-
HL_START_CHAR   0x01
HL_ESC_CHAR     0x02
HL_END_CHAR     0x03

class ZHLMessenger:
    def __init__(self):
        pass

    def init(self):
        self.ser = MxSerial()
        self.ser.open()
        return

    def fini(self):
        self.ser.close()
        return

    def _gen_crc8(self, data):
        """ generate crc8 of data """

        return

    def _tx_byte(self, cbyte, split=True):
        """ output single byte """
        data = []

        if(!split and cbyte < 0x10):
            cbyte ^= 0x10
            data.append(HL_ESC_CHAR)

        data.append(cbyte)

        return self.ser.write(bytearray(data))

