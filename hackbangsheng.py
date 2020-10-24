import json
import hashlib
from urllib import request


fuzzdict = ['wifiMacAddress', 'IMEI', 'serial']

tmplete = "{'parameters': 'notExist', 'coordinates': '[0.0,0.0]', 'cellularIP':'10.57.244.127', 'stat': 'isContent', 'brand': 'Android', 'model': 'AOSPonBullHead', 'UDID': 'NIMRCDv3ECEMSLZ4Mrdy4a4Ls9TqJrdZ', 'syncookies': 'notExist', 'availableMemory': '711258112', 'switch': 'isContent', 'hardware': 'bullhead', 'host': 'nikodeMacBook-Pro.local', 'tags': '2333', 'wifiList': '[TONGDUN-PHONE,38:17:c3:c0:06:c4,WPA2-PSK-CCMPESS,TONGDUNXY,38:17:c3:c0:06:c6,WPA2-PSK-CCMPESS,TONGDUN-GUEST,38:17:c3:c0:06:c1,WPA2-PSK-CCMPESS,TONGDUN-TEST,38:17:c3:c0:06:c3,WPA2-EAP-CCMPESS,TONGDUN,38:17:c3:c0:06:c0,WPA2-EAP-CCMPESS,TONGDUN-MODEL,38:17:c3:c0:06:c2,WPA2-PSK-CCMPESS,TONGDUNXY,38:17:c3:c0:06:d6,WPA2-PSK-CCMPESS,TONGDUN-PHONE,38:17:c3:c0:06:d4,WPA2-PSK-CCMPESS,TONGDUN-MODEL,38:17:c3:c0:06:d2,WPA2-PSK-CCMPESS,TONGDUN-GUEST,38:17:c3:c0:06:d1,WPA2-PSK-CCMPESS,TONGDUN,38:17:c3:c0:06:d0,WPA2-EAP-CCMPESS,TONGDUN-TEST,38:17:c3:c0:06:d3,WPA2-EAP-CCMPESS,,38:17:c3:c0:06:d5,WPA2-EAP-CCMPESS,TONGDUN-GUEST,38:17:c3:c0:09:01,WPA2-PSK-CCMPESS,TONGDUN-MODEL,38:17:c3:c0:09:02,WPA2-PSK-CCMPESS,TONGDUN-PHONE,38:17:c3:c0:09:14,WPA2-PSK-CCMPESS,TONGDUN-TEST,38:17:c3:c0:09:13,WPA2-EAP-CCMPESS,TONGDUN-MODEL,38:17:c3:c0:09:12,WPA2-PSK-CCMPESS,TONGDUN-GUEST,38:17:c3:c0:09:11,WPA2-PSK-CCMPESS,TONGDUN,38:17:c3:c0:09:10,WPA2-EAP-CCMPESS,TONGDUNXY,38:17:c3:c0:09:16,WPA2-PSK-CCMPESS]', 'device': 'bullhead', 'availableSD': '0', 'uevent': 'isContent', 'product': 'aosp_bullhead', 'radio': 'M8994F-2.6.30.0.68', 'serial': '0101168e5e533109', 'battery': '[2,89]', 'brightness': '255', 'displayRom': 'aosp_bullhead-userdebug8.1.0OPM3.171019.013eng.niko.20180801.1140082333', 'networkType': 'WiFi', 'ppp': 'isContent', 'totalSystem': '11521290240', 'userAgent': 'Dalvik/2.1.0(Linux;U;Android8.1.0;AOSPonBullHeadBuild/OPM3.171019.013)', 'custID': '133', 'existPipe': '0', 'totalMemory': '1902940160', 'algID': 'ANDAlg', 'adb': 'notExist', 'manufacturer': 'LGE', 'totalSD': '0', 'platform': 'AND', 'rooted': '1', 'isProxy': '1', 'time': '0', 'currentWifi': '[\"TONGDUN\",38:17:c3:c0:06:d0]', 'fingerprint': 'Android/aosp_bullhead/bullhead:8.1.0/OPM3.171019.013/niko08011140:userdebug/2333', 'id': 'OPM3.171019.013', 'hashCode': '0tIBrpogiFFSFyG3piN6uZN2BJ6ZESjZEAN8aIaDN3Q', 'timeZone': '[GMT+08:00,Asia/Shanghai]', 'timestamp': '1547507278461', 'bootloader': 'BHZ10k', 'availableSystem': '984272896', 'type': 'userdebug', 'wifiMacAddress': '64:BC:0C:83:CE:92', 'cpuABI': 'arm64-v8aarmeabi-v7aarmeabi', 'isVPN': '0', 'cpufreq': 'isContent', 'startupTime': '1547437106', 'board': 'bullhead', 'version': '8.1.0', 'IMEI': '354360070135439', 'existQemu': '0', 'sdkVersion': '4.2.2.1', 'misc': 'isContent', 'resolution': '[2.625,1080,1794,2.625,422.03,424.069]', 'IOPorts': 'isContent'}"
changedict = json.load(open('./change.json', 'r'))

basedata = ""

dictvalue = ""


def restore(dictdata):
    mapkeys = changedict.keys()
    mapvalues = changedict.values()
    dictx = {}
    for key in dictdata.keys():
        if key in mapvalues:
            for src, new in changedict.items():
                if key == new:
                    dictx[str(src)] = str(dictdata[key])
        else:
            dictx[key] = dictdata[key]
    return dictx


def changename(dictdata):
    mapkeys = changedict.keys()
    mapvalues = changedict.values()
    dictx = {}
    for key in dictdata.keys():
        if key in mapkeys:
            for src, new in changedict.items():
                if key == src:
                    dictx[new] = dictdata[key]
        else:
            dictx[key] = dictdata[key]
    # print(dictx)
    return dictx


def postdata(value):
    print(value)
    url = "http://218.13.4.182:9200/public/generate/post"
    requestx = request.Request(url)
    requestx.add_header("Content-Type", "application/json")
    requestx.add_header("Accept-Encoding", "gzip, deflate")
    requestx.add_header("User-Agent", "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus 5 Build/MMB29S)")
    requestx.add_header('Host', '218.13.4.182:9200')
    f = request.urlopen(requestx, value.encode('utf-8'))
    ret = f.read().decode()
    print(ret)
    return ret


def bangshengbyte2hex(bytedata):
    strx = ''
    lens = len(bytedata)
    index = 0
    v0 = 0
    v1 = 0
    kuan = 6
    encmap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
    while index < lens:
        v0 += 8
        tmp = v1 << 8
        tmp2 = (bytedata[index] << (0x20 - v0) & 0xffffffff) >> (0x20 - v0)
        v1 = tmp + tmp2
        while v0 >= kuan:
            index2 = v1 >> v0 - kuan
            strx += encmap[index2]
            v0 -= kuan
            if v0 == 0:
                v1 = 0
            else:
                v1 = ((v1 << (0x20-v0)) & 0xffffffff) >> 0x20 - v0
        index += 1
    if v0 > 0:
        strx += encmap[v1 << 6 - v0]
    print(strx)
    return strx


def calchash(dictdata):
    keys = sorted(dictdata.keys())
    if 'algID' in keys:
        keys.remove('algID')
    if 'timestamp' in keys:
        keys.remove('timestamp')
    if 'hashCode' in keys:
        keys.remove('hashCode')
    strdata = ''
    for key in keys:
        strdata += key+dictdata[key]
    # strdata='IMEI=355637051875045&IOPorts=f9017000-f9017fff:msm-watchdog&adb=isContent&availableMemory=571682816&availableSD=0&availableSystem=505225216&battery=[5,100]&bluetooth=00:19:E8:B4:76:AE&board=hammerhead&bootloader=HHZ12k&brand=google&brightness=55&cellularIP=10.57.242.135&coordinates=[0.0,0.0]&cpuABI=armeabi-v7aarmeabi&cpufreq=isContent&currentWifi=["TONGDUN",38:17:c3:c0:06:d0]&custID=133&device=hammerhead&displayRom=MMB29S&existPipe=0&existQemu=0&fingerprint=google/hammerhead/hammerhead:6.0.1/MMB29S/2489379:user/release-keys&hardware=hammerhead&host=wpiy12.hot.corp.google.com&id=MMB29S&isProxy=1&isVPN=0&manufacturer=LGE&misc=39network_throughput40network_latency41cpu_dma_latency42ramdump_smem43xt_qtaguid44ramdump_audio-ocmem45msm_rtac46msm_acdb47ashmem48binder49uhid236device-mapper50epm_adc51alarm223uinput52keychord53rmnet_ctrl54usb_accessory55android_rndis_qc56mtp_usb57ccid_bulk58ccid_ctrl59laf60android_adb61rmnet_mux_ctrl62android_mbim63bcm2079x200tun64tgt237loop-control183hw_random229fuse65usf166msm_amrwb_in67msm_qcelp68msm_evrc69msm_amrwbplus70msm_amrwb71msm_amrnb72msm_mp373msm_multi_aac74msm_aac75msm_wmapro76msm_wma77msm_amrnb_in78msm_evrc_in79msm_qcelp_in80msm_aac_in81dsp_debug82nmea83qmi284qmi185qmi086smem_log87subsys_venus88ramdump_venus89ramdump_smem-modem90ramdump_modem91subsys_modem92subsys_adsp93ramdump_adsp94rfkill95ion&model=Nexus5&networkType=WiFi&parameters=isContent&platform=AND&ppp=isContent&product=hammerhead&radio=M8974A-2.0.50.2.28&resolution=[3.0,1080,1776,3.0,442.451,443.345]&rooted=1&sdkVersion=4.2.2.1&serial=0b18449943bf22d5&startupTime=1554374919&stat=isContent&switch=isContent&syncookies=notExist&tags=release-keys&time=0&timeZone=[GMT+08:00,Asia/Shanghai]&totalMemory=1945096192&totalSD=0&totalSystem=7719415808&type=user&uevent=MAJOR10MINOR41DEVNAMEcpu_dma_latency&userAgent=Dalvik/2.1.0(Linux;U;Android6.0.1;Nexus5Build/MMB29S)&version=6.0.1&wifiList=yKbVsr,00:05:31:DC:8F:2B,QdQO6JrU,GLYFMwpv,00:17:CC:E8:52:D2,TOLQAvEU&wifiMacAddress=00:21:5C:93:C7:ED'.replace('=','').replace('&','')
    print(len(strdata))
    # hash
    md5data = hashlib.md5(strdata.encode('utf-8')).digest()
    sha256data = hashlib.sha256(md5data).digest()
    ret = bangshengbyte2hex(sha256data)
    dictdata['hashCode'] = ret


def main():
    srcdict = restore(json.load(open('./mynew.json')))
    if 'UDID' in srcdict:
        srcdict.pop('UDID')
    srcdict['IMEI'] = '354637153777254'
    srcdict['wifiMacAddress'] = "92:63:6b:66:17:26"
    srcdict['bluetooth'] = '25:81:8e:87:13:51'
    srcdict['wifiList'] = '[\"23\":12:23:12:6d:5e:5c]'
    calchash(srcdict)
    newdict = changename(srcdict)
    # strs=json.load(open('./mynew.json','r'))
    ret = postdata(json.dumps(newdict))
    jsondata = json.loads(ret)


if __name__ == "__main__":
    main()
