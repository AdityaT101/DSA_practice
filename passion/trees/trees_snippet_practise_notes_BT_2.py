
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

# --=======================  L30. Print all the Nodes at a distance of K in Binary Tree   =======================

visited = set()
nodes_queue = deque()
parent_hmap = {}

def add_children_in_the_nodes_queue(root,index):
    left_element = root.left
    right_element = root.right

    if left_element is not None:
       nodes_queue.append([left_element,index] )
       parent_hmap[left_element] = root

    if right_element is not None:
       nodes_queue.append([right_element,index])
       parent_hmap[right_element] = root



def FindTargetRootNode( root, target):
    if root is None:
        return None

    if( root.data == target ) :
        return root

    left = FindTargetRootNode( root.left , target)
    if left : return left

    right = FindTargetRootNode( root.right, target)
    if right: return right


return_list_nodes = []


def PrintNodesAtDistanceK( root, dist, target):
    # reset globals
    visited.clear()
    nodes_queue.clear()
    parent_hmap.clear()
    return_list_nodes.clear()

    root1 = root
    nodes_queue.append([ root, 0])

    while(nodes_queue):
        root_node, index = nodes_queue.popleft()
        add_children_in_the_nodes_queue( root_node, index+1)

    root_parent = FindTargetRootNode( root1, target)
    visited.add(root_parent.data)

    level = 1
    nodes_queue.append([ root_parent, 0])

    while( nodes_queue and level <= dist):

        for _ in range(len(nodes_queue)):
            root, index = nodes_queue.popleft()

            left_element = root.left
            right_element = root.right
            parent_element = parent_hmap.get(root)

            index += 1
            if left_element is not None and left_element.data not in visited:
                visited.add(left_element.data)
                nodes_queue.append([ left_element, index])

            if right_element is not None and right_element.data not in visited:
                visited.add(right_element.data)
                nodes_queue.append([ right_element, index])

            if parent_element is not None and parent_element.data not in visited:
                visited.add(parent_element.data)
                nodes_queue.append([ parent_element, index])

        level += 1


    while( nodes_queue) :
        root, index = nodes_queue.popleft()
        return_list_nodes.append(root.data)

    return return_list_nodes

# --=======================  L34. Construct a Binary Tree from Preorder and Inorder Traversal  =======================
index_hmap = defaultdict()



def ConstructBTFromPreIn(inorder_list , preorder_list):
    if not preorder_list or not inorder_list:
        return None

    root = Node(preorder_list[0])
    separation_index = inorder_list.index( preorder_list[0] )

    inorder_list_left  = inorder_list [    :    separation_index]
    preorder_list_left = preorder_list[ 1 : 1 + separation_index]
    root.left = ConstructBTFromPreIn( inorder_list_left, preorder_list_left)

    inorder_list_right  = inorder_list [separation_index+1:]
    preorder_list_right = preorder_list[ 1 + separation_index : ]
    root.right = ConstructBTFromPreIn( inorder_list_right, preorder_list_right)

    return root


# --=======================  L35. Construct a Binary Tree from PostOrder and Inorder Traversal  =======================


def ConstructBTFromPrePost(inorder_list , postorder_list):
    if not postorder_list or not inorder_list:
        return None

    root = Node(postorder_list[-1])
    separation_index = inorder_list.index( postorder_list[-1] )

    inorder_list_left   = inorder_list  [   : separation_index]
    postorder_list_left = postorder_list[   : separation_index]
    root.left = ConstructBTFromPrePost( inorder_list_left, postorder_list_left)

    inorder_list_right  = inorder_list  [ separation_index+1 :   ]
    postorder_list_right= postorder_list[ separation_index   : -1]
    root.right = ConstructBTFromPrePost( inorder_list_right, postorder_list_right)

    return root


# --=============================

if __name__ == "__main__":
    # --=======================  L34. Construct a Binary Tree from Preorder and Inorder Traversal  =======================
    # inorder_list = [40, 3, 5, 4, 6, 2, 1, 7, 10, 9, 11, 111, 112, 113, 8]
    # preorder_list = [1, 2, 3, 40, 4, 5, 6, 7, 8, 9, 10, 11, 111, 112, 113]
    # inorder( ConstructBTFromPreIn( inorder_list, preorder_list) )

    # --=======================  L35. Construct a Binary Tree from PostOrder and Inorder Traversal  =======================
    # inorder_list = [ 40, 3, 5, 4, 6, 2, 1, 7, 10, 9, 11, 111, 112, 113, 8]
    # postorder_list =[ 40, 5, 6, 4, 3, 2, 10, 113, 112, 111, 11, 9, 8, 7, 1]
    # inorder(ConstructBTFromPrePost(inorder_list, postorder_list))


    # --=======================  L35. Construct a Binary Tree from PostOrder and Inorder Traversal  =======================
    # inorder_list = [ 40, 3, 5, 4, 6, 2, 1, 7, 10, 9, 11, 111, 112, 113, 8]
    # postorder_list =[ 40, 5, 6, 4, 3, 2, 10, 113, 112, 111, 11, 9, 8, 7, 1]
    # inorder(ConstructBTFromPrePost(inorder_list, postorder_list))

    # --=======================  L336. Serialize and De-serialize Binary Tree                       =======================
    serialized_list = deque([ 1, 2, 13, '#', '#', 4, 5, '#', '#', '#', '#'])
    tree_root = Node( serialized_list.popleft() )
    queue = deque([tree_root])

    while( queue):
        root = queue.popleft()

        if serialized_list:
            element_1 = serialized_list.popleft()
            if element_1 != '#':
               root.left = Node( element_1 )
               queue.append( root.left)
            else:
                root.left = None

        if serialized_list:
            element_2 = serialized_list.popleft()
            if element_2 != '#':
                root.right = Node(element_2)
                queue.append( root.right)
            else:
                root.right = None


    inorder( tree_root )




    # postorder_list =[ 40, 5, 6, 4, 3, 2, 10, 113, 112, 111, 11, 9, 8, 7, 1]
    # inorder(ConstructBTFromPrePost(inorder_list, postorder_list))



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

    # print( IsMirrorImage_using_preorder( root_sym.left, root_sym.right) )

    # --=======================  L26. Print Root to Node Path in Binary Tree                        =======================
    # print( PrintRootToNodeInBT( root1, 6) )
    # print( return_list_root_to_node )

    # --=======================  L27. Lowest Common Ancestor in Binary Tree                         =======================
    # print( LCAInBT( root1, 40, 6) )

    # --=======================  L30. Print all the Nodes at a distance of K in Binary Tree         =======================
    # print( PrintNodesAtDistanceK( root1, 2 , 2 ) )

    # --=======================  L31. Minimum time taken to BURN the Binary Tree from a Node        =======================
    # print(PrintNodesAtDistanceK(root1, 100, 2))







