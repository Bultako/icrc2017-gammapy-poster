# Code examples

The Python script to convert the Python to PDF files calls Pygments directly and
was copied from the Astropy paper repo.

* https://github.com/astropy/astropy-v0.2-paper/blob/master/examples/
* http://pygments.org/

I also tried the `minted` Python package, but couldn't get it to work properly.
Putting the code as pre-generated PDF figures is OK. The only advantage of
`minted` as far as I can see would be that it has extra features like being able
to label code lines and link to them in descriptions from the main test. I'm not
sure if putting the code more "inline", not in a proper Figure would be better.

* https://github.com/gpoore/minted
* http://ftp.fernuni-hagen.de/ftp-dir/pub/mirrors/www.ctan.org/macros/latex/contrib/minted/minted.pdf
