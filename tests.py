import pytest
import pandas as pd
import numpy as np
from app import calculate_metrics

def test_calculate_metrics_logic():
    """
    Test that SMA calculation is mathematically correct.
    """
    # Create dummy data: 200 days of increasing prices
    data = {'Close': [x for x in range(1, 201)]} 
    df = pd.DataFrame(data)
    
    # Run the function
    result = calculate_metrics(df)
    
    # Check SMA 50
    # The mean of 1 to 50 is 25.5
    # The value at index 49 (50th day) should be 25.5
    assert result['SMA50'].iloc[49] == 25.5
    
    # Check SMA 200
    # The mean of 1 to 200 is 100.5
    # The value at index 199 should be 100.5
    assert result['SMA200'].iloc[199] == 100.5

def test_insufficient_data():
    """Test that it handles data shorter than the window gracefully (returns NaN)."""
    data = {'Close': [1, 2, 3]}
    df = pd.DataFrame(data)
    result = calculate_metrics(df)
    
    # SMA50 should be NaN because we only have 3 data points
    assert pd.isna(result['SMA50'].iloc[-1])