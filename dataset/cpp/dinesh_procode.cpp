#include<bits/stdc++.h>
using namespace std;
#define llin(n) scanf("%lld",&n)
#define lin(n) scanf("%ld",&n)
#define in(n) scanf("%d",&n)
#define fl(i,a,n) for(int i=a;i<n;i++)
#define rfl(i,n,a) for(int i=n-1;i>=a;i--)
#define din(n) scanf("%lf",&n)
#define lld long long int
#define ld long int 
lld values[100500];
vector<int> child[100500];
int visited[100500];
int x,y;
struct Node
{
    lld val;
    std::vector<Node*> child;
};
typedef struct Node Node;
Node* createNode(lld val){
    Node *node=new Node;
    node->val=val;
    node->child.clear();
    return node;
}
lld solve(lld k,Node *root){
    if(root==NULL)
        return 0;
    lld oSum=root->val;
    for(int i=0;i<root->child.size();i++){
        oSum+=max(solve(k,root->child[i]),k);
    }
    return max(k,oSum);
}
void ptintTree(Node *root){
    if(root==NULL){
        return;
    }
    for(int i=0;i<root->child.size();i++){
        ptintTree(root->child[i]);
    }
        }
lld count1=0;
Node* constructTree(int ind){
        visited[ind]=1;
    Node *root=createNode(values[ind]);
    for(int i=0;i<child[ind].size();i++){
        if(visited[child[ind][i]]==0){
            visited[child[ind][i]]=1;
            root->child.push_back(constructTree(child[ind][i]));
        }
    }
    return root;
}
void print2D(vector<std::vector<int> > child){
    for(int i=0;i<child.size();i++){
        for(int j=0;j<child[i].size();j++){
            cout<<child[i][j]+1<<" ";
        }
        cout<<"\n";
    }
}
int main(int argc, char const *argv[])
{
    int t;
    in(t);
        while(t--){
                int n;
        in(n);
        lld k;
        llin(k);
        k*=(-1);
        for(int i=0;i<n;i++){
            child[i].clear();
            visited[i]=0;
            llin(values[i]);
        }
        // cout<<values.size()<<"\n";
        for(int i=0;i<n-1;i++){
            in(x);
            in(y);
            child[x-1].push_back(y-1);
            child[y-1].push_back(x-1);
        }
        // print2D(child);
        visited[0]=1;
         Node *root=constructTree(0);
         // cout<<root->val<<"\n";
         // ptintTree(root);
        cout<<solve(k,root)<<"\n";
    }
}