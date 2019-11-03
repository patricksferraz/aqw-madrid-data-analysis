# %%

import pandas as pd

# %% [markdown]

# ## Global variables

# %%

ARGS = {
    "wt-madrid": "dataset/extract/wt_madrid.h5",
    "aq-madrid": "dataset/extract/aq_madrid.h5",
}

# %% [markdown]

# ## Functions

# %%


# Function for dataframe describe
def describe_data(
    data_frame: pd.DataFrame, headers: [str] = None
) -> pd.DataFrame:
    """This function describe the datas of a dataframe. Returning the max,
    min, mean, median, quantile, variance, standard deviation,
    mean absolute deviation, amplitude, root mean squared, kurtosis, skewness
    and count for all headers in dataframe

    Parameters
    ----------
    data_frame : pd.DataFrame
        Dataframe of input
    headers : [str], optional
        Chosen dataframe headers, by default None

    Returns
    -------
    pd.DataFrame
        Dataframe with the descriptions
    """

    FIRST_QUARTILE = 0.25
    THIRD_QUARTILE = 0.75
    IQR_CONSTANT = 1.5

    def _apply(header: str, column: []):
        _max = column.max()
        _min = column.min()

        # Scatter
        _q1 = column.quantile(FIRST_QUARTILE)
        _q3 = column.quantile(THIRD_QUARTILE)
        _iqr = _q3 - _q1
        _lower = max(_min, _q1 - (IQR_CONSTANT * _iqr))
        _upper = min(_max, _q3 + (IQR_CONSTANT * _iqr))

        return {
            "header": header,
            "max": _max,
            "min": _min,
            "mean": column.mean(),
            "median": column.median(),
            "lower limit": _lower,
            "1-quartile": _q1,
            "3-quartile": _q3,
            "upper limit": _upper,
            "var": column.var(),
            "std": column.std(),
            "mad": column.mad(),
            "amp": _max - _min,
            "rms": (column.pow(2)).mean() ** 0.5,
            "kurtosis": column.kurtosis(),
            "skew": column.skew(),
            "count": column.count(),
            "nans": column.isna().sum(),
        }

    if not headers:
        headers = data_frame.columns

    return pd.DataFrame(
        [_apply(_, data_frame.loc[:, _]) for _ in headers]
    ).set_index("header")


# %% [markdown]

# ## Datasets

# %% [markdown]

# ### Weather Madrid 1997 - 2015
#
# Weather data Barajas Airport, Madrid, between 1997 and 2015. Gathered web
# https://www.wunderground.com/ The Weather Company, LLC
#
# Fields:
# - Max TemperatureC
# - Mean TemperatureC
# - Min TemperatureC
# - Dew PointC
# - MeanDew PointC
# - Min DewpointC
# - Max Humidity
# - Mean Humidity
# - Min Humidity
# - Max Sea Level PressurehPa
# - Mean Sea Level PressurehPa
# - Min Sea Level PressurehPa
# - Max VisibilityKm
# - Mean VisibilityKm
# - Min VisibilitykM
# - Max Wind SpeedKm/h
# - Mean Wind SpeedKm/h
# - Max Gust SpeedKm/h
# - Precipitationmm
# - CloudCover
# - Events
# - WindDirDegrees

# %%

# Load wt-madrid and show your keys
df_wt = pd.HDFStore(ARGS.get("wt-madrid"))
df_wt.keys()

# %%

# Show values of man key
df_wt.get("master")

# %% [markdown]

# ---

# %% [markdown]

# ### Air Quality in Madrid (2001-2018)
# Includes daily and hourly historical air quality data of the levels
# registered from 2001 to 2018 and the list of stations being used for
# pollution and other particles analysis in the city.
#
# Fields:
# - SO_2: sulphur dioxide level measured in μg/m³. High levels of sulphur
# dioxide can produce irritation in the skin and membranes, and worsen asthma
# or heart diseases in sensitive groups.
# - CO: carbon monoxide level measured in mg/m³. Carbon monoxide poisoning
# involves headaches, dizziness and confusion in short exposures and can result
# in loss of consciousness, arrhythmias, seizures or even death in the long
# term.
# - NO: nitric oxide level measured in μg/m³. This is a highly corrosive gas
# generated among others by motor vehicles and fuel burning processes.
# - NO_2: nitrogen dioxide level measured in μg/m³. Long-term exposure is a
# cause of chronic lung diseases, and are harmful for the vegetation.
# - PM25: particles smaller than 2.5 μm level measured in μg/m³. The size of
# these particles allow them to penetrate into the gas exchange regions of the
# lungs (alveolus) and even enter the arteries. Long-term exposure is proven to
# be related to low birth weight and high blood pressure in newborn babies.
# - PM10: particles smaller than 10 μm. Even though the cannot penetrate the
# alveolus, they can still penetrate through the lungs and affect other organs.
# Long term exposure can result in lung cancer and cardiovascular complications
# - NOx: nitrous oxides level measured in μg/m³. Affect the human respiratory
# system worsening asthma or other diseases, and are responsible of the
# yellowish-brown color of photochemical smog.
# - O_3: ozone level measured in μg/m³. High levels can produce asthma,
# bronchytis or other chronic pulmonary diseases in sensitive groups or outdoor
# workers.
# - TOL: toluene (methylbenzene) level measured in μg/m³. Long-term exposure to
# this substance (present in tobacco smkoke as well) can result in kidney
# complications or permanent brain damage.
# - BEN: benzene level measured in μg/m³. Benzene is a eye and skin irritant,
# and long exposures may result in several types of cancer, leukaemia and
# anaemias. Benzene is considered a group 1 carcinogenic to humans by the IARC.
# - EBE: ethylbenzene level measured in μg/m³. Long term exposure can cause
# hearing or kidney problems and the IARC has concluded that long-term exposure
# can produce cancer.
# - MXY: m-xylene level measured in μg/m³. Xylenes can affect not only air but
# also water and soil, and a long exposure to high levels of xylenes can result
# in diseases affecting the liver, kidney and nervous system (especially memory
# and affected stimulus reaction).
# - PXY: p-xylene level measured in μg/m³. See MXY for xylene exposure effects
# on health.
# - OXY: o-xylene level measured in μg/m³. See MXY for xylene exposure effects
# on health.
# - TCH: total hydrocarbons level measured in mg/m³. This group of substances
# can be responsible of different blood, immune system, liver, spleen, kidneys
# or lung diseases.
# - CH4: methane level measured in mg/m³. This gas is an asphyxiant, which
# displaces the oxygen animals need to breath. Displaced oxygen can result in
# dizzinnes, weakness, nausea and loss of coordination.
# - NMHC: non-methane hydrocarbons (volatile organic compounds) level measured
# in mg/m³. Long exposure to some of these substances can result in damage to
# the liver, kidney, and central nervous system. Some of them are suspected to
# cause cancer in humans.

# %%

# Load aq-madrid and show keys
df_aq = pd.HDFStore(ARGS["aq-madrid"])
df_aq.keys()

# %% [markdown]

# #### Stations

# %%

df_aq.get("master")

# %% [markdown]

# #### Values of each station
