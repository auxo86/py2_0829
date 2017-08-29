from urllib2 import urlopen
from PIL import Image
url = 'http://www.cwb.gov.tw/V7/observe/satellite/Data/s1p/s1p-2017-08-29-19-30.jpg'
fileToSave = urlopen(url)
image = Image.open(fileToSave)
image.save('normal1.jpg')
halfSize = (image.size[0]/2, image.size[1]/2)
halfImage = image.resize(halfSize, Image.ANTIALIAS)
halfImage.save('small.jpg')
rotation1 = image.transpose(Image.ROTATE_90)
rotation1.save('r90.png')
rotation2 = image.transpose(Image.ROTATE_180)
rotation2.save('r180.png')
rotation3 = image.transpose(Image.ROTATE_270)
rotation3.save('r270.png')