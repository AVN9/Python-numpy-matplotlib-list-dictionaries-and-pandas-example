#Basic plot Data Visualization
import matplotlib.pyplot as plt

year=[1950,1951,1952,1953]

pop=[2.519,3.559,4.612,6.712]

plt.plot(year,pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projection')
plt.yticks([0,2,4,6,8,10],
			['0','2B','4B','6B','8B','10B'])
plt.show()
