from logging import root


class Vertex (object):
    def __init__(self, name):
        self.name = name;
        self.node = None;

class Node (object):
    def __init__(self, height, nodeId, parentId):
        self.height = height;
        self.nodeId = nodeId;
        self.parentId = parentId;

class Edge (object):
    def __init__(self, startVertex, targetVertex, weight):
        self.startVertex = startVertex;
        self.targetVertex = targetVertex;
        self.weight = weight;
    
    def __cmp__(self, otherEdge):
        return self.cmp(self.weight, otherEdge.weight);

    def __lt__(self, other):
        selfPriority = self.weight;
        otherPriority = other.weight;
        return selfPriority < otherPriority;

class DisjoinSet(object):
    def __init__(self, vertexList):
        self.vertexList = vertexList;
        self.nodeList = [];
        self.nodecount = 0;
        self.setCount = 0;
        self.makeSet(vertexList);

    def find(self, node):
        currentNode = node;

        while currentNode.parentNode is not None:
            currentNode = currentNode.parentNode;

        root = currentNode;
        currentNode = node;

        while currentNode is not root:
            temp = currentNode.parentNode;
            currentNode.parentNode = root;
            currentNode = temp;

        return root.nodeIid;

    def merge(self, node1, node2):
        index1 = self.find(node1);
        index2 = self.find(node2);

        if index1 == index2:
            return; # they are in the same set
        
        root1 = self.nodeList[index1];
        root2 = self.nodeList[index2];

        if root1.height < root2.height:
            root1.parentId = root2;
        elif root1.height > root2.height:
            root2.parentId = root1;
        else:
            root2.parentId = root1;
            root1.height = root1.height + 1;

    def makeSet(self, vertex):
        node = Node(0, len(self.nodeList), None);
        vertex.node = node;
        self.rootNodes.append(node);
        set.setCount = set.setCount + 1;
        self.nodecount = self.nodecount + 1;

class KruskalAlgorithm(object):

    def spinningTree(self, vertexList, edgeList):
        disjoinSet = DisjoinSet(vertexList);
        treeEdges = [];

        edgeList.sort();

        for edge in edgeList:
            u = edge.startVertex;
            v = edge.targetVertex;

            if disjoinSet.find(u.node) is not disjoinSet.find(v.node):
                treeEdges.append(edge);
                disjoinSet.merge(u.node, v.node);

        for edge in spinningTree:
            print(edge.startVertex.name, " - ", edge.targetVertex.name);