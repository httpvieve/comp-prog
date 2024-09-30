#include<stdio.h>
#include<malloc.h>
#define N 10
#define BALANCED 0
#define LEFT_LEANING 1
#define RIGHT_LEANING 2

typedef struct node_tag{
	int x, height;
	struct node_tag *parent;
	struct node_tag *left;
	struct node_tag *right;
}avl_node;

int max(int a, int b){
	return(a>b?a:b);
}

void updateheight(avl_node *temp){
	if(temp!=NULL)
		temp->height = max(temp->left==NULL?-1:temp->left->height,temp->right==NULL?-1:temp->right->height)+1;
}

void left_rotate(avl_node **rootptr){
	avl_node *temp1;

	if(rootptr!=NULL && *rootptr!=NULL && (*rootptr)->right!=NULL){
		temp1 = (*rootptr)->right;
		
		(*rootptr)->right = temp1->left;
		if(temp1->left!=NULL)
			temp1->left->parent = (*rootptr);

		temp1->parent = (*rootptr)->parent;

		(*rootptr)->parent = temp1;
		temp1->left = (*rootptr);

		if(temp1->parent != NULL){
			if(temp1->parent->right == *rootptr)
				temp1->parent->right = temp1;
			else
				temp1->parent->left = temp1;
		}

		*rootptr = temp1;

		updateheight(temp1->left);
		updateheight(temp1);

	}

}

void right_rotate(avl_node **rootptr){
	avl_node *temp1;

	if(rootptr!=NULL && *rootptr!=NULL && (*rootptr)->left!=NULL){
		temp1 = (*rootptr)->left;

		(*rootptr)->left = temp1->right;
		if(temp1->right!=NULL)
			temp1->right->parent = (*rootptr);

		temp1->parent = (*rootptr)->parent;

		(*rootptr)->parent = temp1;
		temp1->right = (*rootptr);

		if(temp1->parent != NULL){
			if(temp1->parent->left == *rootptr)
				temp1->parent->left = temp1;
			else
				temp1->parent->right = temp1;
		}

		*rootptr = temp1;

		updateheight(temp1->right);
		updateheight(temp1);

	}

}

void insert_fixup(avl_node **rootptr, avl_node *temp){
	int current = BALANCED, previous, lh, rh;

	do{

		lh= (temp->left==NULL?-1:temp->left->height);
		rh= (temp->right==NULL?-1:temp->right->height);

		previous=current;
		current = (lh==rh?BALANCED:(lh>rh?LEFT_LEANING:RIGHT_LEANING));

		if(abs(lh-rh)>1){
			if(current==LEFT_LEANING){
				if(previous==LEFT_LEANING)
					right_rotate(&temp);
				else{
					left_rotate(&(temp->left));
					right_rotate(&temp);
					
				}
			}
			else{
				if(previous==RIGHT_LEANING)
					left_rotate(&temp);
				else{
					right_rotate(&(temp->right));
					left_rotate(&temp);
					
				}
			}
		} //end if

		updateheight(temp);

		if(temp->parent==NULL)
			*rootptr = temp;

		temp =temp->parent;

	}while(temp!=NULL);
}

void insert_node(avl_node **rootptr, avl_node *temp){
	if(*rootptr==NULL) *rootptr = temp;
	else{
		temp->parent = *rootptr;

		if((*rootptr)->x < temp->x)
			insert_node(&((*rootptr)->right),temp);
		else
			insert_node(&((*rootptr)->left),temp);
	}
}

void insert_value(avl_node **rootptr, int x){
	avl_node *temp;
	temp = (avl_node *)malloc(sizeof(avl_node));
	temp->x = x;
	temp->height = 0;
	temp->parent = temp ->left = temp->right = NULL;
	insert_node(rootptr, temp);
	insert_fixup(rootptr, temp);
}

void view(avl_node *root, int tabs){
	int i;
	if(root != NULL){
		view(root->right, tabs +1);
		for(i=0; i<tabs; i++) printf("\t");
		printf("%2i\n", root->x);
		view(root->left, tabs +1);
	}
}

void swap(int *a, int *b){
	int temp;
	temp = *a; *a= *b; *b =temp;
}

// void* avl_delete(avl_node** rootptr, int key){
	
	// // find node
	// if (root == NULL)
	// 	return root;

	// if (key < root->x)
	// 	root->left = avl_delete(rootptr, root->left, key);

	// else if (key > root->x)
	// 	root->right = avl_delete(rootptr, root->right, key);

	// // once found, do BST delete
	// else{

	// 	if ((root->left == NULL) || (root->right == NULL)){
	// 		avl_node* temp = root->left ? root->left : root->right;
			
	// 		// no child
	// 		if (temp == NULL){
	// 			temp = root;
	// 			root = NULL;
	// 		}else{
	// 			*root = *temp; 
	// one child
	// 		}
			
	// 		free(temp); // delete
	// 	}
	// 	else{
	// 		// two children
			
	// 		// get descendant successor
	// 		avl_node* successor = root;
	// 		while(successor->left != NULL)
	// 			successor = successor->left;
			
	// 		root->x = successor->x; // copy

	// 		root->right = avl_delete(rootptr, root->right, successor->x);
	// 	}
	// }
	// // if tree only had one node
	// if (root == NULL)
	// 	return root;
	
	// // update height
	// updateheight(root);

	// get balance factor of current node
	// int balance, lh, rh;

	// lh= (root->left==NULL?-1:root->left->height);
	// rh= (root->right==NULL?-1:root->right->height);

	// balance = (lh==rh?BALANCED:(lh>rh?LEFT_LEANING:RIGHT_LEANING));

	// if (balance > 1 && lh >= 0){
	// 	printf("u are here\n");
	// 	right_rotate(&root);
	// }

	// if (balance > 1 && lh < 0){
	// 	left_rotate(&(root->left));
	// 	right_rotate(&root);
	// }

	// if (balance < -1 && rh <= 0){
	// 	left_rotate(&root);
	// }

	// if (balance < -1 && rh > 0){
	// 	right_rotate(&(root->right));
	// 	left_rotate(&root);
	// }

	// return root;
// }

void avl_delete(avl_node** rootptr, int key){
	// non-recursive
	// find nodec
	printf("wtf?");
	avl_node* toDel = *rootptr;

	printf("eh dito?");
	// printf("\n toDel = %d", toDel->x);
	while(toDel != NULL){
		if (key < toDel->x) toDel = toDel->left;
		else if (key > toDel->x) toDel = toDel->right;
	}
	printf("\n toDel = %d", toDel->x);

	// once found, do BST delete
	if ((toDel->left == NULL) || (toDel->right == NULL)){
		avl_node* temp = toDel->left ? toDel->left : toDel->right;
		
		// no child
		if (temp == NULL){
			printf("u are here\n");
			temp = toDel;
			toDel = toDel->parent;
		}else{
			// one child
			toDel->x = temp->x;
			toDel->left = NULL;
			toDel->right = NULL;
		}

		free(temp); // delete
	}
	else{
		// two children
		
		// get descendant successor
		avl_node* successor = toDel->right;
		while(successor->left != NULL)
			successor = successor->left;

		avl_delete(rootptr, successor->x);
	}
	
	// if tree only had one node
	if (rootptr == NULL)
		return;
	
	// update height of current
	// updateheight(toDel);

	int current = BALANCED, previous, lh, rh;
	printf("\nkey = %d\n", toDel->x);
	avl_node* temp = toDel;

	do{

		lh= (temp->left==NULL?-1:temp->left->height);
		rh= (temp->right==NULL?-1:temp->right->height);

		previous=current;
		current = (lh==rh?BALANCED:(lh>rh?LEFT_LEANING:RIGHT_LEANING));

		if(abs(lh-rh)>1){
			if(current==LEFT_LEANING){
				if(previous==LEFT_LEANING){
					printf("u are here\n");
					right_rotate(&temp);
				}
				else{
					left_rotate(&(temp->left));
					right_rotate(&temp);
					
				}
			}
			else{
				if(previous==RIGHT_LEANING)
					left_rotate(&temp);
				else{
					right_rotate(&(temp->right));
					left_rotate(&temp);
					
				}
			}
		} //end if

		updateheight(temp);

		if(temp->parent==NULL)
			*rootptr = temp;

		temp =temp->parent;

	}while(temp!=NULL);
	
}


int main(){
	avl_node *root = NULL;
	int i,n=10;
	
	
	
	for(i=0; i<n; i++){
		insert_value(&root,i+1);
		view(root,0);
		printf("\n----------------------------------------\n");
	}
	
	insert_value(&root,0);
	view(root, 0);
	printf("\n----------------------------------------\n");

	avl_delete(&root, 5);
	view(root, 0);
	printf("\n----------------------------------------\n");

}