import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('space_id', type=str)
args = parser.parse_args()
SPACEID = args.space_id or os.environ['SPACE_ID']
print(SPACEID)
