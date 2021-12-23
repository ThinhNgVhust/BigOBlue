#include<bits/stdc++.h>
using namespace std;
const int nax = 5e4 + 10;
int k;
long long int ans = 0;
vector<int> g[nax];
int visited[nax];
vector<int> topo;
long long int f[nax][510];
long long int f_sub[nax][510];
#define NOT_VISITED -100
void dfs(int v,int parent)
{
	f_sub[v][0] = 1;
	visited[v] = parent;
	for (auto u : g[v])
	{
		if (visited[u]!= NOT_VISITED) continue;
		dfs(u,v);
		for (int i = 1; i <= k; i++)
		{
			f_sub[v][i] += f_sub[u][i - 1];
		}
	}
	topo.push_back(v);
}


int main()
{

	//memset(visited, 0, sizeof(visited));
	for (size_t i = 0; i < sizeof(visited)/sizeof(visited[0]); i++)
	{
		visited[i] = NOT_VISITED;
	}
	memset(f_sub, 0, sizeof(f_sub));
	memset(f, 0, sizeof(f));
	for (int i = 0; i < nax; i++)
		g[i].clear();
	int n;
	cin >> n >> k;
	int u,v;
	for (int i = 0; i < n - 1; i++)
	{
		cin >> u >> v;
		u--;
		v--;
		{
			g[u].push_back(v);
			g[v].push_back(u);
		}

	}


	//int ans=0;
	int root = 0;
	dfs(root,-1);
	for (size_t i = 0; i <= k; i++)
	{
		f[0][i] = f_sub[0][i];

	}
	for (size_t i = 0; i < n; i++)
	{
		f[i][0] = 1;
	}
	reverse(topo.begin(), topo.end());
	for (size_t i = 1; i < topo.size(); i++)
	{
		u = topo.at(i);
		for (size_t j = 1; j <= k; j++)
		{
			if (j >= 2)
				f[u][j] = f_sub[u][j] + (f[visited[u]][j - 1] - f_sub[u][j - 2]);
			else
				f[u][j] = f_sub[u][j] + (f[visited[u]][j - 1]);
		}
	}
	for (size_t i = 0; i < n; i++)
	{
		ans += f[i][k];
	}
	cout << ans / 2 << endl;

}