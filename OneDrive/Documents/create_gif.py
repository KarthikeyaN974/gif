import imageio.v3 as iio

filenames = ["C:/Users/karth/Downloads/team-pic1.png", "C:/Users/karth/Downloads/team-pic2.png"]
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('C:/Users/karth/OneDrive/Documents/team.gif', images, duration=500, loop=0)