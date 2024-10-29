"""Merge sort code"""

# Robert Depweg
# CIS 226
# 10-25-2024


class MergeSort:
    """Merge sort class"""

    def _merge(self, mergeable, lo, mid, hi):

        mid = lo + int((hi - lo) / 2)

        _aux = []
        # Copy to aux[]
        for k in range(lo, hi + 1):
            _aux[k] = mergeable[k]

        # Merge back to mergeable[]
        i = lo
        j = mid + 1
        for k in range(lo, hi + 1):
            if i > mid:  # Index past left subarray max index
                mergeable[k] = _aux[j]
                j += 1
            elif j > hi:  # index past right subarray max index
                mergeable[k] = _aux[i]
                i += 1
            elif _aux[j] < _aux[i]:  # compare
                mergeable[k] = _aux[j]
                j += 1
            else:
                mergeable[k] = _aux[i]
                i += 1
        return

    # Constructor
    def __init__(self):
        self._aux = []

        # Main entry point to sort

    def sort(self, iter):
        self._aux = [None for i in range(len(iter))]
        self._sort(iter, 0, len(iter) - 1)

        # mergesort a[lo..hi] using auxiliary array aux[lo..hi]

    def _sort(self, iter, lo, hi):
        if hi <= lo:
            return
        mid = lo + int((hi - lo) / 2)
        self._sort(iter, lo, mid)
        self._sort(iter, mid + 1, hi)
        self._merge(iter, lo, mid, hi)
