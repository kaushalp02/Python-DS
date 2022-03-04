class TreeNode:
    
    def __init__(self,data,parent,childList):
        self.data = data
        self.parent = parent
        self.childList = childList

    def addChild(self,childNode):
        self.childList.append(childNode)

    def countSpace(node):
        if node.parent == None:
            return 0
        else:
            return  node.parent.countSpace() + 1

    def __repr__(self):
        n = self.countSpace()
        return "\t"*n +"->"+self.data + "\n" + " ".join(str(x) for x in self.childList)
        

class Tree:

    def __init__(self,rootNode):
        self.rootNode = rootNode

    def addNode(self,data,parent):
        newNode = TreeNode(data,parent,[])
        parent.addChild(newNode)
        return newNode

    def __repr__(self):
        return str(self.rootNode)


if __name__ == "__main__":

    Root = TreeNode("Elecronics",None,[])
    Tree1 = Tree(Root)
    trimmer = Tree1.addNode("trimmer",Root)
    phone = Tree1.addNode("phone",Root)
    realme_trimmer = Tree1.addNode("Realme Trimmer",trimmer)


    print(Tree1)