# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = {}
        def bfs(root: TreeNode, level: int):
            if not root:
                if level not in res:
                    res[level] = [None]
                else:
                    res[level].append(None)
                return
            if level not in res:
                res[level] = [root.val]
            else:
                res[level].append(root.val)
            bfs(root.left, level + 1)
            bfs(root.right, level + 1)

        bfs(root, 1)
        for k, v in list(res.items()):
            allNones = True
            for i in v:
                if i != None:
                    allNones = False
            if allNones:
                del res[k]
        answer = "["
        for k, v in res.items():
            for i in v:
                answer += str(i) + ","
                
        return answer[:len(answer) - 1] + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:len(data)-1]
        data = str.split(data, ",")
        for i in range(len(data)):
            if data[i] == "None":
                data[i] = None
            else: 
                data[i] = int(data[i])
        root = TreeNode(data[0])
        def buildTree(root, nodes):
            if not root:
                return
            root.left = 
        # buildTree(root, 2, data[1:])
        # res = []
        # number = ""
        # for i in range(len(data)):
        #     if i == len(data) - 1:
        #         res.append(int(data[i]))
        #     if data[i] == ",":
        #         if number == "None":
        #             res.append(None)
        #             number = ""
        #         else:
        #             res.append(int(number))
        #             number = ""
        #         continue
            
        #     number += data[i]
                

        

root = TreeNode(1)
root.left = TreeNode(2)
# root.left.left = TreeNode(9)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
codec.deserialize(codec.serialize(root))
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))