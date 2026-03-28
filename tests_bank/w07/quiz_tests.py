"""Autograding tests — w07 (12 tasks)

Jawaban mahasiswa diambil dari:
  submissions/w07/answers.py
"""
from __future__ import annotations

import math
import re
import sys
from pathlib import Path

# Find repo root (folder that contains 'submissions/') robustly
_p = Path(__file__).resolve()
ROOT = None
for parent in [_p.parent] + list(_p.parents):
    if (parent / "submissions").exists():
        ROOT = parent
        break
if ROOT is None:
    ROOT = _p.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from submissions.w07 import answers as A

def _tf(x):
    if isinstance(x, bool):
        return x
    if isinstance(x, (int, float)):
        # 0 -> False, nonzero -> True
        return bool(x)
    if isinstance(x, str):
        s = x.strip().lower()
        if s in {'true','t','1','benar','ya','y','b'}:
            return True
        if s in {'false','f','0','salah','tidak','no','n','s'}:
            return False
    raise AssertionError(f'Expected True/False (bool). Got: {x!r}')

def _mc(x):
    if not isinstance(x, str):
        raise AssertionError(f'Expected pilihan ganda A/B/C/D (str). Got: {x!r}')
    s = x.strip().upper()
    # accept forms like 'b', 'B)', '(B)', 'Jawaban: B'
    m = re.search(r'[A-D]', s)
    if not m:
        raise AssertionError(f'Expected pilihan ganda A/B/C/D. Got: {x!r}')
    return m.group(0)

def _num(x):
    if isinstance(x, bool):
        raise AssertionError('Numeric answer must be int/float, not bool')
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        return float(x.strip().replace(',', '.'))
    # numpy scalars etc.
    try:
        import numpy as np
        if isinstance(x, np.generic):
            return float(x)
    except Exception:
        pass
    raise AssertionError(f'Numeric answer must be int/float. Got: {x!r}')

def test_q01():
    assert _tf(A.q01()) is True

def test_q02():
    assert _tf(A.q02()) is True

def test_q03():
    assert _tf(A.q03()) is True

def test_q04():
    assert _mc(A.q04()) == 'A'

def test_q05():
    assert _mc(A.q05()) == 'C'

def test_q06():
    assert _mc(A.q06()) == 'B'

def test_q07():
    assert _mc(A.q07()) == 'B'

def test_q08():
    assert math.isclose(_num(A.q08()), 0.5, rel_tol=0.0, abs_tol=0.0005)

def test_q09():
    assert math.isclose(_num(A.q09()), 0.01, rel_tol=0.0, abs_tol=0.0005)

def test_q10():
    assert math.isclose(_num(A.q10()), 1.96, rel_tol=0.0, abs_tol=0.0005)

def test_q11():
    assert _num(A.q11()) == 1.0

def test_q12():
    assert math.isclose(_num(A.q12()), 0.0013, rel_tol=0.0, abs_tol=0.0005)

