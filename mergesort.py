"""Merge sort code"""

# David Barnes, Robert Depweg
# CIS 226
# 10-25-2024

class MergeSort:
    """Merge sort class"""

    def __init__(self):
        """Constructor"""
        self._aux = []

    def sort(self, iter):
        """Main entry point to sort"""
        self._aux = [None for i in range(len(iter))]
        self._sort(iter, 0, len(iter) - 1)

    def _sort(self, iter, lo, hi):
        """mergesort a[lo..hi] using auxiliary array aux[lo..hi]"""
        if hi <= lo:
            return
        mid = lo + int((hi - lo) / 2)
        self._sort(iter, lo, mid)
        self._sort(iter, mid + 1, hi)
        self._merge(iter, lo, mid, hi)

    def _merge(self, mergeable, lo, mid, hi):
        """Merge iter[lo .. mid] with iter[mid+1 .. hi] using aux[lo .. hi]"""
        # Copy to aux[]
        for k in range(lo, hi + 1):
            self._aux[k] = mergeable[k]

        # Merge back to mergeable[]
        i = lo
        j = mid + 1
        for k in range(lo, hi + 1):
            if i > mid: # Index past left subarray max index
                mergeable[k] = self._aux[j]
                j += 1
            elif j > hi: # index past right subarray max index
                mergeable[k] = self._aux[i]
                i += 1
            elif self._aux[j].__lt__(self._aux[i]): # compare lesser than
                mergeable[k] = self._aux[j]
                j += 1
            # elif self._aux[j].__gt__(self._aux[i]): # compare greater than
            #     mergeable[k] = self._aux[j]
            #     j += 1
            else:
                mergeable[k] = self._aux[i]
                i += 1
        return