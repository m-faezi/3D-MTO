import mtolib.main as mto
import glob
import numpy as np
from astropy.io import fits


# Get the input data and parameters
params = mto.setup()

fits_files = glob.glob('_data/*.fits')
image_stack = []
for file in fits_files:
    with fits.open(file) as hdul:
        image = hdul[0].data
        image_stack.append(image)
volume = np.array(image_stack)

# Build a max tree
mt = mto.build_max_tree(volume, params)

# Filter the tree and find objects
id_map, sig_ancs = mto.filter_tree(mt, volume, params)

# Relabel objects for clearer visualisation
id_map = mto.relabel_segments(id_map, shuffle_labels=False)

