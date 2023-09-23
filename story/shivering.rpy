init:
    transform shivering_right(duration=0.5):
        xzoom 1.0 yzoom 1.0
        linear duration/2 xzoom 0.995 yzoom 0.995
        linear duration/2 xzoom 1.0 yzoom 1.0
        repeat

    transform shivering_left(duration=0.5):
        xzoom -1.0 yzoom 1.0
        linear duration/2 xzoom -0.995 yzoom 0.995
        linear duration/2 xzoom -1.0 yzoom 1.0
        repeat
    
    transform reset_transform_shivering_right:
        xzoom 1.0 yzoom 1.0

    transform reset_transform_shivering_left:
        xzoom -1.0 yzoom 1.0