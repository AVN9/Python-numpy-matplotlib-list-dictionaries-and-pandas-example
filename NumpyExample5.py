#Numpy 2-D array median fn

import numpy as np
positions = ['GK', 'M', 'A', 'D', ...]
heights = [191, 184, 185, 180, ...]

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print(np.median(gk_heights))

# Print out the median height of other players. Replace 'None'
print(np.median(other_heights))
