import numpy as np
import pandas as pd

def raw_df():
    dat = """ts;A;B;C
    2015-01-01 00:00:00;27451873;29956800;113
    2015-01-01 01:00:00;20259882;17906600;76
    2015-01-01 02:00:00;11592256;12311600;48
    2015-01-01 03:00:00;11795562;11750100;50
    2015-01-01 04:00:00;9396718;10203900;43
    2015-01-01 05:00:00;14902826;14341100;53"""

    from pandas.compat import StringIO
    df = pd.read_csv(StringIO(dat), sep=';', index_col='ts', parse_dates='ts')
    return df

def random_walk_df(dt_start='2015-01-01', periods=600, freq='1D', offset=800, columns=list('ABC')):
    index = pd.date_range(dt_start, periods=periods, freq=freq)
    df = pd.DataFrame(np.random.randn(periods, len(columns)), index=index, columns=columns)
    df = df.cumsum() + offset
    return df
