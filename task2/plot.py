import matplotlib.pyplot as plt
import numpy as np
from main import get_cohort_sizes

# Takes list with 12 integer values and plots these in a histogram
def plot_new_users(data: list[int]):
    t = np.linspace(0,12,12)
    plt.figure(figsize=(12,6))
    plt.bar(t, data, tick_label=["Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb"])
    plt.xlabel("Month")
    plt.ylabel("New users")
    plt.show()

plot_new_users(get_cohort_sizes())