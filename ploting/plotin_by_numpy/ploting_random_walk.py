import numpy as np
import matplotlib.pyplot as plt
n_steps = 1000
n_walk = 2
rng = np.random.default_rng(seed=123)
draws = rng.integers(0,2,size=(n_walk,n_steps))

steps = np.where(draws == 0,1,-1)
walks = steps.cumsum(axis=1)
plt.figure(figsize=(10,5))
for i in range(n_walk):
    plt.plot(walks[i],label = f'Random Walk{i+1}')
plt.axhline(0, color='gray',linestyle='-',linewidth = 1)
plt.axvline(0, color='gray',linestyle='-',linewidth = 1)
plt.xlabel('Number of steps')
plt.ylabel("postion")
plt.title('Random walk simulation')
plt.legend()
plt.grid()
plt.show()
print(draws)