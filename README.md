# Nobel Prize Data Analysis Project

## 📋 Project Overview
This project analyzes historical Nobel Prize data to uncover interesting patterns, trends, and insights. Using Python, pandas, and Seaborn, the analysis explores various aspects of the Nobel Prize dataset, including the demographics of laureates, trends over decades, and gender representation.

## 📊 Key Insights
1. **Top Gender and Country**:
   - The most awarded gender is **Male**.
   - The most common birth country of laureates is the **United States of America**.
   
2. **Proportion of Female Winners**:
   - The decade with the highest proportion of female laureates in a specific category is **2020** in the **Literature** category.

3. **Proportion of USA Winners**:
   - The highest proportion of USA-born winners occurred in the **2000s decade**.

4. **Repeat Winners**:
   - Identified individuals and organizations who have won the Nobel Prize multiple times.

5. **Gender Trends**:
   - Visualized the evolution of male and female laureates over the decades.

---

## 🚀 Features
### Analysis
- **Top Gender and Country**: Determines the most awarded gender and the most common birth country.
- **Proportions**: Calculates the proportion of USA-born winners and female laureates by decade and category.
- **Repeat Winners**: Identifies repeat laureates and their categories.
- **Trend Analysis**: Analyzes gender representation trends over time.

### Visualizations
- **Bar Charts**:
  - Proportions of female winners by category.
  - Number of prizes won by repeat laureates.
- **Line Plots**:
  - Evolution of male vs. female laureates over decades.
  - Proportion of USA-born winners over time.
- **Scatter Plots**:
  - Timeline of female laureates by category.


---

## 🛠️ Tools & Libraries
- **Python**: Core programming language.
- **pandas**: Data manipulation and analysis.
- **Seaborn**: Data visualization.
- **Matplotlib**: Supporting visualization framework.
- **Jupyter Notebook**: For interactive code execution and exploration.

---

## 🗂️ Dataset
- **Source**: Nobel Prize dataset (`nobel.csv`).
- **Columns**:
  - `year`: The year of the award.
  - `category`: The category of the award (e.g., Physics, Peace).
  - `laureate_id`: Unique identifier for each laureate.
  - `full_name`: Full name of the laureate.
  - `sex`: Gender of the laureate.
  - `birth_country`: Birth country of the laureate.
  - `organization_name`: Affiliation of the laureate.
  - Additional columns for demographic and affiliation details.

---

## 🖼️ Example Outputs
### Visualizations
1. **Proportion of Female Laureates by Decade**:
   ![Line Plot Example](example-line-plot.png)
2. **Bar Plot for Repeat Laureates**:
   ![Bar Plot Example](example-bar-plot.png)

---

## 📂 Folder Structure
```
nobel_prize_laureates/
│
├── data/
│   └── nobel.csv
│
├── notebooks/
│   └── main.ipynb
│
├── scripts/
│   └── functions.py
│
├── README.md
```

---

## 🧑‍💻 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/username/Nobel_Prize_Analysis.git
   cd Nobel_Prize_Analysis
   ```
2. Install the required libraries:
   ```bash
   pip install pandas seaborn matplotlib
   ```
3. Open the Jupyter Notebook:
   ```bash
   jupyter notebook notebooks/notebook.ipynb
   ```

---

## 🌟 Future Work
- Include regional analysis of laureates by continent.
- Predict future trends in gender representation using machine learning.
- Expand analysis to include collaborations and shared prizes.

---

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## 💬 Feedback
Feel free to submit issues or pull requests for enhancements and bug fixes. Contributions are welcome!
