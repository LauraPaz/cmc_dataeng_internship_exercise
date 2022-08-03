import pandas as pd
import numpy as np
import random

compounds = [
    "biguanide",
    "thiazolidinedione",
    "sulfonylureas",
    "meglitinides",
    "vanadyl_sulfate",
]
sample_day_month = [
    ("31", "12"),
    ("27", "12"),
    ("18", "12"),
    ("6", "11"),
    ("1", "11"),
    ("31", "10"),
    ("27", "10"),
    ("18", "10"),
    ("6", "9"),
    ("1", "9"),
]
sample_day = [_[0] for _ in sample_day_month]
sample_month = [_[1] for _ in sample_day_month]
runtime = [random.random() for _ in range(len(sample_day_month))]
measurements = pd.DataFrame(np.random.randn(10, 5), columns=compounds).abs()
equipments = pd.DataFrame(
    {
        "sample_day": sample_day,
        "sample_month": sample_month,
        "runtime": runtime,
    }
)
equipments.index.name = "equipment_name"

# exercise 2.1 Get the random measurement of the equipment 2
# for meglitinides sampled the 18th of Decembre
equipment_measurements = None  # dataframe

# solution start
equipment_measurements = equipments.join(measurements) # or concat
equipment_measurements['equipment_id'] = ['EQ'+str(i) for i in equipment_measurements.index]
equipment_measurements.set_index(['equipment_id', 'sample_day', 'sample_month'], inplace=True)
# solution end

keys = ("EQ2", "18", "12")
compound = "meglitinides"
meglitinides_measurement = equipment_measurements.loc[keys, compound]  # float

# exercise 2.2 Get the average runtime per month for the
# equipments that measured quantities of sulfonylureas
# and of biguanide that are greater than meglitinides_measurement
avg_monthly_runtime = None  # dataframe

# solution start
filtered_measurements = equipment_measurements[(equipment_measurements['biguanide'] > equipment_measurements['meglitinides']) & (equipment_measurements['sulfonylureas'] > equipment_measurements['meglitinides'])]
avg_monthly_runtime = filtered_measurements.groupby(['sample_month'])['runtime'].mean()
# solution end
