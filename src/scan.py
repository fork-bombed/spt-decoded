from time import sleep
from flipper.pyflipper import PyFlipper
from nfc_parser import NFC
import os

def find_device() -> PyFlipper:
    for file in os.listdir(os.fsencode('/dev/')):
        filename = os.fsdecode(file)
        if 'tty.usbmodemflip_' in filename: 
            return PyFlipper(f'/dev/{filename}')

def nfc_scan() -> str:
    flipper = find_device()
    device_name = flipper.device_info.info().get('hardware_name')
    print(f'Connected to {device_name}')
    print('Opening NFC app...')
    flipper.loader.open('NFC')
    print('Taking snapshot of NFC file directory')
    files = flipper.storage.list('/ext')
    if 'nfc' in files.get('dirs'):
        nfc_snapshot = [file.get('name') for file in flipper.storage.list('/ext/nfc').get('files')]
        print('Checking for new files...')
        filename = None
        while filename is None:
            directory = [file.get('name') for file in flipper.storage.list('/ext/nfc').get('files')]
            difference = set(directory) ^ set(nfc_snapshot)
            if difference:
                filename = difference.pop()
            sleep(1)
        print(f'File found {filename}')
        data = flipper.storage.read(f'/ext/nfc/{filename}')
        card = NFC(data)
        # Delete temporary file
        print('Deleting temporary file')
        flipper.storage.remove(f'/ext/nfc/{filename}')
        return card.data
    
