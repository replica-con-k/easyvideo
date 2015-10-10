#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

'''Animation handling module.'''

import easyvideo.image


class FrameSet(object):
    '''Load a set of frames in one frame per file.'''
    def __init__(self, *file_list):
        self.frames = []
        for image_file in file_list:
            self.frames.append(easyvideo.image.load(image_file))

    @property
    def animation(self):
        '''Return a normal animation object.'''
        return Animation(self.frames)

    @property
    def animation_loop(self):
        '''Return a loop animation object.'''
        return AnimationLoop(self.frames)

    @property
    def horizontal_flip(self):
        '''Return a horizontal-flipped FrameSet() object.'''
        result = FrameSet()
        for frame in self.frames:
            result.frames.append(easyvideo.image.horizontal_flip(frame))
        return result


class Animation(object):
    '''A single-loop animation object. This object contains references
       to frames.'''
    def __init__(self, frames):
        self.frames = frames

        self.frame_skip = 1
        self.__current_tick = self.frame_skip

        self.current = 0
        self.top = len(self.frames)

    @property
    def copy(self):
        '''Return a copy of the animation.'''
        result = Animation(self.frames)
        result.frame_skip = self.frame_skip
        result.current = self.current
        return result

    @property
    def current_frame(self):
        '''Return current frame.'''
        return self.frames[self.current]

    @property
    def more_frames(self):
        '''Return if there are more frames in the animation.'''
        return self.current < (self.top - 1)

    @property
    def next_frame_ptr(self):
        '''Return the pointer to the next frame in the animation.'''
        next_ptr = self.current + 1
        if next_ptr >= self.top:
            return self.current
        return next_ptr

    def reset(self):
        '''Restart animation.'''
        self.__current_tick = self.frame_skip
        self.current = 0

    def update(self):
        '''Return next frame of the animation.'''
        self.__current_tick -= 1
        if self.__current_tick == 0:
            self.current = self.next_frame_ptr
            self.__current_tick = self.frame_skip
        return self.frames[self.current]


class AnimationLoop(Animation):
    '''A infinite-loop animation object.'''
    def __init__(self, frames):
        Animation.__init__(self, frames)

    @property
    def copy(self):
        '''Return a copy of the animation.'''
        result = AnimationLoop(self.frames)
        result.frame_skip = self.frame_skip
        result.current = self.current
        return result

    @property
    def more_frames(self):
        '''Return if animation has more frames left.'''
        return True

    @property
    def next_frame_ptr(self):
        '''Return pointer to the next frame.'''
        next_ptr = self.current + 1
        if next_ptr >= self.top:
            return 0
        return next_ptr


class Animations(object):
    '''Container of multiple animation objects. Shows only one at-a-time.'''
    def __init__(self):
        self.animations = {}
        self.__current = None

    def add_animation(self, anim_name, animation, frame_skip=None):
        '''Add another animation to the container.'''
        self.animations[anim_name] = animation.copy
        if self.__current is None:
            self.__current = anim_name
        if frame_skip is not None:
            self.animations[anim_name].frame_skip = frame_skip

    def change_animation(self, anim_name):
        '''Change current animation.'''
        if anim_name not in self.animations.keys():
            raise ValueError('Animation not found: %s' % anim_name)
        self.__current = anim_name
        self.animations[self.__current].reset()

    @property
    def more_frames(self):
        '''Return if current animation has more frames left.'''
        return self.animations[self.__current].more_frames

    @property
    def current_frame(self):
        '''Return the frame of the current animation.'''
        return self.animations[self.__current].current_frame

    def update(self):
        '''Update current animation.'''
        return self.animations[self.__current].update()

    @property
    def copy(self):
        '''Return a clone object (sharing frames references).'''
        result = Animations()
        for animation_name in self.animations.keys():
            result.add_animation(animation_name,
                                 self.animations[animation_name])
        result.change_animation(self.__current)
        return result

    def __getattr__(self, attr):
        return self.animations[attr]
