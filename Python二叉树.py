class Node(object):
    def __init__(self,elem = -1,lchild = None,rchild = None):
        '''节点类'''
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    '''树类'''
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self,elem):
        node = Node(elem)
        #如果树是空的,则对根节点赋值
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)
        else:
            #此节点的子树还没有齐
            treeNode = self.myQueue[0]
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                #如果该结点存在右子树,将此结点丢弃
                self.myQueue.pop(0)
    def front_digui(self,root):
        '''利用递归实现树的先序遍历'''
        if root == None:
            return
        print(root.elem)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def middle_digui(self,root):
        '''利用递归实现树的中序遍历'''
        if root == None:
            return
        self.middle_digui(root.lchild)
        print(root.elem)
        self.middle_digui(root.rchild)

    def later_digui(self,root):
        '''利用递归实现树的后序遍历'''
        if root == None :
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print(root.elem)


    def front_stack(self,root):
        '''利用堆栈实现树的先序遍历'''
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            #从根节点开始,一直找他的左子树
            while node:
                print(node.elem)
                myStack.append(node)
                node = node.lchild
            #while结束表示当前结点node为空,即前一个结点没有左子树了
            node = myStack.pop()
           #开始查看它的右子树
            node = node.rchild

    def middle_stack(self,root):
        '''利用堆栈实现树的中序遍历'''
        if root == None :
            return
        myStack = []
        node = root
        while node or myStack:
            #从根节点开始,一直找它的左子树
            while node:
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            #while结束表示当前结点node为空,即前一个结点没有子树了
            print(node.elem)
            #开始查看它的右子树
            node = node.rchild

    def later_stack(self,root):
        '''利用堆栈实现树的后序遍历'''
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        #这个while循环的功能是找出后序遍历的逆序,存在myStack2里面
        while myStack1:
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        #将myStack2中的元素出栈,即为后序遍历次序
        while myStack2:
            print(myStack2.pop().elem)


    def level_queue(self,root):
        '''利用队列实现树的层次遍历'''
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem)
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)


if __name__ == '__main__':
    '''主函数'''
    #生成十个数据作为树节点
    elems = range(10)
    #新建一个树对象
    tree = Tree()
    for elem in elems:
        #逐个添加树的结点
        tree.add(elem)

    print('队列实现层次遍历')
    tree.level_queue(tree.root)


    print('\n\n递归实现先序遍历:')
    tree.front_digui(tree.root)
    print ('\n递归实现中序遍历:' )
    tree.middle_digui(tree.root)
    print ('\n递归实现后序遍历:')
    tree.later_digui(tree.root)

    print ('\n\n堆栈实现先序遍历:')
    tree.front_stack(tree.root)
    print ('\n堆栈实现中序遍历:')
    tree.middle_stack(tree.root)
    print ('\n堆栈实现后序遍历:')
    tree.later_stack(tree.root)

