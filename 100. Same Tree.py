# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while len(stack):
            print('len of stack')
            print(len(stack))
            print(stack)
            first, second = stack.pop()
            print(first)
            print('')
            print(second)
            # asking is that if both are none then skip 
            if not first and not second:
                print('nulls?')
                continue
            elif None in [first, second]:
                return False
            else:
                print('')
                if first.val != second.val:
                    return False
                print('val')
                print(first.left)
                print(first.right)
                print('')
                stack.append((first.left, second.left))
                stack.append((first.right, second.right))
        return True