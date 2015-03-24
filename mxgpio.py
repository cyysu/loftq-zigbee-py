# -*- coding: utf-8 -*-

class MxGPIO:
    def __init__(self):
        return

    @staticmethod
    def export(id):
        """ export gpio """
        dir_path = "/sys/class/gpio/export"
        fd = open(dir_path, 'w')
        write(fd, str(id))
        close(fd)
        return

    @staticmethod
    def addOutMode(id):
        """ add output port for gpio """
        dir_path = "/sys/class/gpio/gpio"+str(id)+"/directioin"
        fd = open(dir_path, 'w')
        write(fd,"out")
        close(fd)
        return

    @staticmethod
    def setValue(id, value):
        """ set output value for gpio """
        dir_path = "/sys/class/gpio/gpio" + str(id) + "/value"
        fd = open(dir_path, 'w')
        write(fd, str(value))
        close(fd)
        return
