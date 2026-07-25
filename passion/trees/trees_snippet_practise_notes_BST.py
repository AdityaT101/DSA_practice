
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

# --=======================  L40. Search in a Binary Search Tree =======================

def BTS( root, target):
    if root is None:
        return None

    if root.data < target:
        return BTS( root.right, target)

    elif root.data > target:
        return BTS( root.left, target)

    else:
        return root


# --=======================  L41. Ceil in a Binary Search Tree   =======================

def BTS_ceil( root, target , ceil):
    if root is None:
        return ceil

    if root.data < target:
        return BTS_ceil( root.right, target, ceil)

    if root.data >=  target:
        ceil = root.data
        return BTS_ceil( root.left, target , ceil)



# --=======================  L42. Floor in a Binary Search Tree  ======================

def BTS_Floor( root, target , floor):
    if root is None:
        return floor

    if root.data <= target:
        floor = root.data
        return BTS_Floor( root.right, target, floor)

    if root.data > target:
        return BTS_Floor( root.left, target , floor)


# --====================================================================================


if __name__ == "__main__":

    root = Node(11)
    root.left = Node(4)
    root.left.right = Node(6)
    root.left.right.left = Node(5)
    root.left.left = Node(2)
    root.left.left.left = Node(1)

    root.right = Node(18)
    root.right.left = Node(15)
    root.right.left.left = Node(13)
    root.right.left.right = Node(17)
    root.right.right = Node(21)
    root.right.right.left = Node(19)
    root.right.right.right = Node(25)

    #                         ( 11 )
    #                       ╱       ╲
    #                     4          18
    #                    ╱  ╲       ╱   ╲
    #                  2     6    15     21
    #                 ╱     ╱    ╱  ╲   ╱  ╲
    #                1     5   13   17 19   25

    # --=======================  L40. Search in a Binary Search Tree =======================

    # root = BTS( root , 25 )
    # print(root.data if root else "not found")

    # --=======================  L41. Ceil in a Binary Search Tree   =======================
    # ceil = BTS_ceil( root, 6, -1)
    # print( ceil )

    # --=======================  L42. Floor in a Binary Search Tree  ======================
    # floor = BTS_Floor( root, 17, 10000)
    # print(floor)