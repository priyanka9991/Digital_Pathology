import pandas as pd
import numpy as np
import time
import sys
import os
import torch, torchvision
import torch.nn as nn
from torchvision import transforms
from PIL import Image
from torch.utils.data import Dataset
from ctran import ctranspath

from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler

start_time = time.time()
mean = (0.485, 0.456, 0.406)
std = (0.229, 0.224, 0.225)
trnsfrms_val = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=mean, std=std)
])

class roi_dataset(Dataset):
    def __init__(self, img_csv):
        super().__init__()
        self.transform = trnsfrms_val
        self.images_lst = img_csv

    def __len__(self):
        return len(self.images_lst)

    def __getitem__(self, idx):
        path = self.images_lst.filename[idx]
        label = self.images_lst.label[idx]  # Assuming you have a 'label' column in your CSV
        image = Image.open(path).convert('RGB')
        image = self.transform(image)
        return image, label

# instead of reading in 
filenames = sys.argv[1]
output = sys.argv[2]

if not os.path.exists(output):
    os.makedirs(output)


print(filenames)
img_csv=pd.read_csv(filenames, names = ['filename', 'label'], sep = ",")
test_datat = roi_dataset(img_csv)
database_loader = torch.utils.data.DataLoader(test_datat, batch_size=1, shuffle=False)

model = ctranspath()
model.head = nn.Identity()
td = torch.load(r'./ctranspath.pth')
model.load_state_dict(td['model'], strict=True)
model.eval()

embed_list = []
label_list = []  # To store corresponding labels
with torch.no_grad():
    for batch, labels in database_loader:
        features = model(batch)
        features = features.cpu().numpy()
        embed_list.append(features)
        label_list.append(labels.item())  # Assuming labels are scalar values

embeddings = np.vstack(embed_list)
labels = np.array(label_list)
labels = labels.reshape((labels.shape[0],1))

embeddings_with_labels = np.hstack((embeddings, labels))

print("--- %s minutes ---" % ((time.time() - start_time)/60))

#np.savetxt(str(output + f"\embeds_{os.path.basename(filenames)}"), embeddings_with_labels, delimiter=",")

output_path = os.path.join(output, f"embeds_{os.path.basename(filenames)}")
np.savetxt(output_path, embeddings_with_labels, delimiter=",")



