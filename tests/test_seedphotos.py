import unittest

class test_seedphotos(unittest.TestCase):
    def test_seedphotos(self):
        photos = Photos(width=300, height=300, filename='image', seed='Vinicius-Barbosa', folder='/home/barbosa/', format='jpg')
        photosGetPhotos = photos.getPhotos()

        self.assertEqual(photosGetPhotos, 'OK')

if __name__ == '__main__':
    from sys import path; from pathlib import Path
    path.insert(0, str(Path(__file__).resolve().parent.parent))
    from seedphotos.photos import Photos
    unittest.main()
    