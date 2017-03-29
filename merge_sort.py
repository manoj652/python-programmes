def merge(a,b):
	c = []
	if len(a) != 0 and len(b) != 0:
		if a[0] < b[0]:
			c.append(a[0])
			a.remove(a[0])
		else:
			c.append(b[0])
			b.remove(b[0])
	if len(a) == 0:
		c += b
	else:
		c += a
		return c

def merge_sort(x):
	if len(x) == 0 and len(x) == 1:
		return(x)
	else:
		mid = len(x)//2
		a = merge_sort(x[:mid])
		b = merge_sort(x[:mid])
		return(a,b)
def test_empty():
	list = merge_sort([])
	assert(len(list) == 0)
