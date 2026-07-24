
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


# --=======================  # L8. Level Order Traversal in Binary Tree  =======================
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


# --=======================  # L20. Boundary Traversal in Binary Tree  =======================


return_list = []
right_boundary_stack = deque()


def is_leaf(node):
    return node.left is None and node.right is None

def left_boundary(root):
    if is_leaf(root):
        return
    return_list.append(root.data)
    if root.left is not None:
        left_boundary(root.left)
    elif root.right is not None:
        left_boundary(root.right)

def lower_boundary(root):
    if is_leaf(root):
        return_list.append(root.data)
    if root.left is not None:
        lower_boundary(root.left)
    if root.right is not None:
        lower_boundary(root.right)

def right_boundary(root):
    if is_leaf(root):
        return
    right_boundary_stack.append(root.data)
    if root.right is not None:
        right_boundary(root.right)
    elif root.left is not None:
        right_boundary(root.left)

def BoundaryTraversal(root):
    # add the elements from central node into return_list
    if not is_leaf(root):
        return_list.append(root.data)

    # 1. add elements from left boundary
    if root.left is not None:
        left_boundary(root.left)

    # 2. add elements from lower boundary ( leaf nodes )
    lower_boundary(root)

    # 3. add elements from right boundary
    if root.right is not None :
        right_boundary(root.right)
    while right_boundary_stack :
        return_list.append(right_boundary_stack.pop())

    print( return_list )

# --=======================  L21. Vertical Order Traversal of Binary Tree =======================
import heapq
vertical_order_heapq = []                        # flat heap of (col, row, val) tuples
vertical_order_queue = deque()
result_by_col_dict = defaultdict(list)

def VerticalOrderTraversal(root):
    # actual data, vertical_order , horizontal_level_order
    vertical_order_queue.append([ root, 0, 0])

    while( vertical_order_queue):
        root, vertical_order, horizontal_level_order = vertical_order_queue.popleft()
        heapq.heappush( vertical_order_heapq, (vertical_order, horizontal_level_order, root.data) )
        if root.left is not None:
            vertical_order_queue.append([root.left, vertical_order-1 , horizontal_level_order+1 ])
        if root.right is not None:
            vertical_order_queue.append([root.right, vertical_order+1, horizontal_level_order+1 ])

    while vertical_order_heapq:
        col, row, val = heapq.heappop(vertical_order_heapq)
        result_by_col_dict[col].append(val)

    return result_by_col_dict

# --=============================


def TopViewOfBinaryTree(root):
    result_by_col_dict = VerticalOrderTraversal(root)

    for key, value in result_by_col_dict.items():
        print( value[0] )


# --=============================

def BottomViewOfBinaryTree(root):
    result_by_col_dict = VerticalOrderTraversal(root)

    for key, value in result_by_col_dict.items():
        print( value[-1] )

# --=============================

left_view_queue = deque()
left_view_return_dict = defaultdict(list)

def LeftViewOfBinaryTree(root):
    left_view_queue.append([root, 0])

    while( left_view_queue ):
        root, index = left_view_queue.popleft()
        left_view_return_dict[index].append(root.data)
        if root.left is not None:
            left_view_queue.append([root.left, index+1])
        if root.right is not None:
            left_view_queue.append([root.right, index+1])

    for key, value in left_view_return_dict.items():
        print( value[0] )


# --=============================

def IsMirrorImage_using_preorder( root_1, root_2):
    if root_1 is None and root_2 is None:
        return True

    if (root_1 is None and root_2 is not None) or (root_1 is not None and root_2 is None):
        return False

    if root_1.data != root_2.data:
        return False

    flag_1 = IsMirrorImage_using_preorder( root_1.left, root_2.right)
    flag_2 = IsMirrorImage_using_preorder( root_1.right, root_2.left)

    return flag_1 and flag_2

# --=============================

return_list_root_to_node = []
def PrintRootToNodeInBT( root, target):
    if root is None:
        return False

    return_list_root_to_node.append(root.data)

    if root.data == target:
        return True

    # Both children are always evaluated. Once the left subtree finds the target, you should stop.
    if PrintRootToNodeInBT(root.left, target): return True
    if PrintRootToNodeInBT(root.right, target): return True

    return_list_root_to_node.pop() # dead end — undo
    return False


# --=============================


def LCAInBT( root, target1, target2):
    if root is None:
        return None

    if root.data in [target1, target2]:
        return root.data

    left_subtree_result  = LCAInBT( root.left, target1, target2)
    right_subtree_result = LCAInBT( root.right, target1, target2)

    if left_subtree_result == None and right_subtree_result != None:
         return right_subtree_result

    elif left_subtree_result != None and right_subtree_result == None:
         return left_subtree_result

    elif left_subtree_result != None and right_subtree_result != None:
         return root.data

    else:
         return None



# --=============================

if __name__ == "__main__":
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

    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(6)
    root.left.left.left = Node(11)
    root.left.left.left.left = Node(17)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(4)

    # --=======================  # L20. Boundary Traversal in Binary Tree  =======================

    root1 = Node(1)
    root1.left = Node(2)
    root1.left.left = Node(3)
    root1.left.left.right = Node(4)
    root1.left.left.left = Node(40)
    root1.left.left.right.left = Node(5)
    root1.left.left.right.right = Node(6)
    root1.right = Node(7)
    root1.right.right = Node(8)
    root1.right.right.left = Node(9)
    root1.right.right.left.left = Node(10)
    root1.right.right.left.right = Node(11)
    root1.right.right.left.right.right = Node(111)
    root1.right.right.left.right.right.right = Node(112)
    root1.right.right.left.right.right.right.right = Node(113)


    #                    (1)
    #                   ╱   ╲
    #                  2     7
    #                 ╱       ╲
    #                3         8
    #               ╱ ╲       ╱
    #             40   4     9
    #                 ╱ ╲   ╱ ╲
    #                5   6 10  11
    #                            ╲
    #                            111
    #                               ╲
    #                               112
    #                                  ╲
    #                                  113
    # BoundaryTraversal(root1)

    # --=======================  L21. Vertical Order Traversal of Binary Tree =======================
    # print( VerticalOrderTraversal(root1) )

    # --=======================  L22. Top View of Binary Tree                 =======================
    # TopViewOfBinaryTree(root1)

    # --=======================  L23. Bottom View of Binary Tree              =======================
    # BottomViewOfBinaryTree(root1)

    # --=======================  L24. Right/Left View of Binary Tree          =======================
    # LeftViewOfBinaryTree(root1)

    # --=======================  L25. Check for Symmetrical Binary Trees      =======================
    # root_sym = Node(1)
    # # left subtree
    # root_sym.left = Node(2)
    # root_sym.left.left = Node(3)
    # root_sym.left.right = Node(4)
    # root_sym.left.left.left = Node(7)
    # root_sym.left.left.right = Node(8)
    # # right subtree — mirror
    # root_sym.right = Node(2)
    # root_sym.right.left = Node(4)
    # root_sym.right.right = Node(3)
    # root_sym.right.right.left = Node(8)
    # root_sym.right.right.right = Node(7)
    #
    # print( IsMirrorImage_using_preorder( root_sym.left, root_sym.right) )

    # --=======================  L26. Print Root to Node Path in Binary Tree   =======================

    # print( PrintRootToNodeInBT( root1, 6) )
    # print( return_list_root_to_node )

    # --=======================  L27. Lowest Common Ancestor in Binary Tree   =======================
    print( LCAInBT( root1, 40, 6) )
