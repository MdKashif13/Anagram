lstfile=open("wlist","r",encoding="utf-8")
lst=[]
for i in lstfile:
	lst.append(i)
nwlst=[]
for x in lst:
	nwlst.append(x.replace("\n",""))
while True:
	word=(input(">>").lower())
	for a in range(len(nwlst)):
		if len(word)==len(nwlst[a]):
			if sorted(word)==sorted(nwlst[a]):
				print("Match Found ->",nwlst[a])



