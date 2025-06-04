class DummyImage:
    format = 'JPEG'
    def verify(self):
        pass

class DummyParser:
    def __init__(self):
        self.image = DummyImage()
    def feed(self, data):
        pass

class DummyImageFile:
    Parser = DummyParser

class ImageModule:
    MIME = {'JPEG': 'image/jpeg'}
    EXTENSION = ['.jpg']
    @staticmethod
    def open(fp, mode='r'):
        return DummyImage()
    @staticmethod
    def init():
        pass

Image = ImageModule()
ImageFile = DummyImageFile

def open(fp, mode='r'):
    return DummyImage()
