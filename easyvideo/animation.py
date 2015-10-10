#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import image


class FrameSet(object):
    def __init__(self, *file_list):
        self.frames = []
        for image_file in file_list:
            self.frames.append(image.load(image_file))

    @property
    def animation(self):
        return Animation(self.frames)

    @property
    def animation_loop(self):
        return AnimationLoop(self.frames)

    @property
    def horizontal_flip(self):
        result = FrameSet()
        for frame in self.frames:        
            result.frames.append(image.horizontal_flip(frame))
        return result
        

class Animation(object):
    def __init__(self,  frames):
        self.frames = frames

        self.frame_skip = 1
        self.__current_tick = self.frame_skip
        
        self.current = 0
        self.top = len(self.frames)

    @property
    def copy(self):
        result = Animation(self.frames)
        result.frame_skip = self.frame_skip
        result.current = self.current
        return result

    @property
    def current_frame(self):
        return self.frames[self.current]

    @property
    def more_frames(self):
        return self.current < (self.top - 1)

    @property
    def next_frame_ptr(self):
        next = self.current + 1
        if next >= self.top:
            return self.current
        return next

    def add_frame(self, frame):
        self.frames.append(frame)
        self.top += 1
        
    def reset(self):
        self.__current_tick = self.frame_skip
        self.current = 0
        
    def update(self):
        self.__current_tick -= 1
        if self.__current_tick == 0:
            self.current = self.next_frame_ptr
            self.__current_tick = self.frame_skip
        return self.frames[self.current]
    

class AnimationLoop(Animation):
    def __init__(self,  frames):
        Animation.__init__(self, frames)

    @property
    def copy(self):
        result = AnimationLoop(self.frames)
        result.frame_skip = self.frame_skip
        result.current = self.current
        return result

    @property
    def more_frames(self):
        return True
    
    @property
    def next_frame_ptr(self):
        next = self.current + 1
        if next >= self.top:
            return 0
        return next

    
class Animations(object):
    def __init__(self):
        self.animations = {}
        self.__current = None

    def add_animation(self, anim_name, animation, frame_skip=None):
        self.animations[anim_name] = animation.copy
        if self.__current is None:
            self.__current = anim_name
        if frame_skip is not None:
            self.animations[anim_name].frame_skip = frame_skip

    def change_animation(self, anim_name):
        if anim_name not in self.animations.keys():
            raise ValueError('Animation not found: %s' % anim_name)
        self.__current = anim_name
        self.animations[self.__current].reset()
        
    @property
    def more_frames(self):
        return self.animations[self.__current].more_frames

    @property
    def current_frame(self):
        return self.animations[self.__current].current_frame
    
    def update(self):
        return self.animations[self.__current].update()
    
    @property
    def copy(self):
        result = Animations()
        for animation_name in self.animations.keys():
            result.add_animation(animation_name,
                                 self.animations[animation_name])
        result.change_animation(self.__current)
        return result

    def __getattr__(self, attr):
        return self.animations[attr]
