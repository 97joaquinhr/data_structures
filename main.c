#include<stdio.h>
#include "queue/queue.h"
#include "binary_tree/binary_tree.h"

int main(){
    Node *root = newTreeNode(1);

    root->left  = newTreeNode(2);
    root->right = newTreeNode(3);
    root->left->left = newTreeNode(4);
	printf("Hello world\n");
	Queue *q = createQueue();
	enQueue(q, 10); 
    enQueue(q, 20); 
    deQueue(q); 
    deQueue(q); 
    enQueue(q, 30); 
    enQueue(q, 40); 
    enQueue(q, 50); 
    QNode *n = deQueue(q); 
    if (n != NULL) 
      printf("Dequeued item is %d", n->key); 
	getchar();
	return 0;
}