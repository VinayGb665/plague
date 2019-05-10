#include <bits/stdc++.h>
#define pb push_back
using namespace std;
long long Best(bool visnodes[],vector<long long> eds[],long long weight[],long 
    long strvertx,long long x,long long num)
{
     visnodes[strvertx]=1;
    if((eds[strvertx].size()==1&&(strvertx!=1||num==1))||eds[strvertx].size()==0
        )
       {
           if(weight[strvertx]>=0)
            return weight[strvertx];
             if(weight[strvertx]>-x)
                return weight[strvertx];
                              return -x;
       }
       long long ansfinal=0;
       for(long long i=0;i<eds[strvertx].size();i++)
       {
                long long ed=eds[strvertx][i];
                if(visnodes[ed])
                    continue;
            long long opt=Best(visnodes,eds,weight,eds[strvertx][i],x,num);
                  ansfinal+=opt;
       }
      ansfinal+=weight[strvertx];
   if(ansfinal<-x)
     ansfinal=-x;
  return ansfinal;
}
int main()
{
    long long tcase;
    cin >> tcase;
    long long num, x;
    while (tcase--)
    {
        cin >> num >> x;
        long long weight[num + 1];
        for (long long i = 1; i <= num; i++)
            cin >> weight[i];
        bool visnodes[num + 1];
        memset(visnodes, false, sizeof(visnodes));
        visnodes[0] = true;
        vector< long long>  eds[num + 1];
        for (long long i = 1; i < num; i++)
        {
            long long a, b;
            cin >> a >> b;
                        eds[a].pb(b);
            eds[b].pb(a);
        }
        cout << Best( visnodes,eds,weight, 1, x,num) << endl;
    }
}