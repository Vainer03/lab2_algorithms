'''
def build_init_tree(self):
    if self.left_i == self.right_i:
        self.left = None
        self.right = None
    else:
        self.left(Node(), Node(), 0, self.left_i, self.right_i//2)
        self.left.build_init_tree()
        self.right(Node(), Node(), 0, self.right_i//2, self.right_i)
        self.right.build_init_tree()
'''

'''
def build_init_tree_1(head):
    print("head.left_i = ", head.left_i, "head.right_i = ", head.right_i)
    if head.left_i == head.right_i:
        print("Entering if statement")
        head.left = None
        head.right = None
        return 1
    elif head.right is not None:
        print("Going right")
        head.right = Node(Node(), Node(), 0, (head.right_i - head.left_i + 1) // 2, head.right_i)
        return build_init_tree_1(head.right)
    elif head.left is not None:
        print("Going left")
        head.left = Node(Node(), Node(), 0, head.left_i, head.right_i//2)
        return build_init_tree_1(head.left)
    else:
        return 0
'''

'''
    depth_x = 0
    while len(x_compressed) > pow(2, depth_x):
        depth_x += 1
    
    root_x = Node(Node(), Node(), 0, 1, 2 ** depth_x)
    build_init_tree_1(root_x)
    
    
    depth_y = 0
    while len(y_compressed) > pow(2, depth_y):
        depth_y += 1
    
    root_y = Node(Node(), Node(), 0, 1, 2 ** depth_y)
    build_init_tree_1(root_y)
'''

# for i in range(len(tree.tree)):
#     print(i, ": left index - ", tree.tree[i].left_i, " right index - ", tree.tree[i].right_i, " modifier - ", tree.tree[i].modifier)