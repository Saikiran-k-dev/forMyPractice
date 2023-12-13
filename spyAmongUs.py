##Write your code here
trustedOnes = []
nonTrustedOnes = []
def relationFunction(relation1,relation2):
    trustedOnes.append(relation1)
    nonTrustedOnes.append(relation2)

totalNumberOfAgentsAndRelationship = input()
totalNumberOfRelationship = int(totalNumberOfAgentsAndRelationship.split()[1])

for i in range(totalNumberOfRelationship):
    relation = input()
    relation1,relation2 = relation.split()
    relationFunction(int(relation1),int(relation2))
for i in nonTrustedOnes:
    if i in trustedOnes:
        pass
    else:
        print(i)
        break
    if i == nonTrustedOnes[len(nonTrustedOnes)-1]:
        print(-1)

    
    print(i,nonTrustedOnes[len(nonTrustedOnes)-1])