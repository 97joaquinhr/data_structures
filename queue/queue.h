#ifndef QUEUE_H_
#define QUEUE_H_

// A linked list (LL) node to store a queue entry 
struct q_node 
{ 
    int key; 
    struct q_node *next; 
}; 
// The queue, front stores the front node of LL and rear stores the 
// last node of LL 
struct queue 
{ 
    struct q_node *front, *rear; 
};

typedef struct q_node QNode;
typedef struct queue Queue;

QNode* newNode(int k);
Queue* createQueue();
void enQueue(Queue* q,int k);
QNode* deQueue(Queue* q);

#endif // QUEUE_H_