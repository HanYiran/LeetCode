class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        """item存放数据元素"""
        self.item = item
        #next 是下一个节点的标识
        self.next = None

    def is_empty(self):
        # 链表是否为空
    def length(self):
        #链表长度
    def travel(self):
        # 遍历整个链表
    def add(self,item):
        # 链表头部添加元素
    def append(self,item):
        # 链表尾部添加元素
    def insert(self,pos, item):
        # 指定位置添加元素
    def remove(self,item):
        # 删除节点
    def search(self,item):
        # 查找节点是否存在