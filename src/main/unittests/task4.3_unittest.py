# Unit Test for Task 4.3: Call Visualization Functions
import unittest
import os
import sys
import re

# Add the parent directory to path so we can import the module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..', 'python')
sys.path.append(parent_dir)

class TestCallVisualizationFunctions(unittest.TestCase):
    def test_call_visualization_functions(self):
        """Test that the main block properly calls the visualization functions"""
        print(f"\nCHECKING TASK 4.3: CALL VISUALIZATION FUNCTIONS")
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
        
        # Check for visualization function calls within main block
        main_block_pattern = re.compile(r"if\s+__name__\s*==\s*['\"]__main__['\"]\s*:(.*?)(?:\n\S|$)", re.DOTALL)
        main_block_match = main_block_pattern.search(content)
        
        if main_block_match:
            main_block_content = main_block_match.group(1)
            
            # Check for plot_category_sales call
            print("\nChecking for plot_category_sales function call...")
            plot_category_sales_pattern = re.compile(r"plot_category_sales\s*\(\s*category_sales\s*\)")
            if plot_category_sales_pattern.search(main_block_content):
                print("✓ plot_category_sales is called with the correct argument")
            else:
                print("✗ ERROR: plot_category_sales is not called correctly!")
                print("  SOLUTION: Add 'plot_category_sales(category_sales)' to your main block")
                self.assertTrue(plot_category_sales_pattern.search(main_block_content), 
                              "plot_category_sales should be called with category_sales as argument")
            
            # Check for plot_monthly_sales call
            print("\nChecking for plot_monthly_sales function call...")
            plot_monthly_sales_pattern = re.compile(r"plot_monthly_sales\s*\(\s*monthly\s*\)")
            if plot_monthly_sales_pattern.search(main_block_content):
                print("✓ plot_monthly_sales is called with the correct argument")
            else:
                print("✗ ERROR: plot_monthly_sales is not called correctly!")
                print("  SOLUTION: Add 'plot_monthly_sales(monthly)' to your main block")
                self.assertTrue(plot_monthly_sales_pattern.search(main_block_content), 
                              "plot_monthly_sales should be called with monthly as argument")
            
            # Check for confirmation message
            print("\nChecking for visualization confirmation message...")
            confirmation_pattern = re.compile(r"print\s*\(\s*['\"].*?visualization.*?saved.*?['\"]")
            if confirmation_pattern.search(main_block_content):
                print("✓ Confirmation message for saved visualizations is present")
            else:
                print("✗ ERROR: Visualization confirmation message is missing!")
                print("  SOLUTION: Add a print statement confirming visualizations were saved")
                self.assertTrue(confirmation_pattern.search(main_block_content),
                              "Missing confirmation message for saved visualizations")
        else:
            print("✗ ERROR: Could not parse main block content")
            self.fail("Could not parse main block content")
        
        print("\nTASK 4.3 COMPLETE! The visualization functions are correctly called in the main block.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
