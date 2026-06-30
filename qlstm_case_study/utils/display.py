import base64
from pathlib import Path
from IPython.display import IFrame, display


def show_map(map_name, width=900, height=600):
    """Load a pre-generated map from the maps/ directory and display it."""
    map_path = Path.cwd() / "maps" / map_name
    with open(map_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    display(IFrame(src=f"data:text/html;base64,{b64}", width=width, height=height))