import subprocess
#subprocess.call(
# "xcopy \"ISIC_9999806.jpg\"
# \"C:/Users/seckin/PycharmProjects/untitled\"", shell=True, cwd=r'C:\Users\seckin\Downloads\melanoma\train')
import pandas as pd
import numpy as np
col_types = {"image_name": str,
            "patient_id": str,
            "sex": str,
            "age_approx": np.float16,
            "anatom_site_general_challenge": str,
            "diagnosis": str,
            "benign_malignant": str,
            "target": np.uint8}
df_1_train = pd.read_csv("<csv path for train class 1>", dtype=col_types)
df_1_train.reset_index(drop=True, inplace=True)
print(df_1_train.head(3))
i = 1
for index, row in df_1_train.iterrows():
    i = i + 1
#    if i == 31:
#        break
    image_name = row['image_name']
    subprocess.call("xcopy \""+image_name+".jpg\" \"<train class 1 files new location>\"", shell=True, cwd=r'<JPG train files path>')
#train 1 :30
#train 0: 970

