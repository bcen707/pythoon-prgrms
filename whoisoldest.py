def whoOldest(a1, a2, a3):
    if a2<a3 and a1<a3:
        print("The oldest person in the group is", a3)
    elif a1<a2 and a3<a2:
        print("The oldest person in the group is", a2)
    elif a2<a1 and a3<a1:
        print("The oldest person in the group is", a1)
    else:
        print("2 or more people in the group are of the same age.")

# how should I handle 2-way or 3-way ties???

# 2way tie; 3 case checks:
  a1 == a2 and a1 != a3 
  a2 == a3 and a2 != a1
  a1 == a3 and a1 != a2