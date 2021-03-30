from collections import defaultdict

n = int(input())
i = 1
divi = []
while(i*i <= n):
	if(not (n % i)):
		divi.append(i)
		if( n//i != i):
			divi.append(n//i)
	i += 1
new_divi = sorted(divi)
#print(divi, new_divi)
res = [set() for i in range(len(new_divi)) ]
res[0].add(0)

for i in range(len(new_divi)):
	for j in range(i):
		if new_divi[i] % new_divi[j] == 0:
			all_ints = [x for x in res[j]]
			for l in all_ints:
				res[i].add(l + new_divi[i]//new_divi[j] - 1)

#print(res)
print(len(res[len(res)-1]))
for e in sorted(list(res[len(res)-1])):
	print(e,end=" ")
print()
# int main()
# {
# 	scanf("%d", &n);
# 	for (int i=1; i*i<=n; i++)
# 	{
# 		if (!(n%i))
# 		{
# 			divi.push_back(i);
# 			if (n/i!=i)
# 				divi.push_back(n/i);
# 		}
# 	}
# 	sort(divi.begin(), divi.end());
# 	res.resize(divi.size());
# 	res[0].insert(0);
# 	for (int i=0; i<(int)divi.size(); i++)
# 		for (int j=0; j<i; j++)
# 			if (!(divi[i]%divi[j]))
# 				for (int l : res[j])
# 					res[i].insert(l+divi[i]/divi[j]-1);
	
# 	printf("%d\n", (int)res.back().size());
# 	for (int i : res.back())
# 		printf("%d ", i);
# 	printf("\n");
# 	return 0;
# }