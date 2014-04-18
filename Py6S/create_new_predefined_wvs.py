import numpy as np
from scipy.interpolate import interp1d
import pandas as pd


def import_from_excel(filename, sheetid):
	df = pd.read_excel(filename, sheetid)
	f = interp1d(df.ix[:,0], df.ix[:,1])
	minwv = df.ix[:,0].min()

	newwvs = np.arange(minwv, df.ix[:,0].max(), 2.5)

	maxwv = newwvs.max()

	values = f(newwvs)

	print "%.3f, %.3f,\nnp.%s)" % (minwv/1000.0, maxwv/1000.0, values.__repr__())