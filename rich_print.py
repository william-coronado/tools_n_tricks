from rich import print
from rich.table import Table
from rich.progress import track
import time
# Create a fancy table
table = Table(title="Project Statistics")
table.add_column("Module", style="cyan")
table.add_column("Coverage", style="magenta")
table.add_column("Status", style="green")
table.add_row("Core", "87%", "✅")
table.add_row("API", "92%", "✅")
table.add_row("UI", "76%", "⚠️")
print(table)
# Add a progress bar
for step in track(range(100), description="Processing..."):
    time.sleep(0.01)