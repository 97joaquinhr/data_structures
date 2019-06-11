#ifndef BINARY_TREE_H_
#define BINARY_TREE_H_

struct node
{
	int data;
	struct node *left;
	struct node *right;
};

typedef struct node Node;

Node* newTreeNode(int data);

#endif // BINARY_TREE_H_