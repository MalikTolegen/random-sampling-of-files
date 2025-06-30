import os
import random
import shutil
from pathlib import Path

def sample_files():
    # Define the source and output directories
    base_dir = Path(__file__).parent
    output_dir = base_dir / 'sampled_output'
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    
    # Define sampling requirements
    sampling_requirements = {
        'Normal': 413,
        'raining': 100,
        'rainy but not raining': 325,
        'snowing': 100,
        'snowy but not snowing': 312,
        'unclear': 0,
        'Hazy': 0
    }
    
    # Process each category
    for category, num_samples in sampling_requirements.items():
        print(f"Processing {category}...")
        
        # Create category directory in output
        category_output_dir = output_dir / category
        category_output_dir.mkdir(exist_ok=True)
        
        # Get all directories in source directory
        source_dir = base_dir / category
        if not source_dir.exists():
            print(f"Warning: Source directory {category} not found!")
            continue
            
        # Get all directories (not files)
        dirs = [d for d in source_dir.glob('*') if d.is_dir()]
        if len(dirs) < num_samples:
            print(f"Warning: Not enough directories in {category} ({len(dirs)} found, {num_samples} needed)")
            continue
        
        # Randomly sample directories
        sampled_dirs = random.sample(dirs, num_samples)
        
        # Copy directories to output directory
        for dir in sampled_dirs:
            # Get the directory name without path
            dirname = dir.name
            # Create the destination path
            dest_path = category_output_dir / dirname
            # Copy the entire directory tree
            shutil.copytree(dir, dest_path)
        
        print(f"Copied {num_samples} files from {category} to {category_output_dir}")

if __name__ == "__main__":
    sample_files()
