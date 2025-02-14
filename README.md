# digpath_msi_prediction

### Steps for getting patch embeddings
1. get_filenames.sh
    - Set TOP_LEVEL_DIR to the directory containing the slide-specific subdirectories
    - run with `./get_filenames.sh <label>` replacing "label" with 0 or 1 (usually MSS=0, MSI=1)

3. get_features_CTransPath.py and get_all_features.py
   - Fill in line 57 with your path to ctranspath.pth
   - Run with `python get_features_CTransPath.py <filenames.csv>` replacing filenames.csv with the output csv of get_filenames.sh
   - To run feature extraction for all slides' csv files, run python get_all_features.py

4. make_h5.py
   - Set `directory` to the path to the directory containing the embedding CSVs
   - Set `out_directory` to the desired output directory for the h5 files
   - Set `output_csv` to the desired output file for the slide.csv file (an input to HistoBistro)
