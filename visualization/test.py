"""
1.Matplotlib
-> Line Charts
-> bar Charts
-> Scatter Plots
-> histograms
2.seaborn 
-> it provide a high level interface for drawing attractive and informative statistical graphics
-> Better looking for visualization
-> Statical Visulization
-> Heatmaps
-> Box plots 

"""
# pip install matplotlib
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [1000, 1500, 1200, 1800, 2000, 2200]


plt.plot(months, sales)

plt.title("Monthly Sales")

plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()