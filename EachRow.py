
class EachRow:
    
    def __init__(self,nodes,splittedNodes=[]):
        self.nodes = self.replaceSlash(nodes)
        self.splittedNodes = self.splitter(nodes)
    

    def splitter(self,cell):
        if(type(cell) is int):
            return str(cell) 
        
        
        elif(cell.count(",") == 0):
            return (cell[:6])
        elif(cell.count(',') == 1):
            node1=cell[:6]
            node2=cell[8:14]
            return (node1,node2)
        elif(cell.count(',')== 2):
            node1=cell[:6]
            node2=cell[8:14]
            node3=cell[16:22]
            return (node1,node2,node3)
        elif(cell.count(',')== 3):
            node1=cell[:6]
            node2=cell[8:14]
            node3=cell[16:22]
            node4=cell[24:30]
            return (node1,node2,node3,node4)
        elif(cell.count(',')== 4):
            node1=cell[:6]
            node2=cell[8:14]
            node3=cell[16:22]
            node4=cell[24:30]
            node5=cell[32:38]
            return (node1,node2,node3,node4,node5)
        elif(cell.count(',')== 5):
            node1=cell[:6]
            node2=cell[8:14]
            node3=cell[16:22]
            node4=cell[24:30]
            node5=cell[32:38]
            node6=cell[40:46]
            return (node1,node2,node3,node4,node5,node6)
        elif(cell.count(',')== 6):
            node1=cell[:6]
            node2=cell[8:14]
            node3=cell[16:22]
            node4=cell[24:30]
            node5=cell[32:38]
            node6=cell[40:46]
            node7=cell[48:54]
            return (node1,node2,node3,node4,node5,node6,node7)
        elif(cell.count(',')== 7):
            node1=cell[:6]
            node2=cell[8:14]
            node3=cell[16:22]
            node4=cell[24:30]
            node5=cell[32:38]
            node6=cell[40:46]
            node7=cell[48:54]
            node8=cell[56:62]
            return (node1,node2,node3,node4,node5,node6,node7,node8)
        elif(cell.count(',')== 8):
            node1=cell[:6]
            node2=cell[8:14]
            node3=cell[16:22]
            node4=cell[24:30]
            node5=cell[32:38]
            node6=cell[40:46]
            node7=cell[48:54]
            node8=cell[56:62]
            node9=cell[64:70]
            return (node1,node2,node3,node4,node5,node6,node7,node8,node9)
        elif(cell.count(',')== 9):
            node1=cell[:6]
            node2=cell[8:14]
            node3=cell[16:22]
            node4=cell[24:30]
            node5=cell[32:38]
            node6=cell[40:46]
            node7=cell[48:54]
            node8=cell[56:62]
            node9=cell[64:70]
            node10=cell[72:78]
            return tuple(node1,node2,node3,node4,node5,node6,node7,node8,node9,node10)  # type: ignore
    def replaceSlash(self,cell):
        if(cell.count("/") == 1 ):
            cell = cell.replace("/",",")
            return cell
        else:
            return cell
            


    