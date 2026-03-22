"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        mapping = {}
        curr = head
        while curr:
            new_node = Node(curr.val)
            mapping[curr] = new_node
            curr = curr.next
        
        curr = head
        while curr:
            new_node = mapping[curr]
            new_node.next = mapping.get(curr.next, None)
            new_node.random = mapping.get(curr.random, None)
            curr = curr.next
        return mapping.get(head, None)