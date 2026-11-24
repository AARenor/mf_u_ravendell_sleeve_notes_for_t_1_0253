"""Write the frog-trio sleeve notes for make.fun."""

import os
import sys
from pathlib import Path

TEXT = """After Rain
Three frogs play sax, bass and drums in the back of a closed florist's. The bassist stops a note with one webbed finger. In the buckets, the cut stems tremble."""

assert 1 <= len(TEXT) <= 280

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR", "/output")
Path(out_dir).mkdir(parents=True, exist_ok=True)
(Path(out_dir) / "entry.txt").write_bytes(TEXT.encode("utf-8"))
print(len(TEXT), file=sys.stderr)
