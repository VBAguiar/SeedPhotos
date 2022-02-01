SeedPhotos
==========

A lib that create image through words

Install
-------
Use poetry or pip for installation: 

    pip install seedphotos

or

    poetry add seedphotos



How to use:
-----------

.. code-block:: python

    from seedphotos.photos import *

    photos = Photos(width=300, height=300, filename='image name', seed='word seed', folder='file folder', format='webp or jpg') # Mandatory parameters to generate the image
    photos.getPhotos() # Download image


With all parameters satisfied it looks like this:

.. code-block:: python
    from seedphotos.photos import *

    photos = Photos(width=300, height=300, filename='image', seed='Brazil', folder='/home/barbosa/test/test', format='jpg')
    photos.getPhotos()
