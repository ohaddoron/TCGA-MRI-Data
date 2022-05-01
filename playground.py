from pathlib import Path
from tqdm import tqdm

import fiftyone as fo
from loguru import logger

datasets = [fo.load_dataset(ds_name) for ds_name in tqdm(fo.list_datasets())]

merge_dataset = datasets[0].clone()

for dataset in datasets[1:]:
    merge_dataset.merge_samples(dataset)
    
pass