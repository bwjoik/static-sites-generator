import os
import shutil

def copytree(static_dir, public_dir):
    for root, dirs, files in os.walk(static_dir):
        # 計算對應的 public 目錄
        rel_path = os.path.relpath(root, static_dir)
        dest_dir = os.path.join(public_dir, rel_path) if rel_path != "." else public_dir
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)
            print(f"copying {src_file} to {dest_file}")
            shutil.copyfile(src_file, dest_file)