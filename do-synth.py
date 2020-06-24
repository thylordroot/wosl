#!/usr/bin/env python

# File: do-synth.py
# Author: thylordroot
# Since: 6/19/2020
#
# This script is responsible for generating synthesizer samples
#

import os
import os.path
import math;
import wave;
import io;
import struct;
import random;

def normPath(x):
	return x.replace('/', os.sep);

def ensureDir(x):
	x = normPath(x);
	if not os.path.isdir(x):
		os.mkdir(x);

# Primitive Waveforms

def sin(t):
	return math.sin(2*math.pi*t);
	
def sqr(t, duty=0.5):
	phase = t % 1;
	if phase <= duty:
		return 1
	else:
		return -1
		
def saw(t):
	phase = t % 1;
	if (t % 1) <= 0.5:
		return 2*phase
	else:
		return 2*(phase-1)
		
def tri(t):
	phase = t % 1;
	if phase <= 0.25:
		return 4*phase
	elif phase <= 0.75:
		return 4*(0.5 - phase)
	else:
		return -1 + 4*(phase - 0.75);
		
def noise(t):
	return random.uniform(-0.99, 0.99);
	
def sqra(t, harmonics=4):
	smp = sin(t)
	k = 3
	while harmonics > 0:
		smp = smp + 1/k * sin(k*t)
		k = k + 2
		harmonics = harmonics - 1

	return smp

###################
# Derived Waveforms
###################

def _duty(func, t, c, cutout):
	phase = t % 1
	return func(phase) if phase <= c else cutout

# Wrap func so that it has a duty cycle of c
#
# This function takes func and cuts out after the c proportion of the period
# is over. 
#
# Param: func The function to wrap
# Param: c A value from [0,1]
# Param: cutout The quiescent value when the duty cycle is over
def duty(func, c, cutout = 0):
	return lambda t: _duty(func, t, c, cutout)

def clamp(x, hi = 1, lo=None):
	if lo is None:
		lo = -hi

	if x > hi:
		return hi
	elif x < lo:
		return lo
	else:
		return x

def distort(func, gain, hi = 1, lo=None):
	return lambda t: clamp(gain* func(t), hi, lo) 


##########
# Sampling
##########

# Create a sample buffer using func as a basis at the given frequency and 
# bandwidth
#
# This function samples the waveform supplied by func at the specified 
# frequency and bandwidth. The waveform generally has an amplitude of
# amp and will not exceed this value.
#
# Param: func The function to sample
# Param: amp The maximum amplitude of the function (default: 0.75)
# Param: freq The frequency at which to sample the function (default: 440)
# Param: cycles The number of times to repeat the function (default: 1)
# Param: bandwidth The sample rate at which to record the sample in
# 	samples per second. (default: 44100)
# 
# Note: the actual frequency of the sample buffer may slightly different than
# what was requested and depends on the bandwidth. Typically, the sample 
# generated will be slightly sharp. For instance, at 44.1KHz a 440Hz sample
# will end up being at 441Hz instead due to imprecise alignment alignment
# during the discretization process. On the other hand, 48KHz will lead to
# the resulting sample being tuned at 440.3Hz.
def sample(func, amp=0.75, freq=440, cycles=1, bandwidth=44100):
	buf = list();
	
	# Figure out how many samples we need in the buffer
	period = bandwidth/freq;
	for i in range(0, math.floor(cycles*period)):
		t = i/period
		buf.append(clamp(amp*func(t), amp));
	
	
	return buf;
	
def capture(file, func, amp=0.75, freq=440, cycles=1, bandwidth=44100,
	channels=1):
	# Create our sample buffer
	smp = sample(func, amp, freq, cycles, bandwidth)
	
	with wave.open(normPath(file), mode="wb") as out:	
		out.setframerate(bandwidth)
		out.setsampwidth(2)
		out.setnchannels(channels)
		out.setnframes(len(smp));
		
		for i in smp:
			v = struct.pack('<h', int(32767 * i));
			out.writeframesraw(v);
		
	

ensureDir("smp/synth");

# Basic waveforms
capture("smp/synth/a-sin.wav", sin)
capture("smp/synth/a-sqr.wav", sqr)
capture("smp/synth/a-sqra.wav", sqra)
capture("smp/synth/a-saw.wav", saw)
capture("smp/synth/a-tri.wav", tri)
capture("smp/synth/a-noise.wav", noise, cycles=400)

# Duty Cycled waveforms
capture("smp/synth/a-sqr-25.wav", duty(sin, 0.25))
	
