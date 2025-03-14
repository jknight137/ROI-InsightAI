import pandas as pd
import numpy as np

np.random.seed(42)
num_samples = 500

data = {
    "budget_usd": np.random.randint(50000, 500000, num_samples),
    "employees_impacted": np.random.randint(10, 500, num_samples),
    "duration_months": np.random.randint(3, 24, num_samples),
    "risk_level": np.random.choice(["low", "medium", "high"], num_samples),
}

risk_map = {"low": 1, "medium": 2, "high": 3}
data["risk_numeric"] = [risk_map[risk] for risk in data["risk_level"]]

data["success"] = np.where(
    (data["risk_numeric"] * data["budget_usd"] / data["employees_impacted"]) > 7500,
    0,
    1,
)

df = pd.DataFrame(data)
df.to_csv("synthetic_roi_data.csv", index=False)
print("Synthetic data generated and saved as synthetic_roi_data.csv")
