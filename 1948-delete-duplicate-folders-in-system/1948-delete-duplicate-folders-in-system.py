class TreeNode:
    def __init__(self):
        self.children = dict()
        self.path = []
        self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        
        root = TreeNode()
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TreeNode()
                node = node.children[folder]
            node.path = path  
        
        serial_map = defaultdict(list)

        def serialize(node):
            if not node.children:
                return ""
            serials = []
            for name in sorted(node.children):
                child_serial = serialize(node.children[name])
                serials.append(f"{name}({child_serial})")
            serial = "".join(serials)
            serial_map[serial].append(node)
            return serial

        serialize(root)

        
        for nodes in serial_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        
        result = []

        def collect(node):
            for name, child in node.children.items():
                if not child.deleted:
                    result.append(child.path)
                    collect(child)

        collect(root)
        return result