import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import textwrap
import matplotlib.ticker as ticker

def get_max_value_and_plot(df, column_name, top_n=10):
    """
    Plots the top N most frequent values in a DataFrame column and returns the most common value(s).

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    column_name (str): The name of the column to analyze.
    top_n (int): The number of top values to display in the plot.

    Returns:
    list: The most common value(s) in the specified column.
    """
    # Error handling: Check if the column exists
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

    # Handle missing values and ensure data type is consistent
    df = df.dropna(subset=[column_name]).copy()  # Add .copy() to avoid SettingWithCopyWarning
    df[column_name] = df[column_name].astype(str)

    # Use value_counts for simplicity
    counts = df[column_name].value_counts().reset_index()
    counts.columns = [column_name, 'count']

    # Handle ties in the most common values
    max_count = counts['count'].max()
    most_common_values = counts[counts['count'] == max_count][column_name].tolist()

    # Get top N values for plotting
    top_values = counts.head(top_n)

    # Plotting with the updated code
    plt.figure(figsize=(8, 6))
    sns.barplot(
        data=top_values,
        x='count',
        y=column_name,
        hue=column_name,          # Assign the y variable to hue
        palette="viridis",
        dodge=False,              # Ensure bars are not offset
        legend=False              # Hide the legend
    )
    plt.title(f"{column_name.capitalize()} Counts", fontsize=12)
    plt.xlabel("Count", fontsize=10)
    plt.ylabel(column_name.capitalize(), fontsize=10)

    # Add data labels to the bars
    for index, value in enumerate(top_values['count']):
        plt.text(value, index, str(value), va='center', fontsize=8)

    plt.tight_layout()
    plt.show()

    return most_common_values


def get_max_female_decade_category(df):
    """
    Calculates the decade and category with the highest proportion of female Nobel laureates.

    Parameters:
        df (pd.DataFrame): DataFrame containing Nobel laureate data.

    Returns:
        dict: A dictionary with the decade as the key and category as the value.
    """
    # Drop rows with missing values in the 'sex' column
    df = df.dropna(subset=['sex']).copy()

    # Create a new column for the decade
    df['decade'] = (df['year'] // 10) * 10

    # Create a new column indicating whether the laureate is female
    df['female_winner'] = df['sex'] == 'Female'

    # Group by decade and category to calculate the proportion of female winners
    prop_female_winners = df.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()

    # Find the row with the highest proportion of female winners, prioritizing the most recent decade
    max_prop = prop_female_winners['female_winner'].max()
    max_female_decade_category = (
        prop_female_winners[prop_female_winners['female_winner'] == max_prop]
        .sort_values(by='decade', ascending=False)
        .iloc[0]
    )

    # Create a dictionary with the decade and category pair
    max_female_dict = {
        max_female_decade_category['decade']: max_female_decade_category['category']
    }

    return max_female_dict

def plot_gender_over_decades(df):
    """
    Creates a line plot showing the number of Nobel laureates by gender over decades.

    Parameters:
        df (pd.DataFrame): DataFrame containing Nobel laureate data.

    Returns:
        None
    """
    # Drop rows with missing values in the 'sex' column
    df = df.dropna(subset=['sex']).copy()

    # Create a new column for the decade
    df['decade'] = (df['year'] // 10) * 10

    # Group by decade and sex to calculate the count of laureates
    sex_decade_grouped = (
        df.groupby(['decade', 'sex'])
        .size()
        .reset_index(name='count')
    )

    # Define custom color palette
    custom_palette = {'Male': 'blue', 'Female': 'pink'}

    # Create a line plot
    plt.figure(figsize=(12, 6))
    sns.lineplot(
        data=sex_decade_grouped,
        x='decade',
        y='count',
        hue='sex',
        marker='o',
        palette=custom_palette
    )

    # Customize the plot
    plt.title('Number of Nobel Laureates by Gender Over Decades', fontsize=14)
    plt.xlabel('Decade', fontsize=12)
    plt.ylabel('Count of Laureates', fontsize=12)
    plt.legend(title='Gender', loc='upper left')
    plt.grid(axis='y')
    plt.tight_layout()

    # Show the plot
    plt.show()


def calculate_us_ratio_by_decade(df):
    """
    Calculates the ratio of US-born Nobel Prize winners to total winners by decade.

    Parameters:
        df (pd.DataFrame): DataFrame containing Nobel Prize data.

    Returns:
        pd.DataFrame: DataFrame with 'decade', 'total_winners', 'us_winners', and 'us_ratio' columns.
    """
    # Ensure required columns exist
    required_columns = ['year', 'birth_country', 'laureate_id']
    if not all(column in df.columns for column in required_columns):
        raise ValueError(f"DataFrame must contain the following columns: {', '.join(required_columns)}")

    # Create a new column for the decade
    df['decade'] = (df['year'] // 10) * 10

    # Create a new column indicating whether the laureate is US-born
    df['is_us_born'] = df['birth_country'] == 'United States of America'

    # Group by decade and calculate counts
    nobel_grouped = (
        df.groupby('decade')
        .agg(
            total_winners=('laureate_id', 'nunique'),
            us_winners=('is_us_born', 'sum')  # Sum the True values to count US-born winners
        )
        .reset_index()
    )

    # Calculate the ratio of US-born winners to total winners
    nobel_grouped['us_ratio'] = nobel_grouped['us_winners'] / nobel_grouped['total_winners']

    return nobel_grouped

def get_decade_with_highest_us_ratio(nobel_grouped):
    """
    Finds the decade with the highest ratio of US-born Nobel Prize winners.

    Parameters:
        nobel_grouped (pd.DataFrame): DataFrame with 'decade' and 'us_ratio' columns.

    Returns:
        int: The decade with the highest US-born winners ratio.
    """
    max_decade = int(nobel_grouped.loc[nobel_grouped['us_ratio'].idxmax(), 'decade'])
    return max_decade

def plot_us_ratio_over_decades(nobel_grouped):
    """
    Plots the ratio of US-born Nobel Prize winners to total winners by decade.

    Parameters:
        nobel_grouped (pd.DataFrame): DataFrame with 'decade' and 'us_ratio' columns.

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=nobel_grouped,
        x='decade',
        y='us_ratio',
        marker='o'
    )
    plt.title('Ratio of US-born Nobel Prize Winners to Total Winners by Decade', fontsize=14)
    plt.xlabel('Decade', fontsize=12)
    plt.ylabel('US-born Winners Ratio', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def get_first_female_laureate(df):
    """
    Finds the first female Nobel laureate.

    Parameters:
        df (pd.DataFrame): DataFrame containing Nobel laureate data.

    Returns:
        tuple: (name, category, year) of the first female laureate.
    """
    required_columns = ['sex', 'year', 'full_name', 'category']
    if not all(column in df.columns for column in required_columns):
        raise ValueError(f"DataFrame must contain the following columns: {', '.join(required_columns)}")

    # Drop rows with missing 'sex' values
    df = df.dropna(subset=['sex']).copy()

    # Filter for female laureates
    female_laureates = df[df['sex'] == 'Female']

    if female_laureates.empty:
        raise ValueError("No female laureates found in the dataset.")

    # Sort by year to find the first woman
    first_woman = female_laureates.sort_values(by='year').iloc[0]

    # Extract her name, category, and year
    first_woman_name = first_woman['full_name']
    first_woman_category = first_woman['category']
    first_woman_year = int(first_woman['year'])

    return first_woman_name, first_woman_category, first_woman_year

def plot_categories_of_female_laureates(df, first_woman_category):
    """
    Visualizes the number of female laureates by category, highlighting the first laureate's category.
    Adjusts the x-axis to range from 0 to 20 with ticks every 2 units.

    Parameters:
        df (pd.DataFrame): DataFrame containing Nobel laureate data.
        first_woman_category (str): The category of the first female laureate.

    Returns:
        None
    """
    required_columns = ['sex', 'category']
    if not all(column in df.columns for column in required_columns):
        raise ValueError(f"DataFrame must contain the following columns: {', '.join(required_columns)}")

    # Drop rows with missing 'sex' values
    df = df.dropna(subset=['sex']).copy()

    # Filter for female laureates
    female_laureates = df[df['sex'] == 'Female']

    # Count total female laureates by category
    category_counts = female_laureates['category'].value_counts().reset_index()
    category_counts.columns = ['category', 'count']

    # Add a column to highlight the first laureate's category
    category_counts['highlight'] = category_counts['category'].apply(
        lambda x: 'First Female Laureate\'s Category' if x == first_woman_category else 'Other Categories'
    )

    # Create the bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=category_counts,
        x='count',
        y='category',
        hue='highlight',
        dodge=False,
        palette={'First Female Laureate\'s Category': 'pink', 'Other Categories': 'gray'}
    )

    # Adjust the x-axis
    plt.xlim(0, 20)
    plt.xticks(range(0, 21, 2))  # Ticks from 0 to 20 with step of 2

    plt.title('Number of Female Nobel Laureates by Category', fontsize=14)
    plt.xlabel('Number of Female Laureates', fontsize=12)
    plt.ylabel('Category', fontsize=12)
    plt.legend(title='')
    plt.tight_layout()
    plt.show()


def get_repeat_winners(df):
    """
    Identifies individuals or organizations that have won more than one Nobel Prize.

    Parameters:
        df (pd.DataFrame): DataFrame containing Nobel Prize data.

    Returns:
        pd.DataFrame: DataFrame of repeat winners with their prize counts.
    """
    # Ensure required column exists
    if 'full_name' not in df.columns:
        raise ValueError("DataFrame must contain 'full_name' column.")

    # Drop rows with missing 'full_name' values
    df = df.dropna(subset=['full_name']).copy()

    # Group by full_name and count occurrences
    repeat_winners = (
        df.groupby('full_name')
        .size()
        .reset_index(name='prize_count')
    )

    # Filter for those with more than one prize
    repeat_winners = repeat_winners[repeat_winners['prize_count'] > 1]

    # Sort by prize_count descending
    repeat_winners = repeat_winners.sort_values(by='prize_count', ascending=False)

    return repeat_winners

def plot_repeat_winners(repeat_winners):
    """
    Creates a bar plot showing the number of Nobel Prizes won by repeat winners.

    Parameters:
        repeat_winners (pd.DataFrame): DataFrame containing repeat winners and their prize counts.

    Returns:
        None
    """
    # Wrap text for y-axis labels
    repeat_winners = repeat_winners.copy()
    repeat_winners['full_name_wrapped'] = repeat_winners['full_name'].apply(
        lambda x: '\n'.join(textwrap.wrap(x, width=20))
    )

    # Create a bar plot with wrapped y-axis labels
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=repeat_winners,
        x='prize_count',
        y='full_name_wrapped',
        hue='full_name_wrapped',  # Assign the y variable to hue
        palette='muted',
        dodge=False,              # Ensure bars are not offset
        legend=False              # Hide the legend
    )

    # Customize the plot
    plt.title('Number of Nobel Prizes Won by Repeat Winners', fontsize=14)
    plt.xlabel('Number of Prizes', fontsize=12)
    plt.ylabel('Laureate', fontsize=12)

    # Ensure x-axis ticks are integers only
    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

    plt.tight_layout()
    plt.show()
