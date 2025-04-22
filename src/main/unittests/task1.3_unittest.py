# Unit Test for Task 1.3: Call Load Data Function
import unittest
import os
import sys
import re

# Add the parent directory to path so we can import the module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..', 'python')
sys.path.append(parent_dir)

class TestCallLoadDataFunction(unittest.TestCase):
    def test_call_load_data_function(self):
        """Test that the main block properly calls the load_data function"""
        print(f"\nCHECKING TASK 1.3: CALL LOAD DATA FUNCTION")
        print("="*50)
        
        # Check if the file exists
        file_path = os.path.join(parent_dir, 'sales_analysis.py')
        print(f"Checking if {file_path} exists...")
        self.assertTrue(os.path.exists(file_path), 
                        f"sales_analysis.py file not found. Make sure it's in the correct location.")
        print(f"File found at {file_path}")
        
        # Read the file content
        print("\nReading file content...")
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Check for main block
        print("\nChecking for if __name__ == '__main__' block...")
        if "__name__ == '__main__'" in content or '__name__ == "__main__"' in content:
            print("✓ Main block is present")
        else:
            print("✗ ERROR: Main block is missing!")
            print("  SOLUTION: Add 'if __name__ == \"__main__\":' block at the end of your file")
            self.fail("Main block is missing")
        
        # Check for load_data call within main block
        main_block_pattern = re.compile(r"if\s+__name__\s*==\s*['\"]__main__['\"]\s*:(.*?)(?:\n\S|$)", re.DOTALL)
        main_block_match = main_block_pattern.search(content)
        
        if main_block_match:
            main_block_content = main_block_match.group(1)
            
            # Check for load_data call
            print("\nChecking for load_data function call...")
            load_data_pattern = re.compile(r"(\w+)\s*=\s*load_data\s*\(\s*['\"]sales_data\.csv['\"]\s*\)")
            load_data_match = load_data_pattern.search(main_block_content)
            
            if load_data_match:
                var_name = load_data_match.group(1)
                print(f"✓ load_data is called with 'sales_data.csv' and stored in variable '{var_name}'")
                
                # Check if it's stored in sales_df
                if var_name == 'sales_df':
                    print("✓ Result is stored in the correct variable 'sales_df'")
                else:
                    print(f"✗ WARNING: Result is stored in '{var_name}' instead of 'sales_df'")
                    print("  SOLUTION: Use 'sales_df = load_data(\"sales_data.csv\")' in your main block")
            else:
                print("✗ ERROR: load_data is not called correctly!")
                print("  SOLUTION: Add 'sales_df = load_data(\"sales_data.csv\")' to your main block")
                self.assertTrue(load_data_pattern.search(main_block_content), 
                              "load_data should be called with 'sales_data.csv'")
            
            # Check for printing loaded data
            print("\nChecking for code to print loaded data...")
            print_pattern = re.compile(r"print\s*\(.*?\.head\(\s*\)\s*\)")
            if print_pattern.search(main_block_content):
                print("✓ Code to print the first few rows of loaded data is present")
            else:
                print("✗ ERROR: No code to print loaded data!")
                print("  SOLUTION: Add 'print(sales_df.head())' to your main block")
                self.assertTrue(print_pattern.search(main_block_content), 
                              "Missing code to print first few rows of loaded data")
        else:
            print("✗ ERROR: Could not parse main block content")
            self.fail("Could not parse main block content")
        
        print("\nTASK 1.3 COMPLETE! The load_data function is correctly called in the main block.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
