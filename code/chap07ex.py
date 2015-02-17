import thinkstats2
import thinkplot
import nsfg
import math
import numpy
import sys

def print_full(x):
	x.to_csv(sys.stdout)

df = nsfg.ReadFemPreg()
weights=df.totalwgt_lb

print([1,2,3,4,5][1:-1])

nums=[1,2,3,4,5]
new_nums=[]
for i in range(len(nums)-1):
	if (i!=0 and i!=len(nums)):
		new_nums.append(nums[i])
print (new_nums)

# bins = numpy.arange(10, 48, 3)
# indices = numpy.digitize(df.agepreg, bins)
# groups = df.groupby(indices)

# ages=[]
# cdfs=[]
# for i,group in groups:
# 	if not(i==0 or i==len(groups)-1):
# 		ages.append(group.agepreg.mean())
# 		cdfs.append(thinkstats2.Cdf(group.totalwgt_lb))

# for percent in [75,50,25]:
# 	weights=[]
# 	weights = [cdf.Percentile(percent) for cdf in cdfs]
# 	# for cdf in cdfs:
# 	# 	weights.append(cdf.Percentile(percent))
# 	thinkplot.Plot(ages, weights, label=label)


#thinkplot.Scatter(ages,weights)
#thinkplot.Show()