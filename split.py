from PIL import Image 
from argparse import ArgumentParser 
import glob 

def extract_gif(name): 

    frames = Image.open(name)
    counter = 0 
    for frame in range(frames.n_frames): 
        frames.seek(frame)
        frames.save("./im_{}.png".format(counter), 'PNG')
        counter += 1 
        try: 
            frames.seek(counter)
        except:
            break 

    print('Found {} frames'.format(counter))
    return 


if __name__ == "__main__": 
    my_gifs = glob.glob('*.gif')
    for i,gif in enumerate(my_gifs): 
        print('{} -- nb {}'.format(gif,i))
    if len(my_gifs) == 1:
        nb = 0
    else: 
        nb = int(input('File number'))
    extract_gif(my_gifs[nb])