#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:19:47 2018

@author: loganwu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.arange(0, 100)

mu = [35, 60]
sd = [5, 3]

var1 = sd[0]**2
var2 = sd[1]**2
prec1=1/var1
prec2=1/var2
prec3=prec1+prec2
var3=1/prec3
mu3=(mu[0]*prec1+mu[1]*prec2)/(prec1+prec2)
sd3=np.sqrt(var3)

dprior = norm.pdf(x, mu[0], sd[0])
dlikelihood = norm.pdf(x, mu[1], sd[1])
dposterior = norm.pdf(x, mu3, sd3)


fig, ax = plt.subplots(figsize=[2, 1])
plt.fill_between(x, dprior, alpha=0.5, label="Prior")
plt.fill_between(x, dlikelihood, alpha=0.5, label="Likelihood")
plt.fill_between(x, dposterior, alpha=0.5, label="Posterior")
#plt.xlabel("Parameter estimate")
#plt.legend()

# Hide the right and top spines
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.yticks([])
plt.xticks([])

plt.savefig("../media/bayesexample.png", bbox_inches="tight", dpi=144, transparent=True)
