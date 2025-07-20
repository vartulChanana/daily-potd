from typing import List, Dict
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.name = ""
        self.del_flag = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                    node.children[folder].name = folder
                node = node.children[folder]

        serial_map = defaultdict(list)

        def serialize(node):
            if not node.children:
                return ""
            serial = []
            for child_name in sorted(node.children.keys()):
                child = node.children[child_name]
                sub_serial = serialize(child)
                serial.append(f"{child_name}({sub_serial})")
            serial_str = "".join(serial)
            serial_map[serial_str].append(node)
            return serial_str

        serialize(root)

        for nodes in serial_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.del_flag = True

        result = []

        def dfs(node, path):
            for name, child in node.children.items():
                if child.del_flag:
                    continue
                result.append(path + [name])
                dfs(child, path + [name])

        dfs(root, [])
        return result
