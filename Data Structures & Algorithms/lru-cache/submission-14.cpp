struct ListNode {
    int val;
    int key;
    ListNode *next;
    ListNode *prev;
    ListNode() : key(0), val(0), next(nullptr), prev(nullptr) {}
};


class LRUCache {
private:
    int cap;
    int currSize;
    ListNode *left;
    ListNode *right;
    unordered_map<int, ListNode*> key2node;
public:
    LRUCache(int capacity) {
        cap = capacity;
        currSize = 0;
        left = new ListNode();
        right = new ListNode();
        left->next = right;
        right->prev = left;
    }
    
    int get(int key) {
        if (!key2node.count(key)) {
            return -1;
        }

        ListNode* node = key2node[key];
        pop(node);
        push(node);
        return key2node[key]->val;
    }
    
    void put(int key, int value) {
        if (key2node.count(key)) {
            ListNode* node = key2node[key];
            key2node[key]->val = value;
            pop(node);
            push(node);
            return;
        }
        currSize += 1;
        ListNode* node = new ListNode();
        node->val = value;
        node->key = key;
        key2node[key] = node;
        push(node);

        if (currSize > cap) {
            ListNode* remove = right->prev;
            pop(remove);
            key2node.erase(remove->key);
            currSize -= 1;
            delete remove;
        }
        return;



    }

    void pop(ListNode* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }
    void push(ListNode* node) {
        left->next->prev = node;
        node->next = left->next;
        node->prev = left;
        left->next = node;
    }

};
