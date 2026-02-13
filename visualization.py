import matplotlib.pyplot as plt

def plot_density(density_history):
    plt.figure()
    plt.plot(density_history)
    plt.xlabel("Time")
    plt.ylabel("Person Count")
    plt.title("Real-Time Crowd Density")
    plt.show()
