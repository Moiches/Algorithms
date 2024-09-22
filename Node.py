class Node:
    def __init__(self, numero):
        self.numero = numero
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  ##head indica cual es el primer nodo en la lista


    def insert_node_at_start(self, numero):
        new_node = Node(numero)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_node_at_end(self, numero):
        new_node = Node(numero)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while(current.next):
            current = current.next

        current.next = new_node


    def print_linked_list(self):
        current = self.head
        while(current):
            print(current.numero, '->', end=" ")
            current = current.next

    def delete_node_at_start(self):
        self.head = self.head.next

        if self.head is None:
            print("There's nothing to delete")
            return
    def delete_node_at_end(self):
        if self.head is None:
            print("There's nothing to delete, the list is empty")
            return
        ## when there is only one element
        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next ## de esta manera apuntamos a una posicion anterior a la final y por ende al no apuntar a ningun lado de referencia el ultimo nodo, el garbage collector lo eliminara eventualmente
            ## ern otras palabras si nos e hace referencia por ningun lado al nodo .next.next el garbage collectro de python lo eliminara
        current.next = None

    ##determine if an element exists
    def exist_an_element(self, numero):
        if self.head is None:
            print("There's nothing to find")
            return False
        current = self.head

        while(current.numero != numero):
            current = current.next

            if current is None:
                return False
        return True


my_list = LinkedList()
my_list.insert_node_at_start(21)
my_list.insert_node_at_start(11)
my_list.insert_node_at_start(13)
my_list.insert_node_at_start(14)
my_list.insert_node_at_end(27)

print(my_list.exist_an_element(15))

my_list.print_linked_list()
