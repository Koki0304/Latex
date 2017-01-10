# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:04:33 2017

@author: KOKI YAMAMOTO
"""

import numpy as np # clone de Matlab
import matplotlib.pyplot as plt  ## Librairie graphique

def fonction(x, tau, omega):

  """
  Une fonction a tracer
        
  fonction(1,2,3) = 0.0519151497
  """
  return np.exp( -x / tau)*np.sin(omega * x)

# Trace de la fonction
x = np.linspace(0.,10.,1000)
y1 = fonction(x, tau = 5., omega = .5* np.pi)
y2 = fonction(x, tau = 3., omega = 2.* np.pi)

#----------------------------------------------------------------
#Mise en page plus fine de la figure
plt.rc('text', usetex=False)
plt.rc('font', family='serif')
plt.rc("font.serif")
plt.rcParams['font.serif'] = ['Times']
plt.rcParams["xtick.labelsize"] = 10.
plt.rcParams["ytick.labelsize"] = 10.

width = 6.69  # laeger de la figure
heigth = width /2.5 # hauter de ala figure
#----------------------------------------------------------------


fig =plt.figure(figsize = (width, heigth))
plt.plot(x, y1, label = r"$\tau = 5, \omega = \pi/2 $")
plt.plot(x, y2, label = r"$\tau = 3, \omega = 2\pi $")
plt.grid()
plt.legend(loc = "best")
plt.xlabel("Temps, $t$")
plt.ylabel("Amplitude, $y(t)$")
plt.title(r"oscillateur amorti: $y(t) = \exp(-t/\tau)\sin(\omega t)$")

#plt.show()
#plt.tight_layout()
#plt.tight_layout()
#plt.savefig("osciallateur.pdf")

plt.savefig('test1')

