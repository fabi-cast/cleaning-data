def null_cols(data):

    """
    This function takes a dataframe df and shows the columns of df that have NaN values
    and the number of them

    """

    nulls = data.isna().sum()
    return nulls[nulls > 0] / len(data) * 100

def detect_low_variance(data, col, n= 90):

    """
    This function takes a dataframe data, a column col from data
    and a number n between 0 and 100.
    Returns True if the minimum value of column is equal to its n-th percentile
    and False otherwise. The predetermined value of the percentile is 90.
    """
    min_val = data[col].min()
    perc_val = np.percentile(data[col], perc)
    return min_val == perc_val

def drop_low_variance(data, n= 90):

    """
    Takes a dataframe data and a number n between 0 and 100.
    It returns a dataframe after removing the numerical columns having low
    variance having as a reference the value n.
    """

    low_var_cols = [col for col in data.select_dtypes(include = [np.number]).columns if detect_low_variance(data, col, n)]
    return data.drop(low_var_cols, axis=1)

def iqr(data, cols, t=1.5):

    """
    This function computes the interquartal range with rule t.
    "data" is a dataframe, "cols" is a list of columns with numerical values
    from "data" and "t" is a positive number. By default t takes the value 1.5.
    iqr returns a dictionary of dictionaries containing the lower and upper
    extremes of the adjusted IQR for each column.
    """
    Q1 = data[cols].quantile(0.25)
    Q3 = data[cols].quantile(0.75)
    IQR = Q3-Q1
    low_bound = {}
    upp_bound = {}
    for col in list(IQR.index):
        low_bound[col] = Q1[col]-t*IQR[col]
        upp_bound[col] = Q3[col]+t*IQR[col]
    return {"low_b": low_bound, "upp_b": upp_bound}

def drop_outliers(data, cols, t=1.5):

    """
    Takes a dataset data, a list of columns cols with numerical values and a positive
    number t which is the rule for calculating the interquartal range.
    Returns a data set without outliers removed accourding with the rule t.
    """
    iqr_d = iqr(data, cols, t)
    for col in cols:
    return data[~((data[col]< iqr_d["low_b"][col]) | (data[col]> iqr_d["upp_b"][col]))]
