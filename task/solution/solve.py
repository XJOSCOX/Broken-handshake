import json
import os
import re
from collections import Counter
from pathlib import Path


app_dir = Path(os.environ.get("APP_DIR", "/app"))
access_log = app_dir / "access.log"
report_path = app_dir / "report.json"

paths, ips, total = Counter(), set(), 0
with access_log.open() as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += 1
        ips.add(line.split()[0])
        m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
        if m:
            paths[m.group(1)] += 1

top_count = max(paths.values())
top_path = sorted(path for path, count in paths.items() if count == top_count)[0]

with report_path.open("w") as out:
    json.dump(
        {
            "total_requests": total,
            "unique_clients": len(ips),
            "clients": sorted(ips),
            "path_counts": dict(sorted(paths.items())),
            "top_path": top_path,
        },
        out,
        indent=2,
        sort_keys=True,
    )
print(f"wrote {report_path}")
