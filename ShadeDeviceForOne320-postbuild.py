# This file was generated by Simplicity Studio from the following template:
#   app/esf_common/template/common/common-postbuild.py
# Please do not edit it directly.

# Post Build processing.

import sys
import os
import logging
import re

# This returns the windows short path name
def shortPath(pathName):
    if ((not (START_FLAGS or WINE.strip())) 
        and ' ' in pathName and (os.path.isdir(pathName)
        or os.path.isfile(pathName))):
        command = "for %I in ( \"" + pathName + "\" ) do @echo %~fsI"
        shortNameProcess = os.popen(command,"r")
        shortPathName = shortNameProcess.read()
        shortNameProcess.close()
        return shortPathName.replace("\n","")
    else:
        return pathName

def S37():
    print " "
    print "This converts an IAR .out to 32 bit Motorola S-record image"
    print " "
    if ("gcc" == "iar" or "gcc" == ""):
        MOTOROLLA_32_BIT_COMMAND = WINE + "\"" + TOOLCHAIN_DIR + \
            "/bin/ielftool.exe\" " + OUT_FILE + " --srec --srec-s3only " + S37_BINARY
    else:
        GCC_TOOLCHAIN_PATH = shortPath(r"file:/D:/soft/SiliconLabs/SimplicityStudio/v4/developer/toolchains/gnu_arm/7.2_2017q4/".replace(
            "file:", "").replace("%20", " "))
        if (GCC_TOOLCHAIN_PATH != "" and os.path.exists(
                GCC_TOOLCHAIN_PATH[1:])):
            GCC_TOOLCHAIN_PATH = GCC_TOOLCHAIN_PATH[1:]
        MOTOROLLA_32_BIT_COMMAND = "\"" + GCC_TOOLCHAIN_PATH + \
            "bin/arm-none-eabi-objcopy\" --srec-forceS3 -O srec " + OUT_FILE + " " + S37_BINARY

    s32RecProcess = os.popen(MOTOROLLA_32_BIT_COMMAND)
    s32RecOutput = s32RecProcess.read();
    s32RecProcess.close()
    print s32RecOutput
    outputFile.write(s32RecOutput)
    logging.info("Creation of 32 bit srec file: " + MOTOROLLA_32_BIT_COMMAND)


def EBL():
    CONVERT_FLAGS = "Z:" + ""
    CONVERT_FLAGS = CONVERT_FLAGS.replace("Z:", "")
    if "" == "":
        EBL_FILE = "\"" + os.path.join(TARGET_BPATH + ".ebl") + "\""
    else:
        CONVERT_FLAGS = CONVERT_FLAGS.replace("\\", "/")
        EBL_FILE = "\"" + os.path.join(TARGET_BPATH + ".ebl.encrypted") + "\""

    print " "
    print "This converts S37 to Ember Bootload File format if a bootloader has been selected in AppBuilder"
    print " "
    EBL_COMMAND = START_FLAGS + shortPath(r"D:\soft\SiliconLabs\SimplicityStudio\v4\developer\adapter_packs\commander\commander.exe").replace(
        " ", "\ ") + " ebl create " + EBL_FILE + " --app " + S37_BINARY + " --device EFR32MG13P732F512GM48 " + CONVERT_FLAGS
    eblProcess = os.popen(EBL_COMMAND)
    eblOutput = eblProcess.read()
    eblProcess.close()
    print eblOutput
    outputFile.write(eblOutput)
    logging.info("Creation of ebl file: " + EBL_COMMAND)
    if os.path.exists(EBL_FILE):
        logging.info("EBL file has been created")


def GBL():
    print " "
    print "This converts S37 to Gecko Bootload File format if a bootloader has been selected in AppBuilder"
    print " "
    print "Note that this GBL file does not use encryption or digital signing.  Please refer to UG266 for more information about enabling these features from your S37 files."
    GBL_FILE = "\"" + os.path.join(TARGET_BPATH + ".gbl") + "\""
    GBL_COMMAND = START_FLAGS + shortPath(r"D:\soft\SiliconLabs\SimplicityStudio\v4\developer\adapter_packs\commander\commander.exe").replace(
        " ", "\ ") + " gbl create " + GBL_FILE + " --app " + S37_BINARY + " --device EFR32MG13P732F512GM48"
    gblProcess = os.popen(GBL_COMMAND)
    gblOutput = gblProcess.read()
    gblProcess.close()
    print gblOutput
    outputFile.write(gblOutput)
    outputFile.write("Note that this GBL file does not use encryption or digital signing.  Please refer to UG266 for more information about enabling these features from your S37 files.")
    logging.info("Creation of gbl file: " + GBL_COMMAND)
    if os.path.exists(GBL_FILE):
        logging.info("GBL file has been created")


def OTA():
    if not '"%PROJECT_DIR%\..\\..\\..\\protocol\\zigbee\\tool\\image-builder\\image-builder-windows.exe" --create "%TARGET_BPATH%.ota" --version 0x42 --manuf-id 0x1254 --image-type 0x0301 --tag-id 0x0000 --tag-file "%TARGET_BPATH%.gbl" --string "EBL ShadeDeviceForOne320"':
        sys.exit(0)
    print " "
    print "This creates a ZigBee OTA file if the OTA Client Policy Plugin has been enabled."
    print "It uses the parameters defined there.  "
    print " "
    # wine needed by postbuild script under studio for mac/linux
    IMAGE_BUILDER = '"%PROJECT_DIR%\..\\..\\..\\protocol\\zigbee\\tool\\image-builder\\image-builder-windows.exe" --create "%TARGET_BPATH%.ota" --version 0x42 --manuf-id 0x1254 --image-type 0x0301 --tag-id 0x0000 --tag-file "%TARGET_BPATH%.gbl" --string "EBL ShadeDeviceForOne320"'.replace("\t", "\\t")
    WINE_CMD = WINE.replace("cmd /C ","") if not "echo" in IMAGE_BUILDER else WINE
    OTA_COMMAND = WINE_CMD + IMAGE_BUILDER
    OTA_COMMAND = OTA_COMMAND.replace("%PROJECT_DIR%", PROJECT_DIR)
    OTA_COMMAND = OTA_COMMAND.replace("%TARGET_BPATH%", TARGET_BPATH)
    otaProcess = os.popen(OTA_COMMAND)
    otaOutput = otaProcess.read()
    otaProcess.close()
    print otaOutput
    outputFile.write(otaOutput)
    logging.info("Creation of ota file: " + OTA_COMMAND)
    if os.path.exists(os.path.join(TARGET_BPATH + ".ota")):
        logging.info("OTA file has been created")


# Stopping postbuild script from running when Bootloader is set to None
if ("APP_GECKO_INFO_PAGE_BTL" == "NULL_BTL"):
    print "NULL Bootloader image detected, not running postbuild process"
    sys.exit(0)

# Extracting parameters to python file
TARGET_BPATH = sys.argv[1].replace("\'", "")
START_FLAGS = sys.argv[3] if len(sys.argv) > 3 else ""
WINE = sys.argv[4] + " " if len(sys.argv) > 4 else ""
PROJECT_DIR = shortPath(sys.argv[2].replace("\'", ""))
TOOLCHAIN_DIR = shortPath(sys.argv[5].replace("\'", ""))

#Applying quotes to the WINE path as necessary
if "cmd /C" in WINE:
    WINE = re.sub(r'(.*wine)(.*)', r'"\1"\2',WINE)

# Extracting the current directory
CURRENT_DIR = os.getcwd() + sys.argv[0]
CURRENT_DIR = CURRENT_DIR.replace("Z:", "")
CURRENT_DIR = CURRENT_DIR.replace("\\", "/")

# Extracting the path to s37 for iar and studio
TARGET_BPATH = TARGET_BPATH.replace("Z:", "")
TARGET_BPATH = TARGET_BPATH.replace("\\", "/")
if os.path.isfile(CURRENT_DIR + "/" + TARGET_BPATH + ".s37"):
    TARGET_BPATH = CURRENT_DIR + "/" + TARGET_BPATH
TARGET_BPATH=shortPath(TARGET_BPATH)
# Getting architecture and output files
ARCHITECTURE_SERIES = "1"
ARCHITECTURE_CONFIGURATION = "3"
S37_BINARY = "\"" + os.path.join(TARGET_BPATH + ".s37") + "\""
OUT_FILE = "\"" + os.path.join(
    TARGET_BPATH +
    ".out") + "\"" if (
        "gcc" == "iar" or "gcc" == "") else "\"" + os.path.join(
            TARGET_BPATH +
    ".axf") + "\""
outputFilePath = TARGET_BPATH + "-commander-convert-output.txt"
outputFile = open(outputFilePath, 'w+')
logging.basicConfig(
    filename=TARGET_BPATH +
    "-postbuild.log",
    level=logging.DEBUG)

# Creating a 32 bit s37 image
if (not "efr32mg13p" or ("efr32mg13p" and not "efr32mg13p".startswith("EM3"))):
    S37()

# Creating ebl/gbl files
if (ARCHITECTURE_SERIES and int(ARCHITECTURE_SERIES) >= 2):
    GBL()
elif (ARCHITECTURE_SERIES and int(ARCHITECTURE_CONFIGURATION) >= 2):
    GBL()
elif(ARCHITECTURE_SERIES and int(ARCHITECTURE_SERIES) == 1 and int(
        ARCHITECTURE_CONFIGURATION) == 1):
    EBL()
    GBL()
else:
    EBL()
# Creating ota files if ota plugins are chosen
OTA()

# close output file
outputFile.close()
