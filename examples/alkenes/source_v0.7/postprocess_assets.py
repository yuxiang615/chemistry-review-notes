"""Archived optional vector-crop postprocessor; requires pymupdf and numpy.
Only trims excessive whitespace around vinyl_heptane.pdf after generation.
"""
from pathlib import Path
import fitz
import numpy as np
import os
folder=Path(__file__).resolve().parent/'assets'
f=folder/'vinyl_heptane.pdf'
d=fitz.open(str(f));p=d[0]
res=3
pix=p.get_pixmap(matrix=fitz.Matrix(res,res),alpha=False)
a=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width,pix.n)
y,x=np.where(a[:,:,:3].min(axis=2)<210)
if not len(x):raise ValueError('No molecular artwork detected')
margin=7
p.set_cropbox(fitz.Rect(max(0,x.min()/res-margin),max(0,y.min()/res-margin),min(p.rect.width,x.max()/res+margin),min(p.rect.height,y.max()/res+margin)))
tmp=f.with_suffix('.pdf.tmp');d.save(str(tmp));d.close();os.replace(tmp,f)
print('Vector molecule crop updated:',f)
