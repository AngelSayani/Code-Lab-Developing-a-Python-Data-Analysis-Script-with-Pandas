# Unit Test for Task 3.3: Call Analysis Functions
import unittest
import os
import sys
import re

# Add the parent directory to path so we can import the module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..', 'python')
sys.path.append(parent_dir)

class TestCallAnalysisFunctions(unittest.TestCase):
    def test_call_analysis_functions(self):
        """Test that the main block properly calls the analysis functions"""
        print(f"\nCHECKING TASK 3.3: CALL ANALYSIS FUNCTIONS")
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
        
        # Check for analysis function calls within main block
        main_block_pattern = re.compile(r"if\s+__name__\s*==\s*['\"]__main__['\"]\s*:(.*?)(?:\n\S|$)", re.DOTALL)
        main_block_match = main_block_pattern.search(content)
        
        if main_block_match:
            main_block_content = main_block_match.group(1)
            
            # Check for sales_by_category call
            print("\nChecking for sales_by_category function call...")
            sales_by_category_pattern = re.compile(r"(\w+)\s*=\s*sales_by_category\s*\(\s*clean_sales_df\s*\)")
            sales_by_category_match = sales_by_category_pattern.search(main_block_content)
            
            if sales_by_category_match:
                var_name = sales_by_category_match.group(1)
                print(f"✓ sales_by_category is called with 'clean_sales_df' and stored in variable '{var_name}'")
                
                # Check if it's stored in category_sales
                if var_name == 'category_sales':
                    print("✓ Result is stored in the correct variable 'category_sales'")
                else:
                    print(f"✗ WARNING: Result is stored in '{var_name}' instead of 'category_sales'")
                    print("  SOLUTION: Use 'category_sales = sales_by_category(clean_sales_df)' in your main block")
            else:
                print("✗ ERROR: sales_by_category is not called correctly!")
                print("  SOLUTION: Add 'category_sales = sales_by_category(clean_sales_df)' to your main block")
                self.assertTrue(sales_by_category_pattern.search(main_block_content), 
                              "sales_by_category should be called with clean_sales_df as argument")
            
            # Check for monthly_sales call
            print("\nChecking for monthly_sales function call...")
            monthly_sales_pattern = re.compile(r"(\w+)\s*=\s*monthly_sales\s*\(\s*clean_sales_df\s*\)")
            monthly_sales_match = monthly_sales_pattern.search(main_block_content)
            
            if monthly_sales_match:
                var_name = monthly_sales_match.group(1)
                print(f"✓ monthly_sales is called with 'clean_sales_df' and stored in variable '{var_name}'")
                
                # Check if it's stored in monthly
                if var_name == 'monthly':
                    print("✓ Result is stored in the correct variable 'monthly'")
                else:
                    print(f"✗ WARNING: Result is stored in '{var_name}' instead of 'monthly'")
                    print("  SOLUTION: Use 'monthly = monthly_sales(clean_sales_df)' in your main block")
            else:
                print("✗ ERROR: monthly_sales is not called correctly!")
                print("  SOLUTION: Add 'monthly = monthly_sales(clean_sales_df)' to your main block")
                self.assertTrue(monthly_sales_pattern.search(main_block_content), 
                              "monthly_sales should be called with clean_sales_df as argument")
            
            # Check for printing results
            print("\nChecking for code to print analysis results...")
            print_category_pattern = re.compile(r"print\s*\(\s*.*?category.*?\s*\)")
            print_monthly_pattern = re.compile(r"print\s*\(\s*.*?monthly.*?\s*\)")
            
            if print_category_pattern.search(main_block_content):
                print("✓ Code to print category sales results is present")
            else:
                print("✗ ERROR: No code to print category sales results!")
                print("  SOLUTION: Add print statement for category sales results")
                self.assertTrue(print_category_pattern.search(main_block_content), 
                              "Missing code to print category sales results")
            
            if print_monthly_pattern.search(main_block_content):
                print("✓ Code to print monthly sales results is present")
            else:
                print("✗ ERROR: No code to print monthly sales results!")
                print("  SOLUTION: Add print statement for monthly sales results")
                self.assertTrue(print_monthly_pattern.search(main_block_content), 
                              "Missing code to print monthly sales results")
        else:
            print("✗ ERROR: Could not parse main block content")
            self.fail("Could not parse main block content")
        
        print("\nTASK 3.3 COMPLETE! The analysis functions are correctly called in the main block.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
