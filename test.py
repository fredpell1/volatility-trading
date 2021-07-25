import volatility.volest as volest
import volatility.data as data

# data
symbol = 'JPM'
bench = '^GSPC'
data_file_path = r'C:\Users\frede\OneDrive\Documents\Concordia\HedgeFund\volatility-trading\tests\BENCH.csv'
bench_file_path = r'C:\Users\frede\OneDrive\Documents\Concordia\HedgeFund\volatility-trading\tests\JPM.csv'
estimator = 'Kurtosis'


# estimator windows
window = 30
windows = [30, 60, 90, 120]
quantiles = [0.25, 0.75]
bins = 100
normed = True

# use the yahoo helper to correctly format data from finance.yahoo.com
jpm_price_data = data.yahoo_helper(symbol, data_file_path)
spx_price_data = data.yahoo_helper(bench, bench_file_path)

# initialize class
vol = volest.VolatilityEstimator(
    price_data=jpm_price_data,
    estimator=estimator,
    bench_data=spx_price_data
)


_, plt = vol.cones(windows=windows, quantiles=quantiles)
plt.show()


"""

# call plt.show() on any of the below...
_, plt = vol.cones(windows=windows, quantiles=quantiles)
_, plt = vol.rolling_quantiles(window=window, quantiles=quantiles)
_, plt = vol.rolling_extremes(window=window)
_, plt = vol.rolling_descriptives(window=window)
_, plt = vol.histogram(window=window, bins=bins, normed=normed)

_, plt = vol.benchmark_compare(window=window)
_, plt = vol.benchmark_correlation(window=window)

# ... or create a pdf term sheet with all metrics in term-sheets/
vol.term_sheet(
    window,
    windows,
    quantiles,
    bins,
    normed
)

"""
