#!/usr/bin/env python3
import numpy as np
from PIL import Image, ImageDraw, ImageFont # Pillow fork
import os

ttf = "DejaVuSansMono-Bold.ttf"             # An installed truetype font
w, h = 660, 500                             # height, width
font_a = ImageFont.truetype(ttf, h // 20)   # font size
xc, s = -0.35, 1.75                         # x-center, and scaling
y, x = np.ogrid[-s * h/w: 1e-4: 1j * h/2, xc - s: xc + s: 1j * w]
c = x + 1j*y                                # complex plane
os.makedirs("video", exist_ok=True)         # dir for images
blues = [(v**4, v**2.5, v) for v in np.linspace(0, 1, 72)]
sepias = [(v, v**1.5, v**3) for v in np.linspace(1, 0, 12) for _ in range(6)]
rgbcolors = np.uint8(np.array(blues + sepias) * 255)
t = 200                                     # total frames
for f in range(t):
    #asymptotically rising power value over range 1.05 - 10000
    n = 2 + 2 * f / (1e-9 + t - f - 1 + (2 * t - 2) / (1e4 - 1.05))
    # slow and stop at each whole number by adding sine wave
    p = ((n * 2 * np.pi) + np.sin((n * 2 - 1) * np.pi)) / (2 * np.pi)
    imax = 10 + int((250 / ( p - 0.75)))    # max iterations
    zmax = 1 + 20 / ( p - 2 + 2 / p)        # max escape value
    its = np.zeros_like(c.real)             # iteration count        
    z = np.zeros_like(c)                    # z's start value
    
    for n in range(imax):
        mask = abs(z) < zmax                # not-yet-escaped mask
        m = np.where(mask)                  # indexes of mask
        its[m] = n                          # not-esc iteration count
        z[m] = z[m] ** p + c[m]             # multibrot formula

    # calc for continuous gradient of background
    zlog = (its - np.log(abs(np.log(abs(z)))) / np.log (p)) * np.log (p)
    # tweak gradient for good contrast at all power values
    backgnd = np.log1p(np.fmax(0, zlog * 2.6)) * (0.15 + 0.01 * np.log(p))
    np.putmask(backgnd, mask, np.zeros_like(mask))
    tones = np.uint8(np.clip(backgnd, 0, 1) * 143)
    fullheight = np.vstack((tones, np.flipud(tones)[1:],tones[0]))
    image = Image.fromarray(rgbcolors[fullheight], mode="RGB")
    draw = ImageDraw.Draw(image)
    pow = "{:.2f}".format(p)
    txt = "Z \N{RIGHTWARDS ARROW FROM BAR} Z " + ' ' * len(pow) + " + C"
    draw.text((h/18, h - h/10), txt, "white", font=font_a)
    draw.text((h/4.5, h - h/8), pow, "white", font=font_a)
    image.save('video/file{:04d}.gif'.format(f))
     
os.system("gifsicle -d5 -l0 -O3 --lossy=30 video/file????.gif >multibrot.gif")
