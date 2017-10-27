class Node:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

    def traverse(self, outer=None, inner=None):
        if inner is None:
            inner = []
        if outer is None:
            outer = []
   
        if not self.left and not self.right:
            inner.append(self.value)
            outer.append(inner)
            return
        else:
            inner.append(self.value)
            return self.left.traverse(outer=outer, inner=inner)
            return self.right.traverse(outer=outer, inner=inner) 
        
        return outer
