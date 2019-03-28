# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1, 7)

# Finish the control construct
if(dice <= 2):
    step-=1
elif(dice <= 5):
    step+=1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice, step)