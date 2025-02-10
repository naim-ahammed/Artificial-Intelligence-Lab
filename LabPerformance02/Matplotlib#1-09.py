# Matplotlib#1: Plot a line graph showing temperature variations over a week.

import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temperatures = [42, 35, 29, 28, 30, 29, 38]  

plt.figure(figsize=(8, 5))  
plt.plot(days, temperatures, marker='o', linestyle='-', color='b', linewidth=2, markersize=6)

plt.xlabel("days of the week")
plt.ylabel("temperature (°C)")
plt.title("temperature variations over a week")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
