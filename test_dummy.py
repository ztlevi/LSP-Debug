# Method 2
# python3 -m pytest test_dummy.py

import pytest
import debugpy
debugpy.listen(("0.0.0.0", 5678))
debugpy.wait_for_client()


@pytest.mark.parametrize("i", (1, 2, 3))
def test_dummy(i):
    print()
    print(i)
    a = 2
