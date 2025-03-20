# Dataset Checker User Guide

## Introduction

Dataset Checker is a comprehensive Python library designed to help data scientists and machine learning practitioners ensure high-quality datasets. It provides tools for detecting and fixing common data quality issues such as missing values, outliers, duplicates, format inconsistencies, class imbalance, and non-normal distributions.

## Installation

```bash
# Install from PyPI
pip install dataset-checker

# Or install from source
git clone https://github.com/JonusNattapong/Dataset-checker.git
cd Dataset-checker
pip install -e .
```

## Quick Start

```python
import pandas as pd
from dataset_checker import DatasetChecker

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# Create a checker instance
checker = DatasetChecker(df)

# Run a comprehensive quality check
report = checker.run_quality_check()

# View report summary
print(report.summary())

# Generate a comprehensive report
report.to_html('dataset_quality_report.html')
```

## Main Components

### DatasetChecker

The `DatasetChecker` class is the main entry point for checking and improving dataset quality. It provides methods for detecting and addressing various quality issues.

```python
from dataset_checker import DatasetChecker

# Initialize with your dataset
checker = DatasetChecker(df, name="my_dataset")

# Run individual checks
checker.check_missing_values()
checker.check_outliers(method='zscore', threshold=3.0)
checker.check_duplicates(fuzzy=True, threshold=0.9)
checker.check_data_format()
checker.check_data_balance(target_column='target')
checker.check_data_distribution()

# Fix issues
checker.fix_missing_values(strategy='auto')
checker.remove_outliers(method='zscore')
checker.remove_duplicates(keep='first')

# Run comprehensive check
report = checker.run_quality_check()
```

### QualityReport

The `QualityReport` class provides tools for visualizing and understanding the results of quality checks.

```python
# Get report from checker
report = checker.run_quality_check()

# View summary
print(report.summary())

# View recommendations
print(report.view_recommendations())

# Visualize issues
report.plot_missing_values()
report.plot_outliers()
report.plot_class_balance()

# Export report
report.to_html('report.html')
report.to_json('report.json')
```

## Quality Checks

### Missing Values

Detects and handles missing values in your dataset.

```python
# Check for missing values
result = checker.check_missing_values()

# Fix missing values
checker.fix_missing_values(strategy='auto')  # Auto-selects best strategy per column
checker.fix_missing_values(strategy='mean')  # Use mean for numerical columns
checker.fix_missing_values(strategy='median')  # Use median for numerical columns
checker.fix_missing_values(strategy='mode')  # Use mode for categorical columns
checker.fix_missing_values(strategy='constant', fill_values={'col1': 0, 'col2': 'Unknown'})  # Custom values
```

### Outlier Detection

Identifies and handles statistical outliers in your dataset.

```python
# Check for outliers
checker.check_outliers(method='zscore', threshold=3.0)  # Z-score method
checker.check_outliers(method='iqr', threshold=1.5)  # IQR method
checker.check_outliers(method='isolation_forest')  # Isolation Forest method

# Remove outliers
checker.remove_outliers(method='zscore')  # Remove detected outliers
checker.remove_outliers(strategy='cap')  # Cap outliers at threshold values
checker.remove_outliers(strategy='mean')  # Replace outliers with column mean
checker.remove_outliers(strategy='median')  # Replace outliers with column median
```

### Duplicate Detection

Finds and removes duplicate records in your dataset.

```python
# Check for duplicates
checker.check_duplicates()  # Exact duplicates
checker.check_duplicates(columns=['col1', 'col2'])  # Duplicates in specific columns
checker.check_duplicates(fuzzy=True, threshold=0.9)  # Fuzzy matching for text data

# Remove duplicates
checker.remove_duplicates(keep='first')  # Keep first occurrence
checker.remove_duplicates(keep='last')  # Keep last occurrence
checker.remove_duplicates(keep=False)  # Remove all duplicates
```

### Data Format Validation

Validates data formats and ensures consistency.

```python
# Check data formats
checker.check_data_format()  # Auto-infer formats
checker.check_data_format(format_rules={
    'email_col': 'email',
    'date_col': 'date',
    'phone_col': 'phone',
    'url_col': 'url',
    'zipcode_col': 'zipcode',
    'ip_col': 'ip'
})
```

### Class Balance Analysis

Analyzes class distribution for classification datasets.

```python
# Check class balance
checker.check_data_balance(target_column='target')

# Balance the dataset
from dataset_checker.checks import data_balance

# Using undersampling
balanced_df = data_balance.balance_dataset(
    df, target_column='target', method='undersample'
)

# Using oversampling
balanced_df = data_balance.balance_dataset(
    df, target_column='target', method='oversample'
)

# Using SMOTE (if imbalanced-learn is installed)
balanced_df = data_balance.balance_dataset(
    df, target_column='target', method='smote'
)
```

### Distribution Analysis

Analyzes feature distributions and provides transformations for non-normal data.

```python
# Check distributions
dist_results = checker.check_data_distribution()

# Transform skewed columns
from dataset_checker.checks import data_distribution

# Auto-select transformation
transformed_df = data_distribution.transform_non_normal(
    df, method='auto'
)

# Specific transformations
transformed_df = data_distribution.transform_non_normal(
    df, columns=['col1', 'col2'], method='log'
)
transformed_df = data_distribution.transform_non_normal(
    df, columns=['col3'], method='boxcox'
)
```

## Workflow Example

```python
import pandas as pd
from dataset_checker import DatasetChecker

# Load data
df = pd.read_csv('your_dataset.csv')

# Initialize checker
checker = DatasetChecker(df, name="my_dataset")

# Run comprehensive check
report = checker.run_quality_check()

# Print summary and recommendations
print(report.summary())
print(report.view_recommendations())

# Fix issues based on recommendations
checker.fix_missing_values(strategy='auto')
checker.remove_duplicates()
checker.remove_outliers(method='zscore')

# Get the cleaned dataset
clean_df = checker.data

# Save cleaned dataset
clean_df.to_csv('cleaned_dataset.csv', index=False)

# Generate detailed report
report.to_html('quality_report.html')
```

## Advanced Features

### Custom Format Rules

```python
# Define custom format rules
format_rules = {
    'email': 'email',
    'date_registered': 'date',
    'phone_number': 'phone',
    'website': 'url',
    'postal_code': 'zipcode',
    'ip_address': 'ip',
    'is_active': 'boolean'
}

# Check formats with custom rules
checker.check_data_format(format_rules=format_rules)
```

### Custom Balancing Strategy

```python
# Define custom sampling strategy
sampling_strategy = {
    'class_0': 100,
    'class_1': 100,
    'class_2': 100
}

# Balance dataset with custom strategy
from dataset_checker.checks import data_balance
balanced_df = data_balance.balance_dataset(
    df, target_column='target', method='oversample', 
    sampling_strategy=sampling_strategy
)
```

## Best Practices

1. **Run a comprehensive check first**: Always start by running a comprehensive quality check to get an overview of potential issues.

2. **Fix issues in the right order**:
   - Fix missing values first
   - Remove duplicates
   - Handle outliers
   - Fix format issues
   - Address imbalance issues
   - Transform distributions

3. **Save original data**: Always keep a copy of your original data to compare with the cleaned version.

4. **Validate after cleaning**: Run a new quality check after fixing issues to ensure your changes improved data quality.

5. **Document your data cleaning process**: Save the quality reports and keep track of what changes were made.

6. **Use visualizations**: Visualize your data before and after cleaning to better understand the impact of your changes.

## FAQ

### Q: How do I handle time series data?
A: When dealing with time series data, be careful when removing outliers as they might represent important events. Consider using the 'cap' strategy instead of removing rows.

### Q: What's the best way to handle missing values?
A: The 'auto' strategy analyzes each column's data type and distribution to select the most appropriate strategy, which is recommended for most cases.

### Q: How do I choose a threshold for outlier detection?
A: A Z-score threshold of 3.0 is generally good for normally distributed data. For skewed data, the IQR method with a threshold of 1.5 might be more appropriate.

### Q: Can I use this library for big datasets?
A: Yes, but some operations (like fuzzy duplicate detection) might be slower on very large datasets. Consider sampling your data first if performance is an issue.

### Q: How do I interpret the quality score?
A: The quality score ranges from 0 to 1, where 1 represents a perfect dataset. A score above 0.8 is generally considered good. The score is a weighted average of individual check scores.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
