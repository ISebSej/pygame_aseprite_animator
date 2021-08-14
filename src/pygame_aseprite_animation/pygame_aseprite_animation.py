from py_aseprite import AsepriteFile
from py_aseprite import CelChunk

from enum import Enum
from pathlib import Path
import pygame
import time

class Animation(object):
    """A class that contains all of the animations and frame duration information
    TODO: Maybe add name property to assign to animations

    Artibutes:
        :aseprite_file: the loaded in aseprite file. Shouldn't have to use this file\n
        :animation_frames: a list of pygame.Surface() objects, each containing a single frames\n
        :frame_duration: a list of the duration each frame should be displayed. Index matches that of :animation_frame:"""

    def __init__(self, _filedir):
        """Instanciate a animation object
        
        :_filedir: Path to your .ase or .aseprite files\n
        :return: Animation object containt your frames as a list of pygame.surface() objects """

        # load aseprite file
        self.aseprite_file = self.parseFile(_filedir)
        # create precompiled list of surfaces for each frame
        self.animation_frames = self.draw_all_animation_frames()
        # Create list of frame duration for each frame
        self.frame_duration = [frame.frame_duration for frame in self.aseprite_file.frames]

    def parseFile(self, filedir):
        """Uses py_aseprite to load the file
        
        :filedir: Path to your .ase or .aseprite files\n 
        :return: Animation object containt your frames as a list of pygame.surface() objects """
        with open(filedir, 'rb') as f:
            return AsepriteFile(f.read())

    def draw_all_animation_frames(self):
        """Goes through .ase or .aseprite file and draws all of your frames
        
        :return: animation_frames which is a list of every individual frame"""
        animation_frames = []
        for frame_number in range(self.aseprite_file.header.num_frames):
                frame = self.draw_single_frame(frame_number)
                animation_frames.append(frame)

        return animation_frames

    def draw_single_frame(self, num_frame):
        """Draws single frame onto an empty pygame.Surface
        
        :num_frame: index of the frame to be drawn\n
        :return: frame which is a pygame.Surface() of the same size as the aseprite file onto which the pixels are drawn """
        cel_slice = [None] * len(self.aseprite_file.layers)

        #read slices
        for chunk in self.aseprite_file.frames[num_frame].chunks:
            if isinstance(chunk, CelChunk):
                cel_slice[chunk.layer_index] = chunk

        #initialize frame surface
        frame = pygame.Surface((self.aseprite_file.header.width, self.aseprite_file.header.height), pygame.SRCALPHA)
        frame.fill((255,0,0,0))
        # draw layers on top of each other
        for layer in self.aseprite_file.layer_tree:
            current_cel = cel_slice[layer.layer_index]
            if current_cel:
                frame = self.draw_raw_image_data(current_cel, frame)
        return frame

    def draw_raw_image_data(self, cel :CelChunk, frame):
        """Actually reads the pixel data and draw it onto the surface() layer by layer
        
        :cel: CelChunk object from the raw aseprite file, handles by py_aseprite\n
        :frame: the pygame.Surface() onto which the data will be drawn\n
        :return: the pygame.Surface(), but with the layer drawn onto it"""
        data = list(cel.data['data'])
        for y in range(cel.data['height']):
            for x in range(cel.data['width']):
                base_offset = y * cel.data['width'] + x
                CHANNELRED      = data[base_offset * 4]
                CHANNELGREEN    = data[base_offset * 4 + 1]
                CHANNELBLUE     = data[base_offset * 4 + 2]
                if (CHANNELRED + CHANNELGREEN + CHANNELBLUE == 0):
                    CHANNELALPHA = 0
                else:
                    CHANNELALPHA    = data[base_offset * 4 + 3]
                    frame.set_at((x + cel.x_pos, y + cel.y_pos), pygame.Color(CHANNELRED, CHANNELGREEN, CHANNELBLUE, CHANNELALPHA))
                
                
        return frame

class AnimationManager(object):
    """A class that actually handles the animation timing and drawing to the screen. 
    It contains all the animations of an object and can switch between them.
    Automatically start on the first Animation in the list

    Methods:
        :start_animation: Call whenever you want to cancel the current animation and start a new one\n
        :update_self: Called every frame, checks if animation counter has expired and updates if necessary. Also blits the frame to the screen\n
    
    Atributes:
        :animation_list: a list of all the animations for this instance\n
        :draw_surface: the surface onto which the frame needs to be drawn"""

    def __init__(self, _animation_list :Animation, _draw_surface :pygame.Surface):
        """Init
        
        :_animation_list: a list of Animation Objects \n
        :_draw_frame: the pygame.Surface() onto which you'd like to blit the frames"""
        self.animation_list = _animation_list
        self.draw_surface = _draw_surface
        # Initialize animation to the 1st frame in the list
        self.start_animation(self.animation_list[0])

    def start_animation(self, _animation:Animation, _next_animation:Animation = None):
        """Start a new animation to
        
        :_animation: the animation you'd like to display
        :_next_animation: what animation to play after this one is finished. Loops if left empty."""
        # Set the animation you'd like to display
        self.current_animation = _animation
        # Animation to play after finishing. Animation loops if None.
        self.next_animation = _next_animation
        # Set timing
        self.tstart =  round(time.time() * 1000)
        self.tend = self.tstart + _animation.frame_duration[0]
        self.framenum = 0

    def update_self(self, frame_x, frame_y):
        """Called every frame. Checks if frame duration is finished and blits frame to your Surface
        
        :frame_x/y: Pixel location where the frame need to be blit"""
        # Check if frame is finished. if so, set next frame
        if  round(time.time() * 1000) > self.tend:
            # Check if animation is finished and set next animation if needed
            if self.framenum == len(self.current_animation.frame_duration) - 1:
                if self.next_animation is not None:
                    self.current_animation = self.next_animation
                self.framenum = 0
            else:
                self.framenum += 1
            # reset timings
            self.tstart =  round(time.time() * 1000)
            self.tend = self.tstart + self.current_animation.frame_duration[self.framenum]
        
        # Blit frame
        self.draw_surface.blit(self.current_animation.animation_frames[self.framenum], (frame_x, frame_y))
        
