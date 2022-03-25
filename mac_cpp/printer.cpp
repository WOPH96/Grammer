#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

// struct comp{
//     bool operator()(pair<int,int> &p1,pair<int,int> &p2){
//         if(p1.first==p2.first)
//             return p1.second > p2.second;
//         return p1.first<p2.first;
//     }
// };

int solution(vector<int> priorities, int location)
{
    int answer = 0;
    queue<pair<int, int>> q;
    priority_queue<pair<int, int>> pq;

    for (int i = 0; i < priorities.size(); i++)
    {
        q.push({priorities[i], i});
        pq.push({priorities[i], -i});
    }

    while (!q.empty())
    {

        pair<int, int> tmp;
        tmp = q.front();

        if (tmp.first >= pq.top().first)
        {
            answer += 1;
            if (tmp.second == location)
                break;
            q.pop();
            pq.pop();
        }
        else
        {
            q.pop();
            q.push(tmp);
        }
    }

    // while (!q.empty()){
    //     cout << q.front().first << q.front().second << endl;
    //     cout << pq.top().first << -pq.top().second << endl;
    //     cout<<endl;
    //     q.pop();
    //     pq.pop();
    // }

    return answer;
}