import sys
import os

# Add project root to sys.path so generated tests can import source modules.
# e.g. 'from src.notifications import ...' works when src/ lives at the repo root.
_project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)
