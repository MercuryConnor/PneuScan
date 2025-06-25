import os
import shutil

src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'best_pneumonia_model.h5'))
dst = os.path.abspath(os.path.join(os.path.dirname(__file__), 'best_pneumonia_model.h5'))

if not os.path.exists(dst):
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Model file copied to {dst}")
    else:
        print(f"Source model file not found at {src}")
else:
    print(f"Model file already exists at {dst}")
