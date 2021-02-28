# Notes on Convex and Non-convex 

---

## 1. What if an equation has only one solution or has multiple solutions?
The basic difference between convex and non-convex is that in a) convex optimization there can be only one optimal solution, which is globally optimal or you might prove that there is no feasible solution to the problem, while in b) nonconvex optimization may have multiple locally optimal points and it can take a lot of time to identify whether the problem has no solution or if the solution is global. Hence, the efficiency in time of the convex optimization problem is much better. From my experience a convex problem usually is much more easier to deal with in comparison to a non convex problem which takes a lot of time and it might lead you to a dead end.

## Non-convex problem has no axact **analysis solution**. It is also hard to recognize. You can use some methods to identity a convex or not by,
1. Using defination of convex , adds new variables;
2. Using its derivative or Hessian properties;
3. Several geometrical convex properties: combination of convex;
4. By intuition or try graph it.
