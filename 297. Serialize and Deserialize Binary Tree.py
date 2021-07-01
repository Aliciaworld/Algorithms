
import collections
class Codec:
    def serialize(self, root):
        """Encode a tree to a single string
        : type root: TreeNode
        : rtype:str
        """
        res = []

        def pre_order(node):
            if not node:
                return res.append('None')
            res.append(str(node.val))
            pre_order(node.left)
            pre_order(node.right)

        pre_order(root)
        return ','.join(res)

    def deserialize(self, data):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype:str
        www."""
        data_list = data.split(',')
        queue = collections.deque(data_list)

        def helper(queue):
            node = queue.popleft()
            if node == 'None':
                return
            root = TreeNode(node)
            root.left = helper(queue)
            root.right = helper(queue)
            return root

        return helper(queue)

