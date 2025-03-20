"""
Simple test script to verify the installation and basic functionality of Dataset Checker
"""

import pandas as pd
import numpy as np
from dataset_checker import DatasetChecker

def create_test_dataset():
    """Create a tiny test dataset with some quality issues"""
    # Create a small dataframe with common issues
    data = {
        'age': [25, 30, 45, 90, 35, np.nan, 32, 30, 45],
        'income': [50000, 60000, 75000, 800000, 65000, 55000, 52000, 60000, 75000],
        'gender': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F', 'M'],
        'email': ['user1@example.com', 'user2@example.com', 'user3@example.com', 
                  'invalid-email', 'user5@example.com', 'user6@example.com', 
                  'user7@example.com', 'user2@example.com', 'user3@example.com'],
        'status': ['active', 'inactive', 'active', 'active', 'inactive', np.nan, 'active', 'inactive', 'active']
    }
    
    return pd.DataFrame(data)

def main():
    print("=" * 50)
    print("Dataset Checker Installation Test")
    print("=" * 50)
    
    # Create test dataset
    print("\nCreating test dataset...")
    df = create_test_dataset()
    
    print("\nTest dataset preview:")
    print(df.head(3))
    print(f"Shape: {df.shape}")
    
    # Initialize DatasetChecker
    print("\nInitializing DatasetChecker...")
    try:
        checker = DatasetChecker(df, name="test_dataset")
        print("✓ DatasetChecker initialized successfully!")
    except Exception as e:
        print(f"✗ Failed to initialize DatasetChecker: {str(e)}")
        return
    
    # Run basic checks
    print("\nRunning basic quality checks...")
    
    try:
        # Check missing values
        missing_result = checker.check_missing_values()
        print(f"✓ Missing values check complete: found {missing_result['total_missing']} missing values")
        
        # Check outliers
        outlier_result = checker.check_outliers()
        print(f"✓ Outlier check complete: found {outlier_result['total_outliers']} outliers")
        
        # Check duplicates
        duplicate_result = checker.check_duplicates()
        print(f"✓ Duplicate check complete: found {duplicate_result['total_duplicates']} duplicates")
        
        # Run comprehensive check
        print("\nRunning comprehensive quality check...")
        report = checker.run_quality_check()
        print("✓ Comprehensive quality check complete!")
        
        # Print summary
        print("\nQuality Report Summary:")
        print("-" * 40)
        print(report.summary())
        
        print("\n✓ All tests passed! Dataset Checker is working correctly.")
        
    except Exception as e:
        print(f"\n✗ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
