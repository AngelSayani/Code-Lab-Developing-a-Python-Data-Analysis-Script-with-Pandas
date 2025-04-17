# Import the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# Function to load the sales data
def load_data(filename):
    try:
        print(f"Attempting to load data from: {filename}")
        if not os.path.exists(filename):
            print(f"ERROR: The file {filename} does not exist!")
            return None
        df = pd.read_csv(filename)
        print(f"Successfully loaded data with {len(df)} rows and {len(df.columns)} columns")
        return df
    except Exception as e:
        print(f"ERROR loading data: {e}")
        return None

# Function to clean the data
def clean_data(df):
    try:
        if df is None:
            print("ERROR: Cannot clean a None DataFrame")
            return None
            
        # Record original shape for comparison
        original_shape = df.shape
        print(f"Original data shape before cleaning: {original_shape}")
        
        # Drop rows with missing values
        df_cleaned = df.dropna()
        print(f"After removing missing values: {df_cleaned.shape}")
        
        # Convert Date column to datetime
        df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'])
        print("Date column converted to datetime format")
        
        # Extract month from Date
        df_cleaned['Month'] = df_cleaned['Date'].dt.month_name()
        print("Added Month column extracted from Date")
        
        return df_cleaned
    except Exception as e:
        print(f"ERROR cleaning data: {e}")
        return None

# Function to calculate sales by category
def sales_by_category(df):
    try:
        if df is None:
            print("ERROR: Cannot analyze a None DataFrame")
            return None
            
        category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
        print(f"Analyzed sales for {len(category_sales)} categories")
        return category_sales
    except Exception as e:
        print(f"ERROR analyzing categories: {e}")
        return None

# Function to calculate monthly sales trends
def monthly_sales(df):
    try:
        if df is None:
            print("ERROR: Cannot analyze a None DataFrame")
            return None
            
        monthly = df.groupby('Month')['Sales'].sum()
        # Reorder months chronologically
        months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                       'July', 'August', 'September', 'October', 'November', 'December']
        monthly = monthly.reindex(months_order)
        print(f"Analyzed sales for {len(monthly)} months")
        return monthly
    except Exception as e:
        print(f"ERROR analyzing monthly trends: {e}")
        return None

# Function to plot sales by category
def plot_category_sales(category_sales):
    try:
        if category_sales is None or len(category_sales) == 0:
            print("ERROR: No category data to plot")
            return
            
        plt.figure(figsize=(10, 6))
        category_sales.plot(kind='bar', color='skyblue')
        plt.title('Sales by Product Category', fontsize=14)
        plt.xlabel('Category', fontsize=12)
        plt.ylabel('Total Sales ($)', fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save the figure with path debugging
        output_file = 'category_sales.png'
        print(f"Saving category plot to: {os.path.abspath(output_file)}")
        plt.savefig(output_file)
        plt.close()
        print("Category sales plot saved successfully")
    except Exception as e:
        print(f"ERROR plotting categories: {e}")

# Function to plot monthly sales trends
def plot_monthly_sales(monthly):
    try:
        if monthly is None or len(monthly) == 0:
            print("ERROR: No monthly data to plot")
            return
            
        plt.figure(figsize=(12, 6))
        monthly.plot(kind='line', marker='o', color='royalblue', linewidth=2)
        plt.title('Monthly Sales Trends', fontsize=14)
        plt.xlabel('Month', fontsize=12)
        plt.ylabel('Total Sales ($)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        # Save the figure with path debugging
        output_file = 'monthly_sales.png'
        print(f"Saving monthly plot to: {os.path.abspath(output_file)}")
        plt.savefig(output_file)
        plt.close()
        print("Monthly sales plot saved successfully")
    except Exception as e:
        print(f"ERROR plotting monthly trends: {e}")

# Function to identify top-selling products
def top_products(df):
    try:
        if df is None:
            print("ERROR: Cannot analyze a None DataFrame")
            return None
            
        top = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(5)
        return top.reset_index()
    except Exception as e:
        print(f"ERROR identifying top products: {e}")
        return None

# Function to calculate sales statistics
def sales_statistics(df):
    try:
        if df is None:
            print("ERROR: Cannot analyze a None DataFrame")
            return None
            
        stats = {
            'total_sales': df['Sales'].sum(),
            'average_sale': df['Sales'].mean(),
            'max_sale': df['Sales'].max(),
            'min_sale': df['Sales'].min(),
            'sale_std_dev': df['Sales'].std()
        }
        return stats
    except Exception as e:
        print(f"ERROR calculating statistics: {e}")
        return None

# Main execution block
if __name__ == "__main__":
    try:
        print("="*50)
        print("SALES ANALYSIS PROGRAM")
        print("="*50)
        
        # Determine file locations
        print("Checking file locations...")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"Script directory: {script_dir}")
        
        # Try multiple possible locations for the CSV file
        possible_paths = [
            "sales_data.csv",  # Same directory
            os.path.join(script_dir, "sales_data.csv"),  # Absolute path in same directory
            os.path.join(os.path.dirname(os.path.dirname(script_dir)), "resources", "sales_data.csv"),  # In resources folder
            os.path.join("E:", "workspace", "src", "resources", "sales_data.csv")  # Hardcoded path
        ]
        
        # Try each path until we find the file
        sales_df = None
        for path in possible_paths:
            print(f"Trying path: {path}")
            if os.path.exists(path):
                print(f"Found file at: {path}")
                sales_df = load_data(path)
                if sales_df is not None:
                    break
        
        # Check if we found and loaded the file
        if sales_df is None:
            print("ERROR: Could not find or load sales_data.csv. Please check the file location.")
            print("Tried the following paths:")
            for path in possible_paths:
                print(f"  - {path}")
            sys.exit(1)
            
        print("\nData loaded successfully. First 5 rows:")
        print(sales_df.head())
        
        # Clean the data
        clean_sales_df = clean_data(sales_df)
        if clean_sales_df is None:
            print("ERROR: Data cleaning failed, cannot continue analysis.")
            sys.exit(1)
            
        print(f"\nData cleaned successfully. Shape before cleaning: {sales_df.shape}")
        print(f"Shape after cleaning: {clean_sales_df.shape}")
        
        # Analyze sales by category
        category_sales = sales_by_category(clean_sales_df)
        if category_sales is not None:
            print("\nSales by Category:")
            print(category_sales)
        
        # Analyze monthly sales
        monthly = monthly_sales(clean_sales_df)
        if monthly is not None:
            print("\nMonthly Sales:")
            print(monthly)
        
        # Create visualizations
        print("\nCreating visualizations...")
        plot_category_sales(category_sales)
        plot_monthly_sales(monthly)
        
        # Advanced analysis
        top = top_products(clean_sales_df)
        if top is not None:
            print("\nTop 5 Products by Sales:")
            print(top)
        
        stats = sales_statistics(clean_sales_df)
        if stats is not None:
            print("\nSales Statistics:")
            for key, value in stats.items():
                print(f"{key.replace('_', ' ').title()}: ${value:.2f}")
        
        # Generate report
        try:
            print("\nGenerating sales analysis report...")
            report_path = "sales_report.txt"
            with open(report_path, 'w') as f:
                f.write("SALES ANALYSIS REPORT\n")
                f.write("=====================\n\n")
                
                if stats is not None:
                    f.write("Sales Statistics:\n")
                    for key, value in stats.items():
                        f.write(f"{key.replace('_', ' ').title()}: ${value:.2f}\n")
                
                if top is not None:
                    f.write("\nTop 5 Products by Sales:\n")
                    for i, row in top.iterrows():
                        f.write(f"{i+1}. {row['Product']}: ${row['Sales']:.2f}\n")
                
                if category_sales is not None:
                    f.write("\nTop 3 Categories by Sales:\n")
                    for i, (category, sales) in enumerate(category_sales.head(3).items()):
                        f.write(f"{i+1}. {category}: ${sales:.2f}\n")
                    
                f.write("\nNote: Visualizations have been saved as 'category_sales.png' and 'monthly_sales.png'.\n")
            
            print(f"Report generated as '{os.path.abspath(report_path)}'")
        except Exception as e:
            print(f"ERROR generating report: {e}")
        
        print("\nAnalysis complete!")
        
    except Exception as e:
        print(f"ERROR in main program: {e}")
        import traceback
        traceback.print_exc()
