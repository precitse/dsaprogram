# ---------------- Binary Search Tree (BST) ----------------

# Node class represents a single node in the BST
class Node:
    def __init__(self, key):
        self.key = key        # Node value
        self.left = None      # Left child
        self.right = None     # Right child


# Binary Search Tree class
class BST:
    def __init__(self):
        self.root = None

    # ---------------- INSERT NODE ----------------
    def insert(self, root, key):
        """Insert a node into the BST (ignores duplicates)."""
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            print(f"Duplicate entry {key} ignored.")
        return root

    # ---------------- SEARCH NODE ----------------
    def search(self, root, key):
        """Search for a key in the BST."""
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    # ---------------- FIND MINIMUM NODE ----------------
    def minValueNode(self, node):
        """Find the node with the smallest key (used in deletion)."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    # ---------------- DELETE NODE ----------------
    def delete(self, root, key):
        """Delete a node from the BST."""
        if root is None:
            return root

        # Traverse left or right to find the node
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Case 1: Node has no left child
            if root.left is None:
                return root.right
            # Case 2: Node has no right child
            elif root.right is None:
                return root.left
            # Case 3: Node has two children
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    # ---------------- TREE TRAVERSALS ----------------
    def inorder(self, root):
        """Inorder traversal (LNR)."""
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        """Preorder traversal (NLR)."""
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        """Postorder traversal (LRN)."""
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    # ---------------- DEPTH OF TREE ----------------
    def depth(self, root):
        """Calculate depth (height) of BST."""
        if root is None:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

    # ---------------- MIRROR IMAGE ----------------
    def mirror(self, root):
        """Convert tree into its mirror image."""
        if root:
            root.left, root.right = root.right, root.left
            self.mirror(root.left)
            self.mirror(root.right)

    # ---------------- COPY TREE ----------------
    def copy(self, root):
        """Create a deep copy of the tree."""
        if root is None:
            return None
        new_node = Node(root.key)
        new_node.left = self.copy(root.left)
        new_node.right = self.copy(root.right)
        return new_node

    # ---------------- DISPLAY PARENTS WITH CHILDREN ----------------
    def display_parents(self, root):
        """Display each parent node with its children."""
        if root:
            if root.left or root.right:
                print(f"Parent {root.key}: ", end="")
                if root.left:
                    print(f"Left Child = {root.left.key}", end=" ")
                if root.right:
                    print(f"Right Child = {root.right.key}", end=" ")
                print()
            self.display_parents(root.left)
            self.display_parents(root.right)

    # ---------------- DISPLAY LEAF NODES ----------------
    def display_leaves(self, root):
        """Display all leaf nodes (nodes with no children)."""
        if root:
            if root.left is None and root.right is None:
                print(root.key, end=" ")
            self.display_leaves(root.left)
            self.display_leaves(root.right)

    # ---------------- LEVEL ORDER TRAVERSAL ----------------
    def level_order(self, root):
        """Print nodes level by level (Breadth-First Traversal)."""
        if root is None:
            return
        queue = [root]
        while queue:
            current = queue.pop(0)
            print(current.key, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    tree = BST()
    root = None

    while True:
        print("\n--- Binary Search Tree Menu ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Display (Inorder, Preorder, Postorder)")
        print("5. Display Depth of Tree")
        print("6. Display Mirror Image")
        print("7. Create Copy of Tree")
        print("8. Display Parents with Children")
        print("9. Display Leaf Nodes")
        print("10. Display Level-wise")
        print("11. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            val = int(input("Enter value: "))
            root = tree.insert(root, val)

        elif choice == 2:
            val = int(input("Enter value to delete: "))
            root = tree.delete(root, val)

        elif choice == 3:
            val = int(input("Enter value to search: "))
            res = tree.search(root, val)
            if res:
                print(f"Found {val} in tree.")
            else:
                print(f"{val} not found.")

        elif choice == 4:
            print("Inorder: ", end=""); tree.inorder(root); print()
            print("Preorder: ", end=""); tree.preorder(root); print()
            print("Postorder: ", end=""); tree.postorder(root); print()

        elif choice == 5:
            print("Depth of tree:", tree.depth(root))

        elif choice == 6:
            print("Mirror Image created.")
            tree.mirror(root)
            tree.inorder(root); print()

        elif choice == 7:
            copy_root = tree.copy(root)
            print("Copied Tree (Inorder): ", end="")
            tree.inorder(copy_root); print()

        elif choice == 8:
            print("Parents with their children:")
            tree.display_parents(root)

        elif choice == 9:
            print("Leaf nodes: ", end="")
            tree.display_leaves(root); print()

        elif choice == 10:
            print("Level order: ", end="")
            tree.level_order(root); print()

        elif choice == 11:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")
