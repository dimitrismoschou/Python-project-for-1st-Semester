# -*-coding:utf-8-*-
list1=[1,2,3,4,5]
def maxDistance (list1,x): #ορίζω την συνάρτηση
                sum = 0
                for i in list1:
                        sum = sum + i
                        if sum > x :
                                    sum = sum - i
                return ('το μεγαλύτερο άθροισμα στοιχείων της λίστας ώστε να μην υπερβαίνουν τον ακέραιο που περάσε σαν δεύτερο όρισμα είναι το', (sum))
	
print (maxDistance(list1,6))
