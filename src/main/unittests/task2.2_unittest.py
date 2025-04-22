# Unit Test for Task 2.2: Call Clean Data Function
import unittest
import os
import sys
import re

# Add the parent directory to path so we can import the module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..', 'python')
sys.path.append(parent_dir)

class TestCallCleanDataFunction(unittest.TestCase):
    def test_call_clean_data_function(self):
        """Test that the main block properly calls the clean_data function"""
        print(f"\nCHECKING TASK 2.2: CALL CLEAN DATA FUNCTION")
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
        
        # Check for clean_data call within main block
        main_block_pattern = re.compile(r"if\s+__name__\s*==\s*['\"]__main__['\"]\s*:(.*?)(?:\n\S|$)", re.DOTALL)
        main_block_match = main_block_pattern.search(content)
        
        if main_block_match:
            main_block_content = main_block_match.group(1)
            
            # Check for clean_data call
            print("\nChecking for clean_data function call...")
            clean_data_pattern = re.compile(r"(\w+)\s*=\s*clean_data\s*\(\s*sales_df\s*\)")
            clean_data_match = clean_data_pattern.search(main_block_content)
            
            if clean_data_match:
                var_name = clean_data_match.group(1)
                print(f"✓ clean_data is called with 'sales_df' and stored in variable '{var_name}'")
                
                # Check if it's stored in clean_sales_df
                if var_name == 'clean_sales_df':
                    print("✓ Result is stored in the correct variable 'clean_sales_df'")
                else:
                    print(f"✗ WARNING: Result is stored in '{var_name}' instead of 'clean_sales_df'")
                    print("  SOLUTION: Use 'clean_sales_df = clean_data(sales_df)' in your main block")
            else:
                print("✗ ERROR: clean_data is not called correctly!")
                print("  SOLUTION: Add 'clean_sales_df = clean_data(sales_df)' to your main block")
                self.assertTrue(clean_data_pattern.search(main_block_content), 
                              "clean_data should be called with sales_df as argument")
            
            # Check for printing shapes
            print("\nChecking for code to print shapes before and after cleaning...")
            shape_pattern = re.compile(r"print\s*\(.*?shape.*?shape\)")
            if shape_pattern.search(main_block_content):
                print("✓ Code to print the shapes before and after cleaning is present")
            else:
                print("✗ ERROR: No code to print shapes before and after cleaning!")
                print("  SOLUTION: Add print statement comparing shapes before and after cleaning")
                self.assertTrue(shape_pattern.search(main_block_content), 
                              "Missing code to print shapes before and after cleaning")
        else:
            print("✗ ERROR: Could not parse main block content")
            self.fail("Could not parse main block content")
        
        print("\nTASK 2.2 COMPLETE! The clean_data function is correctly called in the main block.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
