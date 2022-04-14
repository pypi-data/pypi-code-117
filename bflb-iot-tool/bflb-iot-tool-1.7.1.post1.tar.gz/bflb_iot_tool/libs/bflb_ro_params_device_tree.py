# -*- coding: utf-8 -*-
#  Copyright (C) 2021- BOUFFALO LAB (NANJING) CO., LTD.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.


import os
import binascii

from libs import bflb_utils
from libs import bflb_fdt as fdt
from libs.bflb_utils import app_path, string_to_bytearray


def little_endian(data):
    return binascii.hexlify(binascii.unhexlify(data)[::-1]).decode('utf-8')


def bl_dts2dtb(src_addr="", dest_addr=""):
    if "" == src_addr or "" == dest_addr:
        bflb_utils.printf("bl_dts2dtb please check arg.")
        return
    bflb_utils.printf("=========", src_addr, " ——> ", dest_addr, "=========")
    with open(src_addr, "r", encoding='utf-8') as f:
        tmp1_dts = f.read()
    tmp2_dtb = fdt.parse_dts(tmp1_dts)
    dest_addr = os.path.join(app_path, dest_addr)
    with open(dest_addr, "wb") as f:
        f.write(tmp2_dtb.to_dtb(version=17))


def bl_ro_params_device_tree(in_dts_config, out_bin_file):
    dts_config = in_dts_config
    bin_file = out_bin_file
    bl_dts2dtb(dts_config, bin_file)


def bl_dts2hex(dts):
    with open(dts, "r", encoding='utf-8') as f:
        tmp_dts = f.read()
    fdt_obj = fdt.parse_dts(tmp_dts)
    
    xtal_mode = ""
    xtal = ""
    pwr_mode = ""
    pwr_table_11b = ""
    pwr_table_11g = ""
    pwr_table_11n = ""
    pwr_offset = ""
    en_tcal = ""
    linear_or_follow = ""
    tchannels = ""
    tchannel_os = ""
    tchannel_os_low = ""
    troom_os = ""
    pwr_table_ble = ""

    if fdt_obj.exist_node("wifi/brd_rf"):
        xtal_mode = fdt_obj.get_property("xtal_mode", "wifi/brd_rf")
        xtal = fdt_obj.get_property("xtal", "wifi/brd_rf")
        pwr_mode = fdt_obj.get_property("pwr_mode", "wifi/brd_rf")
        pwr_offset = fdt_obj.get_property("pwr_offset", "wifi/brd_rf")
        pwr_table_11b = fdt_obj.get_property("pwr_table_11b", "wifi/brd_rf")
        pwr_table_11g = fdt_obj.get_property("pwr_table_11g", "wifi/brd_rf")
        pwr_table_11n = fdt_obj.get_property("pwr_table_11n", "wifi/brd_rf")
    if fdt_obj.exist_node("wifi/rf_temp"):
        en_tcal = fdt_obj.get_property("en_tcal", "wifi/rf_temp")
        linear_or_follow = fdt_obj.get_property("linear_or_follow", "wifi/rf_temp")
        tchannels = fdt_obj.get_property("Tchannels", "wifi/rf_temp")
        tchannel_os = fdt_obj.get_property("Tchannel_os", "wifi/rf_temp")
        tchannel_os_low = fdt_obj.get_property("Tchannel_os_low", "wifi/rf_temp")
        troom_os = fdt_obj.get_property("Troom_os", "wifi/rf_temp")
    if fdt_obj.exist_node("bluetooth/brd_rf"):
        pwr_table_ble = fdt_obj.get_property("pwr_table_ble", "bluetooth/brd_rf")

    init_hex = little_endian(string_to_bytearray("k1bXkD6O").hex())

    if xtal_mode:
        length = '%02x' % len(xtal_mode[0])
        xtal_mode_hex = "0100" + length + "00" + string_to_bytearray(xtal_mode[0]).hex()
    else:
        xtal_mode_hex = ""
    
    if xtal:
        xtal_hex = "02001400"
        for item in xtal:
            item_hex = little_endian('%08x' % item)
            xtal_hex += item_hex
    else:
        xtal_hex = ""
    
    if pwr_mode:
        length = '%02x' % len(pwr_mode[0])
        pwr_mode_hex = "0300" + length + "00" + string_to_bytearray(pwr_mode[0]).hex()
    else:
        pwr_mode_hex = ""
    
    if pwr_table_11b:
        pwr_table_11b_hex = "05000400"
        for item in pwr_table_11b:
            item_hex = '%02x' % item
            pwr_table_11b_hex += item_hex
    else:
        pwr_table_11b_hex = ""

    if pwr_table_11g:
        pwr_table_11g_hex = "06000800"
        for item in pwr_table_11g:
            item_hex = '%02x' % item
            pwr_table_11g_hex += item_hex
    else:
        pwr_table_11g_hex = ""

    if pwr_table_11n:
        pwr_table_11n_hex = "07000800"
        for item in pwr_table_11n:
            item_hex = '%02x' % item
            pwr_table_11n_hex += item_hex
    else:
        pwr_table_11n_hex = ""

    if pwr_offset:
        pwr_offset_hex = "08000e00"
        for item in pwr_offset:
            item_hex = '%02x' % item
            pwr_offset_hex += item_hex
    else:
        pwr_offset_hex = ""
    
    if en_tcal:
        en_tcal_hex = "20000100%02x" % en_tcal[0]
    else:
        en_tcal_hex = ""
    
    if linear_or_follow:
        linear_or_follow_hex = "21000100%02x" % linear_or_follow[0]
    else:
        linear_or_follow_hex = ""

    if tchannels:
        tchannels_hex = "22000a00"
        for item in tchannels:
            item_hex = little_endian('%04x' % item)
            tchannels_hex += item_hex
    else:
        tchannels_hex = ""

    if tchannel_os:
        tchannel_os_hex = "23000a00"
        for item in tchannel_os:
            item_hex = little_endian('%04x' % item)
            tchannel_os_hex += item_hex
    else:
        tchannel_os_hex = ""
        
    if tchannel_os_low:
        tchannel_os_low_hex = "24000a00"
        for item in tchannel_os_low:
            item_hex = little_endian('%04x' % item)
            tchannel_os_low_hex += item_hex
    else:
        tchannel_os_low_hex = ""   
    
    if troom_os:
        troom_os_hex = "25000200" + little_endian("%04x" % troom_os[0])
    else:
        troom_os_hex = ""
    
    if pwr_table_ble:
        pwr_table_ble_hex = "30000400" + little_endian("%08x" % pwr_table_ble[0])
    else:
        pwr_table_ble_hex = ""
    
    dts_hex = init_hex + \
              xtal_mode_hex + xtal_hex + \
              pwr_mode_hex + pwr_table_11b_hex + pwr_table_11g_hex + pwr_table_11n_hex + pwr_offset_hex + \
              en_tcal_hex + linear_or_follow_hex + \
              tchannels_hex + tchannel_os_hex + tchannel_os_low_hex + troom_os_hex + \
              pwr_table_ble_hex

    '''
    dts_hex_little_end = ""
    for item in [dts_hex[i:i+8] for i in range(0, len(dts_hex), 8)]:
        dts_hex_little_end += little_endian(item.ljust(8, '0'))
    '''

    return dts_hex

