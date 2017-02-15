def kth_last_node(k, head):
    
    node_list = [head]
    
    while node.next:
        node_list.append(node.next)
        node = node.next

    return node_list[-k]


def kth_last_node_alternative(k, head):
    
    num_nodes = 1
    node = head

    while node.next:
        num_nodes += 1
        node = node.next

    num_count = 1
    node = head
    
    while num_count < num_nodes - k + 1:
        num_count += 1
        node = node.next

    return node

def kth_last_node_optimal(k, head):

    start = head
    end = head
    
    for i in range(k):
        end = end.next
    
    while end.next:
        start = start.next
        end = end.next

    return start