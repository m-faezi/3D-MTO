=====
3D-MTO
=====

3D-MTO by Mohammad H. Faezi based on
the implementation by Caroline Haigh (University of Groningen).

--------------------------

Build instructions:

Python dependencies - pip install:

- scikit-image
- astropy
- matplotlib
- Pillow
- SciPy
- numpy

The program is written for python 3.

To recompile the C libraries, run ./recompile.sh

--------------------------

To run with default parameters: 

::

	python 3d-mto.py

--------------------------

Arguments:

  -h, --help            Show the help message and exit
  -out  	        Location to save filtered image. Supports .fits and .png filenames
  -par_out		Location to save calculated parameters. Saves in .csv format
  -soft_bias		Constant bias to subtract from the image
  -gain		        Gain (estimated by default)
  -bg_mean		Mean background (estimated by default)
  -bg_variance		Background variance (estimated by default)
  -alpha	        Significance level - for the original test, this must be 1e-6
  -move_factor          Higher values reduce the spread of large objects.
				Default = 0.5
  -min_distance         Minimum brightness difference between objects.
				Default = 0.0
  -verbosity		Verbosity level (0-2)


-------------------------

We acknowledge financial support from the European Union’s Horizon 2020 research and innovation programme under Marie Skłodowska-Curie grant agreement No 721463 to the SUNDIAL ITN network.

-------------------------


[1] Citing:
::

	@inproceedings{teeninga2015improved,
	  title={Improved detection of faint extended astronomical objects through statistical attribute filtering},
	  author={Teeninga, Paul and Moschini, Ugo and Trager, Scott C and Wilkinson, Michael HF},
	  booktitle={International Symposium on Mathematical Morphology and Its Applications to Signal and Image Processing},
	  pages={157--168},
	  year={2015},
	  organization={Springer}
	}

