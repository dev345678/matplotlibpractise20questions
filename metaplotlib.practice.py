import matplotlib.pyplot as plt

# 1. Line graph
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.figure()
plt.plot(x, y)
plt.title("Line Graph")
plt.show()

# 2. Bar chart
students = ['A', 'B', 'C', 'D', 'E']
marks = [80, 90, 70, 85, 95]
plt.figure()
plt.bar(students, marks)
plt.title("Bar Chart of Student Marks")
plt.show()

# 3. Horizontal bar chart
students = ['A', 'B', 'C', 'D', 'E']
marks = [80, 90, 70, 85, 95]
plt.figure()
plt.barh(students, marks)
plt.title("Horizontal Bar Chart")
plt.show()

# 4. Pie chart
companies = ['A', 'B', 'C', 'D']
share = [40, 25, 20, 15]
plt.figure()
plt.pie(share, labels=companies, autopct='%1.1f%%')
plt.title("Market Share")
plt.show()

# 5. Scatter plot
height = [150, 160, 165, 170, 175]
weight = [50, 55, 60, 65, 70]
plt.figure()
plt.scatter(height, weight)
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.show()




# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("Line Graph of y = 2x")
plt.xlabel("X-axis: Numbers")
plt.ylabel("Y-axis: Doubled Values")
plt.show()




# 7. Dotted green line
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.figure()
plt.plot(x, y, 'g--')
plt.title("Dotted Green Line")
plt.show()

# 8. Two lines with legend
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
y2 = [1, 2, 1, 2, 1]
plt.figure()
plt.plot(x, y, label="Line 1")
plt.plot(x, y2, label="Line 2")
plt.legend()
plt.title("Two Lines with Legends")
plt.show()

# 9. Custom ticks
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.figure()
plt.plot(x, y)
plt.xticks([1, 2, 3, 4, 5], ['One', 'Two', 'Three', 'Four', 'Five'])
plt.yticks([0, 5, 10])
plt.title("Custom Ticks")
plt.show()

# 10. Rotate x-axis labels
students = ['A', 'B', 'C', 'D', 'E']
marks = [80, 90, 70, 85, 95]
plt.figure()
plt.bar(students, marks)
plt.xticks(rotation=45)
plt.title("X-axis Labels Rotated")
plt.show()

# 11. 2 subplots in 1 row
students = ['A', 'B', 'C', 'D', 'E']
marks = [80, 90, 70, 85, 95]
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
fig, axs = plt.subplots(1, 2)
axs[0].plot(x, y)
axs[0].set_title("Plot 1")
axs[1].bar(students, marks)
axs[1].set_title("Plot 2")
plt.suptitle("Two Subplots")
plt.show()

# 12. 4 subplots in 2x2 layout
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
students = ['A', 'B', 'C', 'D', 'E']
marks = [80, 90, 70, 85, 95]
height = [150, 160, 165, 170, 175]
weight = [50, 55, 60, 65, 70]
companies = ['A', 'B', 'C', 'D']
share = [40, 25, 20, 15]

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].bar(students, marks)
axs[1, 0].scatter(height, weight)
axs[1, 1].pie(share, labels=companies)
plt.suptitle("4 Subplots (2x2)")
plt.tight_layout()
plt.show()



x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.subplot()
plt.plot(x,y,color="blue",marker="s",linestyle="--",label="plotting")
plt.legend()
plt.xticks([1,2,3,4,5],["one","two","three","four","five"])
plt.title("numbers")
plt.xlabel("prime no ")
plt.ylabel("even no")
plt.grid(color= "green",linewidth="1")
plt.show()


x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.subplot(2,1,1)
plt.plot(x,y,color="blue",marker="s",linestyle="--",label="plotting")
plt.title("line graph")

plt.subplot(2,1,2)
plt.barh(x,y,color=['red','blue','pink','coral','green'])
plt.title("bar graph")
plt.tight_layout()

plt.show()




x=[1,2,3,4,5]
y=[2,4,6,8,10]
fig,dev=plt.subplots(1,2,figsize=(10,5))
dev[0].plot(x,y)
dev[0].set_title('line graph')
dev[1].bar(x,y)
dev[1].set_title('bar graph')
plt.suptitle('two subplots')
plt.tight_layout()
plt.show()



x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.pie(x,labels=y,autopct="%1.1f%%")

plt.show()



import numpy as np
x=np.random.randn(1000)
plt.hist(x,bins=10,edgecolor='black')
plt.show()


math_marks=[60,70,80,90]
english_marks=[40,50,60,70]
science_marks=[65,75,85,95]
data1=[math_marks,english_marks,science_marks]
box=plt.boxplot(data1,patch_artist=True,labels=['maths','english','science'])
colors=['teal','coral','green','purple']
for patch,color in zip (box['boxes'],colors):
    patch.set_color(color)
plt.show()

import numpy as np
x=np.linspace(0,10,200)
print(x)
y1=np.sin(x)
y2=np.cos(x)
fig,dev= plt.subplots(2,1)
dev[0].plot(x,y1,linestyle='--')
dev[0].set_title('line graph')
dev[1].plot(x,y2)
dev[1].set_title('bar graph')

plt.show()