init python:
    config.subpixel = True

transform shake:
    parallel:
        linear 0.05 xoffset 10
        linear 0.05 yoffset -5
    parallel:
        linear 0.05 xoffset -10
        linear 0.05 yoffset 5
    repeat

transform reset_transform_shake_right:
        xzoom 1.0 yzoom 1.0

transform reset_transform_shake_left:
        xzoom -1.0 yzoom 1.0