import imageio
import os

frames = []
path = 'images'

# Load each file into a list
for filename in os.listdir(path):
    if filename.endswith(".jpg"):
        print(filename)
        frames.append(imageio.imread(path + "/" + filename))


# Save them as frames into a gif 
exportname = "output.gif"
kargs = { 'duration': 0.1 }
imageio.mimsave(exportname, frames, 'GIF', **kargs)

# Image resize, normalize, compress 