import collections

class TwoWatchedLiterals:
    """
    2-Watched Literals (2WL) Clause Indexing.
    Tracks 2 non-false literals per clause to avoid full clause traversals during BCP.
    """
    def __init__(self, clauses):
        self.clauses = clauses
        self.watches = collections.defaultdict(list)
        for c_idx, c in enumerate(clauses):
            if len(c) >= 2:
                self.watches[c[0]].append(c_idx)
                self.watches[c[1]].append(c_idx)
            elif len(c) == 1:
                self.watches[c[0]].append(c_idx)

    def on_literal_falsified(self, false_lit):
        affected = self.watches.get(false_lit, [])
        return len(affected)
