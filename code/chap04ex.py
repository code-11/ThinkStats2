import random
import thinkstats2
import thinkplot

list_o_nums=[]
for i in range(1000):
	list_o_nums.append(random.random())
cdf=thinkstats2.Cdf(list_o_nums)
pmf=thinkstats2.Pmf(list_o_nums)
thinkplot.Cdf(cdf)
thinkplot.show()
# thinkplot.Pmf(pmf)
# thinkplot.show()