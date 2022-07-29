class NFC:
    def __init__(self, raw):
        self.raw = raw.strip()
        self.uid = self._get_uid()
        self.device_type = self._get_device_type()
        self.data = self._get_data()
    def _get_uid(self):
        return self.raw.split('UID: ')[1].split('\n')[0].strip()
    def _get_device_type(self):
        return self.raw.split('Device type: ')[1].split('\n')[0].strip()
    def _get_data(self):
        page_data = self.raw.split('Pages total: ')[1].split('Failed')[0].strip().split('\n')[1:]
        data = ' '.join([line.split(': ')[1].strip() for line in page_data]).strip()
        return data