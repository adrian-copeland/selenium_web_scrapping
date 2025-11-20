import sys
from pathlib import Path

### add the src directory to sys.path
project_root = Path(__file__).resolve().parent.parent
src_path = project_root / "src"
sys.path.append(str(src_path))

from utils_etl import new_filename

if __name__ == "__main__":
    print(new_filename('new_file'))