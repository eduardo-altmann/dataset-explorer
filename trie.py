class TrieNode:
    def __init__(self):
        self.val = None
        self.next = {} 


class TrieST:
    def __init__(self):
        self.root = TrieNode()
    def get(self, key):
        x = self._get(self.root, key, 0)
        if x is None:
            return None
        return x.val

    def _get(self, node, key, d):
        if node is None:
            return None
        if d == len(key):
            return node
        c = key[d]
        if c not in node.next:
            return None
        return self._get(node.next[c], key, d + 1)

    def put(self, key, val):
        self.root = self._put(self.root, key, val, 0)

    def _put(self, node, key, val, d):
        if node is None:
            node = TrieNode()
        if d == len(key):
            if node.val is None:
                node.val = []
            
            if val not in node.val:
                node.val.append(val)
            return node

        c = key[d]
        if c not in node.next:
            node.next[c] = TrieNode()
        node.next[c] = self._put(node.next[c], key, val, d + 1)
        return node

    def keys_with_prefix(self, prefix):
        results = []
        node = self._get(self.root, prefix, 0)
        if node is None:
            return results
        self._collect(node, prefix, results)
        return results

    def _collect(self, node, prefix, results):
        if node is None:
            return
        if node.val is not None:
            results.append(prefix)
        for c in node.next:
            self._collect(node.next[c], prefix + c, results)

    def movie_ids_with_prefix(self, prefix):
        results = []
        node = self._get(self.root, prefix, 0)
        if node is None:
            return results
        self._collect_ids(node, results)
        return results

    def _collect_ids(self, node, results):
        if node is None:
            return
        if node.val is not None:
            # node.val é uma lista de movieId
            results.extend(node.val)
        for c in node.next:
            self._collect_ids(node.next[c], results)

