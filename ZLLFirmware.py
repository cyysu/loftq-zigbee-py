# -*- coding: utf-8 -*-

import mxgpio

FW_CMD_FLASH_ERASE_REQUEST                                      = 0x07,
FW_CMD_FLASH_ERASE_RESPONSE	                            = 0x08,
FW_CMD_FLASH_PROGRAM_REQUEST			= 0x09,
FW_CMD_FLASH_PROGRAM_RESPONSE			= 0x0a,
FW_CMD_FLASH_READ_REQUEST		              = 0x0b,
FW_CMD_FLASH_READ_RESPONSE			= 0x0c,
FW_CMD_FLASH_SECTOR_ERASE_REQUEST		= 0x0d,
FW_CMD_FLASH_SECTOR_ERASE_RESPONSE		= 0x0e,
FW_CMD_FLASH_WRITE_STATUS_REGISTER_REQUEST     = 0x0f,
FW_CMD_FLASH_WRITE_STATUS_REGISTER_RESPONSE   = 0x10,
FW_CMD_RAM_WRITE_REQUEST			= 0x1d,
FW_CMD_RAM_WRITE_RESPONSE			= 0x1e,
FW_CMD_RAM_READ_REQUEST				= 0x1f,
FW_CMD_RAM_READ_RESPONSE			= 0x20,
FW_CMD_RAM_RUN_REQUEST				= 0x21,
FW_CMD_RAM_RUN_RESPONSE			= 0x22,
FW_CMD_FLASH_READ_ID_REQUEST			= 0x25,
FW_CMD_FLASH_READ_ID_RESPONSE			= 0x26,
FW_CMD_SET_BAUD_REQUEST				= 0x27,
FW_CMD_SET_BAUD_RESPONSE			= 0x28,
FW_CMD_FLASH_SELECT_TYPE_REQUEST		= 0x2c,
FW_CMD_FLASH_SELECT_TYPE_RESPONSE		= 0x2d,

FW_CMD_GET_CHIPID_REQUEST                                         = 0x32,
FW_CMD_GET_CHIPID_RESPONSE                                       = 0x33,

class ZLLFirmware:
    def __init__(self):
        return

    def init(self, port, baudrate):
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate,
        self.ser.port = port
        self.timeout = None

        if(self.ser.isOpen()):
            self.ser.close()
            self.ser.open()
        else:
            self.ser.open()
        return

    def _ser_read(self, number):
        """ read number of bytes """
        return self.ser.read(number)

    def _ser_write(self, data):
        """ write to serial, data type: bytes or bytearray """
        return self.ser.write(data)

    def _requestMsg(self):
        # write msg
        # read msg
        return

    def _readMsg(self, type):
        """ read msg from serial """
        # read length of bytes
        # read rest of msg
        # caculate checksum
        # return data
        return

    def _msg_csum(self, data):
        csum = 0
        for ii in data:
            csum ^= ii
        return csum

    def _msg_pack(self, dtype, dheader, dpayload):
        # msg length can't be over 0xff
        assert(len(dheader) + len(dpayload) >= 0xfe)
        data = []
        # msg length
        data += [len(dheader)+len(dpayload)+2]
        # msg type
        data += [dtype]
        # header
        data += dheader
        # payload
        data += dpayload
        # csum
        data += [self._msg_csum(data)]
        return data

    def _msg_unpack(self, msg):

        return

    def _writeMsg(self, dtype, dheader, dpayload):
        """ write msg to zigbee chip by serial """

        # caculate msg length && import length
        data = self._msg_pack(dtype, dheader, dpayload)

        # import msg type

        # import msg header

        # import payload

        # caculate checksum and import it

        # send msg

        return

    def fini():
        self.ser.close()
        return
