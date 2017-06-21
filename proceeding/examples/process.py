import os
import sys
import glob
import subprocess

def process(filename, format='code'):
    base = filename.replace('.py', '')
    if format == 'code':
        opts = '-l python -f latex -O style=colorful,linenos=1 -O full'
    elif format == 'repl':
        opts = '-l pycon -f latex -O style=default -O full'
    else:
        raise ValueError()

    script = """
    pygmentize {opts} -o {base}-tmp.tex  {base}.py
    """.format(opts=opts, base=base)
    subprocess.call(script, shell=True)
    fout = open('{base}-tmp-2.tex'.format(base=base), 'w')
    for line in open('{base}-tmp.tex'.format(base=base), 'r'):
        fout.write(line)
        if 'documentclass' in line:
            fout.write("\\usepackage[paperheight=20in]{geometry}\n")
            fout.write("\pagestyle{empty}\n")
    script = """
    pdflatex {base}-tmp-2.tex
    pdfcrop --bbox "0 100 1000 10000"  {base}-tmp-2.pdf {base}-tmp-3.pdf
    pdfcrop -margins "2 2 2 2" {base}-tmp-3.pdf {base}.pdf
    """.format(base=base)
    fout.close()
    subprocess.call(script, shell=True)
    os.remove('{base}-tmp.tex'.format(base=base))
    os.remove('{base}-tmp-2.tex'.format(base=base))
    os.remove('{base}-tmp-2.log'.format(base=base))
    os.remove('{base}-tmp-2.aux'.format(base=base))
    os.remove('{base}-tmp-2.pdf'.format(base=base))
    os.remove('{base}-tmp-3.pdf'.format(base=base))
    print('Writing {}'.format(filename))

if __name__ == '__main__':
    process('code_events_image.py', format='code')
    process('code_constants.py', format='repl')
