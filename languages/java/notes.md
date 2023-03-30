# NOTES  
  
//organized in hierarchies  
interface - class  
  
  
Iterator  
  
JAVA COLLECTIONS:  
Iterable  
Collection  
  
Collection -> List  
ArrayList	Deque->LinkedList		Vector  
						Stack  
Collection -> Queue  
	Deque			PriorityQueue  
	ArrayDeque  
  
Collection -> Set  
	SortedSet		HashSet		LinkedHashSet  
	TreeSet  
  
  
(interface) MAP<K,V>:  
  
  
  
ArrayList:  
//fast access at i-element  
//slow insert/remove  
access:  
1 -	for(type var : list)  
2 -	Iterator it = someArrayList.iterator()  
	  
.get(int index) :  
  
Iterable:  
.iterator() : returns iterator in proper sequence  
  
Iterator:  
//accesses elements in sequence  
boolean .hasNext() :  
.next() : returns current element, goes to next  
.size() :   
  
LinkedList:  
(implemented as doubly linked list)  
//slow access at i-element  
//fast insert/remove  
