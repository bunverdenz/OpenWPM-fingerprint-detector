import os
import sys
from demo import run_demo

if __name__ == '__main__':

    if len((sys.argv)) > 1:
        url = sys.argv[1]

        run_demo(url)
        str_run = "feature_extraction/extract_feature.py"
        os.system(str_run)
    else:
        print("Please input url")

