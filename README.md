# digpath_msi_prediction

### Steps for getting patch embeddings
1. get_filenames.sh - Generate.csv files for each WSI containing file names of all the patches from the WSI. These .csv files are stored in the same directory.
    - Set TOP_LEVEL_DIR to the directory containing the slide-specific subdirectories
    - run with `./get_filenames.sh <label>` replacing "label" with 0 or 1 (usually MSS=0, MSI=1)

3. get_features_CTransPath.py and get_all_features.py
   - Download the trained ctranspath model from https://drive.google.com/file/d/1DoDx_70_TLj98gTf6YTXnu4tFhsFocDX/view?usp=sharing
   - Fill in line 57 with your path to ctranspath.pth
   - Run with `python get_features_CTransPath.py <filenames.csv> <path to the output directory>` replacing filenames.csv with the output csv of get_filenames.sh
   - To run feature extraction for all slides' csv files, run python get_all_features.py <path to the folder containing the CSV files>` <path to the output directory>`
   - The output of this script will be .csv files with the extracted features

4. make_h5.py - To convert .csv feature files to .h5
   - Set `directory` to the path to the directory containing the embedding CSVs
   - Set `out_directory` to the desired output directory for the h5 files
   - Set `output_csv` to the desired output file for the slide.csv file (an input to HistoBistro)
   - This script produces the .h5 files as well as a .csv file to summarize the feature file names. Both are required for HistoBistro.
