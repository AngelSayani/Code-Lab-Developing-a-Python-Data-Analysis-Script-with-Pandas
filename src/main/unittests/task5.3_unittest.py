# Unit Test for Task 5.3: Generate Report
import unittest
import os
import sys
import re

# Add the parent directory to path so we can import the module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..', 'python')
sys.path.append(parent_dir)

class TestGenerateReport(unittest.TestCase):
    def setUp(self):
        # Clean up any existing report file
        self.report_path = 'sales_report.txt'
        if os.path.exists(self.report_path):
            try:
                os.remove(self.report_path)
            except (PermissionError, FileNotFoundError):
                pass
    
    def tearDown(self):
        # Clean up created file
        if os.path.exists(self.report_path):
            try:
                os.remove(self.report_path)
            except (PermissionError, FileNotFoundError):
                pass
    
    def test_generate_report(self):
        """Test that the main block properly generates a report"""
        print(f"\nCHECKING TASK 5.3: GENERATE REPORT")
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
        
        # Check for report generation code within main block
        main_block_pattern = re.compile(r"if\s+__name__\s*==\s*['\"]__main__['\"]\s*:(.*?)(?:\n\S|$)", re.DOTALL)
        main_block_match = main_block_pattern.search(content)
        
        if main_block_match:
            main_block_content = main_block_match.group(1)
            
            # Check for file writing
            print("\nChecking for file writing code...")
            if "open('sales_report.txt', 'w')" in main_block_content or "open(\"sales_report.txt\", \"w\")" in main_block_content:
                print("✓ Code to open sales_report.txt for writing is present")
            else:
                print("✗ ERROR: No code to create sales_report.txt!")
                print("  SOLUTION: Add 'with open(\"sales_report.txt\", \"w\") as f:' to your main block")
                self.assertTrue("open('sales_report.txt', 'w')" in main_block_content or "open(\"sales_report.txt\", \"w\")" in main_block_content, 
                              "Missing code to create sales_report.txt")
            
            # Check for writing statistics
            print("\nChecking for code to write statistics...")
            stats_pattern = re.compile(r"f\.write.*?sales.*?statistics", re.IGNORECASE)
            if stats_pattern.search(main_block_content):
                print("✓ Code to write sales statistics is present")
            else:
                print("✗ ERROR: No code to write sales statistics to the report!")
                print("  SOLUTION: Add code to write sales statistics to the report")
                self.assertTrue(stats_pattern.search(main_block_content), 
                              "Missing code to write sales statistics")
            
            # Check for writing top products
            print("\nChecking for code to write top products...")
            products_pattern = re.compile(r"f\.write.*?products", re.IGNORECASE)
            if products_pattern.search(main_block_content):
                print("✓ Code to write top products is present")
            else:
                print("✗ ERROR: No code to write top products to the report!")
                print("  SOLUTION: Add code to write top products to the report")
                self.assertTrue(products_pattern.search(main_block_content), 
                              "Missing code to write top products")
            
            # Check for writing top categories
            print("\nChecking for code to write top categories...")
            categories_pattern = re.compile(r"f\.write.*?categor", re.IGNORECASE)
            if categories_pattern.search(main_block_content):
                print("✓ Code to write top categories is present")
            else:
                print("✗ ERROR: No code to write top categories to the report!")
                print("  SOLUTION: Add code to write top categories to the report")
                self.assertTrue(categories_pattern.search(main_block_content), 
                              "Missing code to write top categories")
            
            # Check for confirmation message
            print("\nChecking for report confirmation message...")
            confirmation_pattern = re.compile(r"print\s*\(\s*['\"].*?report.*?['\"]")
            if confirmation_pattern.search(main_block_content):
                print("✓ Confirmation message for report generation is present")
            else:
                print("✗ ERROR: Report confirmation message is missing!")
                print("  SOLUTION: Add a print statement confirming report generation")
                self.assertTrue(confirmation_pattern.search(main_block_content),
                              "Missing confirmation message for report generation")
        else:
            print("✗ ERROR: Could not parse main block content")
            self.fail("Could not parse main block content")
        
        print("\nTASK 5.3 COMPLETE! The report generation code is correctly implemented.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
