
#--=======================
#--=======================  L2. Binary Tree Representation in Python   =======================
#--=======================  L4. Binary Tree Traversals in Binary Tree  =======================
#
#             (1)
#           ╱    ╲
#          2      3
#         ╱ ╲    ╱
#        6   5  4
#       ╱
#     11
#     ╱
#   17
#

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data= key


# left -> center -> right
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=" → ")
    inorder(node.right)


# center -> left -> right
def PreOrder(root):
    if root is not None:
        print(root.data, end=" → ")
    else:
        return
    PreOrder(root.left)
    PreOrder(root.right)


# left -> right -> center
def PostOrder(root):
    if root is None:
       return
    PostOrder(root.left)
    PostOrder(root.right)
    print(root.data, end=" → ")


from collections import deque, defaultdict
queue = deque()


def add_children_in_the_queue(root,index):
    left_element = root.left
    right_element = root.right

    if left_element is not None:
       queue.append([left_element,index] )
    if right_element is not None:
       queue.append([right_element,index])


return_dict = defaultdict(list)
def LevelOrder(root):
    queue.append([root, 0])
    while(queue):
        root_node, index = queue.popleft()
        return_dict[index].append(root_node.data)
        index += 1
        add_children_in_the_queue( root_node, index )
    print( return_dict )


def MaxDepthOfBinaryTree(root):
    if root is None:
        return 0
    return 1 + max( MaxDepthOfBinaryTree(root.left), MaxDepthOfBinaryTree(root.right) )


def BalancedBinaryTree(root):
    if root is None:
        return 0
    left_subtree = BalancedBinaryTree(root.left)
    right_subtree = BalancedBinaryTree(root.right)
    if left_subtree == -1 or right_subtree ==-1 or abs(left_subtree-right_subtree) > 1 :
        return -1
    return 1 + max(left_subtree, right_subtree)


max_diameter_of_tree = 0
def DiameterOfBinaryTree(root):
    global max_diameter_of_tree
    if root is None:
        return 0
    left_subtree_height  = DiameterOfBinaryTree(root.left)
    right_subtree_height = DiameterOfBinaryTree(root.right)
    max_diameter_of_tree = max( max_diameter_of_tree , left_subtree_height + right_subtree_height )
    return 1 + max(left_subtree_height, right_subtree_height)



def IsSameTree_using_preorder(root_1, root_2):
     if root_1 is None and root_2 is None:
         return True

     if ( root_1 is None and root_2 is not None ) or ( root_1 is not None and root_2 is None ) :
         return False

     if root_1.data != root_2.data:
         return False

     flag_1 = IsSameTree_using_preorder( root_1.left, root_2.left)
     flag_2 = IsSameTree_using_preorder( root_1.right, root_2.right)

     return flag_1 and flag_2


traversal_root_1 = []
traversal_root_2 = []

def inorder_traversal(node, traversal_root):
    if node is None:
        return
    inorder_traversal( node.left, traversal_root )
    traversal_root.append( node.data )
    inorder_traversal( node.right, traversal_root)


return_dict_ZigZagOrder = defaultdict(list)
queue_for_zigzag = deque()

def add_children_in_the_queue_for_zigzag(root_node):
    left_element = root.left
    right_element = root.right

    if root_node.left is not None:
        queue_for_zigzag.append(root_node.left)
    if root_node.right is not None:
        queue_for_zigzag.append(root_node.right)



if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(6)
    root.left.left.left = Node(11)
    root.left.left.left.left = Node(17)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(4)

    # --=======================  L7. InOrder Traversal - DFS                =======================
    # inorder(root)    #   6 → 2 → 5 → 1 → 4 → 3

    # --=======================  L5. PreOrder Traversal - DFS               =======================
    # PreOrder(root)   #   1 → 2 → 6 → 5 → 3 → 4

    # --=======================  L6. PostOrder Traversal - DFS              =======================
    # PostOrder(root)  #   6 → 5 → 2 → 4 → 3 → 1

    # --=======================  L8. Level Traversal - BFS                  =======================
    # LevelOrder(root)   #  { 0: [1], 1: [2, 3], 2: [6, 5, 4], 3: [11] }

    # --=======================  MaxDepthOfBinaryTree                       =======================
    # print( MaxDepthOfBinaryTree(root) )

    #--=======================  L15. Check for Balanced Binary Tree         =======================
    # if BalancedBinaryTree(root) == -1:
    #     print("not balanced")
    # else:
    #     print("balanced")

    #--=======================  L16.Diameter of Binary Tree                 =======================
    # DiameterOfBinaryTree(root)
    # print( max_diameter_of_tree )

    #--=======================  L18.Check it two trees are Identical or Not =======================
    # root1 = Node(1)
    # root1.left = Node(2)
    # root1.left.left = Node(6)
    # root1.left.left.left = Node(11)
    # root1.left.left.left.left = Node(17)
    # root1.left.right = Node(5)
    # root1.right = Node(3)
    # root1.right.left = Node(4)
    # root1.right.right = Node(14)

    # method 1
    # print( sSameTree_using_preorder(root, root1) )

    # method 2
    # inorder_traversal(root, traversal_root_1)
    # inorder_traversal(root1,traversal_root_2)
    # if traversal_root_1 == traversal_root_2:
    #     print("Matching")
    # else:
    #     print("Not matching")

    # --=======================  L19.Zig - Zag or Spiral Traversal in Binary Tree=======================
    # ZigZagOrder(root)




