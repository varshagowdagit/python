#adb 
# from ppadb.client import Client as AdbClient
# # Default is "127.0.0.1" and 5037
# client = AdbClient(host="127.0.0.1", port=5037)
# print(client.version())
# device = client.device("emulator-5554")

from ppadb.client import Client as AdbClient
# Connect to ADB server
adb = AdbClient(host="127.0.0.1", port=5037)
# Get the list of connected devices
devices = adb.devices()

if len(devices) == 0:
    print("No devices connected")
else:
    # Perform actions on the connected device
    device = devices[0]
    print(f"Connected to {device.serial}")

    # Example: Get device properties
    print(f"Device properties: {device.get_properties()}")

    # Example: Run ADB shell command
    result = device.shell("pm list packages")
    print(f"Installed packages: {result}")
