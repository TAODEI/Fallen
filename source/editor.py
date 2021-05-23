"""
This file is meant to make it easy to load the main features of
MoviePy by simply typing:

>>> from moviepy.editor import *

In particular it will load many effects from the video.fx and audio.fx
folders and turn them into VideoClip methods, so that instead of
>>> clip.fx( resize, 2 ) # or equivalently resize(clip, 2)
we can write
>>> clip.resize(2)

It also starts a PyGame session (if PyGame is installed) and enables
clip.preview().
"""

from  moviepy.audio.fx import audio_fadein
from  moviepy.audio.fx import audio_fadeout
from  moviepy.audio.fx import audio_left_right
from  moviepy.audio.fx import audio_loop
from  moviepy.audio.fx import audio_normalize
from  moviepy.audio.fx import volumex

from moviepy.video.fx import accel_decel
from moviepy.video.fx import blackwhite
from moviepy.video.fx import blink
from moviepy.video.fx import colorx
from moviepy.video.fx import crop
from moviepy.video.fx import even_size
from moviepy.video.fx import fadein
from moviepy.video.fx import fadeout
from moviepy.video.fx import freeze
from moviepy.video.fx import freeze_region
from moviepy.video.fx import gamma_corr
from moviepy.video.fx import headblur
from moviepy.video.fx import invert_colors
from moviepy.video.fx import loop
from moviepy.video.fx import lum_contrast
from moviepy.video.fx import make_loopable
from moviepy.video.fx import margin
from moviepy.video.fx import mask_and
from moviepy.video.fx import mask_color
from moviepy.video.fx import mask_or
from moviepy.video.fx import mirror_x
from moviepy.video.fx import mirror_y
from moviepy.video.fx import painting
from moviepy.video.fx.resize import *
from moviepy.video.fx import rotate
from moviepy.video.fx import scroll
from moviepy.video.fx import speedx
from moviepy.video.fx import supersample
from moviepy.video.fx import time_mirror
from moviepy.video.fx import time_symmetrize

# Note that these imports could have been performed in the __init__.py
# file, but this would make the loading of moviepy slower.

import os
import sys

# Downloads ffmpeg if it isn't already installed
import imageio
# Checks to see if the user has set a place for their own version of ffmpeg
import moviepy

if os.getenv('FFMPEG_BINARY') is None:
    if sys.version_info < (3, 4):
        #uses an old version of imageio with ffmpeg.download.
        imageio.plugins.ffmpeg.download()

# Hide the welcome message from pygame: https://github.com/pygame/pygame/issues/542
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

# Clips
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from moviepy.video.io.downloader import download_webfile
from moviepy.video.VideoClip import VideoClip, ImageClip, ColorClip, TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip, clips_array
from moviepy.video.compositing.concatenate import concatenate_videoclips, concatenate # concatenate=deprecated

from moviepy.audio.AudioClip import AudioClip, CompositeAudioClip, concatenate_audioclips
from moviepy.audio.io.AudioFileClip import AudioFileClip

# FX

import moviepy.video.compositing.transitions as transfx

# Tools

import moviepy.video.tools as videotools
import moviepy.video.io.ffmpeg_tools as ffmpeg_tools
from moviepy.video.io.html_tools import ipython_display
from moviepy.tools import cvsecs

try:
    from .video.io.sliders import sliders
except ImportError:
    pass

# The next loop transforms many effects into VideoClip methods so that
# they can be walled with myclip.resize(width=500) instead of 
# myclip.fx( resize, width= 500)
# for method in [
#           "afx.audio_fadein",
#           "afx.audio_fadeout",
#           "afx.audio_normalize",
#           "afx.volumex",
#           "transfx.crossfadein",
#           "transfx.crossfadeout",
#           "crop",
#           "fadein",
#           "fadeout",
#           "invert_colors",
#           "loop",
#           "margin",
#           "mask_and",
#           "mask_or",
#           "resize",
#           "rotate",
#           "speedx"
#           ]:

#     print("VideoClip.%s = %s" % (method.split('.')[1], method))

VideoClip.audio_fadein = audio_fadein
VideoClip.audio_fadeout = audio_fadeout
VideoClip.audio_normalize = audio_normalize
VideoClip.volumex = volumex
VideoClip.crossfadein = transfx.crossfadein
VideoClip.crossfadeout = transfx.crossfadeout
VideoClip.crop = crop
VideoClip.fadein = fadein
VideoClip.fadeout = fadeout
VideoClip.invert_colors = invert_colors
VideoClip.loop = loop
VideoClip.margin = margin
VideoClip.mask_and = mask_and
VideoClip.mask_or = mask_or
VideoClip.resize = resize
VideoClip.rotate = rotate
VideoClip.speedx = speedx

# for method in ["afx.audio_fadein",
#                "afx.audio_fadeout",
#                "afx.audio_loop",
#                "afx.audio_normalize",
#                "afx.volumex"
#               ]:
              
#     print("AudioClip.%s = %s" % (method.split('.')[1], method))

AudioClip.audio_fadein = audio_fadein
AudioClip.audio_fadeout = audio_fadeout
AudioClip.audio_loop = audio_loop
AudioClip.audio_normalize = audio_normalize
AudioClip.volumex = volumex

# adds easy ipython integration
VideoClip.ipython_display = ipython_display
AudioClip.ipython_display = ipython_display
#-----------------------------------------------------------------
# Previews: try to import pygame, else make methods which raise
# exceptions saying to install PyGame


# Add methods preview and show (only if pygame installed)
try:
    from moviepy.video.io.preview import show, preview
except ImportError:
    def preview(self, *args, **kwargs):
        """NOT AVAILABLE : clip.preview requires Pygame installed."""
        raise ImportError("clip.preview requires Pygame installed")

    def show(self, *args, **kwargs):
        """NOT AVAILABLE : clip.show requires Pygame installed."""
        raise ImportError("clip.show requires Pygame installed")


VideoClip.preview = preview
VideoClip.show = show

try:
    from moviepy.audio.io.preview import preview
except ImportError:
    def preview(self, *args, **kwargs):
        """ NOT AVAILABLE : clip.preview requires Pygame installed."""
        raise ImportError("clip.preview requires Pygame installed")

AudioClip.preview = preview
