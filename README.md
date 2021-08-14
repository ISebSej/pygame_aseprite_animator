Pygame_Aseprite_Animation
============
[![GitHub Stars](https://img.shields.io/github/stars/ISebSej/pygame_aseprite_animator.svg)](https://github.com/IgorAntun/node-chat/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/ISebSej/pygame_aseprite_animator.svg)](https://github.com/IgorAntun/node-chat/issues) [![Current Version](https://img.shields.io/badge/version-0.0.7-yellow.svg)](https://github.com/IgorAntun/node-chat) 

It's finally possible to parse and display .ase and .aseprite files directly without exporting them into some other kind of format first! Thanks to @Eiyeron for his work on the [py_aseprite](https://github.com/Eiyeron/py_aseprite) on which this was build.


![Animation Preview](http://i.imgur.com/n8EUvEa.mp4)

Check out the full example in example/example.py

<!-- ---
## Buy me a coffee

Whether you use this project, have learned something from it, or just like it, please consider supporting it by buying me a coffee, so I can dedicate more time on open-source projects like this :)

<a href="https://www.buymeacoffee.com/igorantun" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a> -->

---

## Features
- Load .ase and .aseprite files
- **NOTE:** only RGBA mode is currently supported. Grayscale and indexed have not been tested
- Supports layers
- Supports animations with variable timing, straight from the aseprite file
- Automatically handles timings
- py_aseprite is currently bundled into this package, so you don't have to manually download it

---

## TODOs
- implement grayscale and indexed images (never used this myself)
- allow Animations to have a name/id attribute so users can more easily access them in the animation manager
- do the programmer stuff like unit testing which I can't bothered to do
- Improve and feature complete the animation manager, it's still a bit simple. I'm sure people can find lots of ideas for it. 

---

## Get package
Simply run `pip3 install pygame_aseprite_animation` to install the package.

---
## How to Use

The package is  simple to set up and implement

```python
import pygame_aseprite_animation
import os, pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([300, 300])

# Set file directory
dirname = os.path.dirname(__file__)
aseprite_file_directory = str(dirname) + '/test.ase'

# Load animations
test_animation = Animation(aseprite_file_directory)
test_animation2 = Animation(str(dirname) + '/test2.aseprite')
# Load manager
animationmanager = AnimationManager([test_animation, test_animation2], screen)

running = True
while running:
    # Fill the background with white
    screen.fill((0, 0, 0))

    animationmanager.update_self(0, 0)

    if something_happened():
        # Play test2 once, after which you continue with test
        animationmanager.startanimation(animationmanager.animation_list[1], animationmanager.animation_list[0])

    # Flip the display
    pygame.display.flip()

```

So what exactly is available to you and how to access it

```python
import pygame_aseprite_animation
import os

# Set file directory
dirname = os.path.dirname(__file__)
aseprite_file_directory = str(dirname) + '/test.ase'

# Load animations
test_animation = Animation(aseprite_file_directory)

## Access attributes of animation
# contains a list of every frame as a pygame.Surface() object
print(test_animation.animation_frames)
# Access individual frame. It's still a pygame.Surface() object
print(test_animation.animation_frames[1])
# A list of how long a frame should be displayed for. read straight from the .ase file
print(test_animation.frame_duration)

## Attributes of animation manager
# NOTE: The 1st animation in the list will automatically start playing when the 
# manager is instanciated
animationmanager = AnimationManager([test_animation], screen)

# View list of Animation() objects 
print(animationmanager.animation_list)
# Start a new animation. this one will be looping as long as _next_animation is not set
# I think you can get away with using this function with an animation that is not in .animation list.
# But I haven't tested yet. It needs at least 1 animation to have a default state
# TODO: Allow animations to have a name/id so users can call anmations by name instead of by index in the list
animationmanager.startanimation(animationmanager.animation_list[0])

# Start animation, but after it's done it will switch to a different on
animationmanager.startanimation(animationmanager.animation_list[0], animationmanager.animation_list[1])

# Actually update the state of the animation and blit it to the display
animationmanager.update_self(x_coordinate, y_coordinate)
```

---

## How it works

To keep a long story short, I use the py_aseprite package by @Eiyeron to parse the .ase file. He managed to handle all of the of raw bit parsing, handling diffenent formats and what now. pretty impressive and timeconsuming stuff. 

I then continue to create an empty pygame surface for every frame of the aseprite animation, after which I read the chucks/layers (not exactly sure what the difference is, but in my testing a chuck just represented a layer) one by one and draw onto the pygame.surface. You only need to do this once at loadtime of whatever object you are importing. After that you have a pygame.Surface with your beautiful frame drawn onto it.
We do this for every frame and save it to a list. 

Next to that, we also read the frame duration for each frame from the aseprite header data, which allows us to pretty easily implement some basic timing stuff.

The parsed aseprite file is still available in the Animation objects, so if you want to access additional parameters you can do so. You'll just need to read through the py_aseprite documentation to get a better idea of how it's all structured. 


---

## License
>You can check out the full license [here](https://github.com/ISebSej/pygame_aseprite_animator/blob/main/LICENSE)

This project is licensed under the terms of the **MIT** license.