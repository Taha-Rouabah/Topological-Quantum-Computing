# -*- coding: utf-8 -*-
"""
Created on Wed May 29th 2019

@author: N. Belaloui
"""

import numpy as np
import matplotlib.pyplot as plt

# Images paths
SIG_1 = ['moves/s1.png', 'moves/s1_inv.png']
SIG_2 = ['moves/s2.png', 'moves/s2_inv.png']

SIGMA = {1:SIG_1, 2:SIG_2}

def concat_images(imga, imgb):
    """
    Combines two color image ndarrays side-by-side.
    """
    ha,wa = imga.shape[:2]
    hb,wb = imgb.shape[:2]
    max_height = np.max([ha, hb])
    total_width = wa+wb
    new_img = np.zeros(shape=(max_height, total_width, 3))
    new_img[:ha,:wa]=imga
    new_img[:hb,wa:wa+wb]=imgb
    return new_img

def concat_n_images(image_path_list):
    """
    Combines N color images from a list of image paths.
    """
    output = None
    for i, img_path in enumerate(image_path_list):
        img = plt.imread(img_path)[:,:,:3]
        if i==0:
            output = img
        else:
            output = concat_images(output, img)
    return output


def draw(weave, init_sigma, file_name):
    """
    Draws the braid corresponding to the weave as described by 'weave'
    starting with init_sigma, shows it and saves it to the file 'file_name'.

    Example :
        draw(weave=[2,2,-2,-4], init_sigma=1, file_name='test.png')

    Parameters
    ----------
    weave : List
        List of powers describing the weave.
    init_sigma : int
        The first sigma move, 1 for sigma_1, 2 for sigma_2.
    file_name : str
        Name (and path) of the saved file.
    """
    # Generating the images list
    images = []
    cur_sigma = init_sigma
    for p in reversed(weave):
        # drawing the move |p|-times
        if p > 0:
            images += [SIGMA[cur_sigma][0]] * p
        else:
            images += [SIGMA[cur_sigma][1]] * (-p)

        # Flipping the sigma value
        if cur_sigma == 1:
            cur_sigma = 2
        else:
            cur_sigma = 1

    # Drawing
    output = concat_n_images(images)
    plt.imshow(output)
    plt.axis('off')
    plt.savefig(file_name, dpi=300)
    plt.show()
