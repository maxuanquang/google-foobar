'''
Disorderly Escape
=================
Oh no! You've managed to free the bunny workers and escape 
Commander Lambdas exploding space station, but Lambda's team 
of elite starfighters has flanked your ship. If you dont jump 
to hyperspace, and fast, youll be shot out of the sky!

Problem is, to avoid detection by galactic law enforcement, 
Commander Lambda planted the space station in the middle of a 
quasar quantum flux field. In order to make the jump to 
hyperspace, you need to know the configuration of celestial 
bodies in the quadrant you plan to jump through. In order to 
do *that*, you need to figure out how many configurations each 
quadrant could possibly have, so that you can pick the optimal 
quadrant through which youll make your jump.

There's something important to note about quasar quantum flux 
fields' configurations: when drawn on a star grid, 
configurations are considered equivalent by grouping rather 
than by order. That is, for a given set of configurations, if 
you exchange the position of any two columns or any two rows 
some number of times, youll find that all of those 
configurations are equivalent in that way -- in grouping, 
rather than order.

Write a function solution(w, h, s) that takes 3 integers and 
returns the number of unique, non-equivalent configurations that 
can be found on a star grid w blocks wide and h blocks tall 
where each celestial body has s possible states. Equivalency 
is defined as above: any two star grids with each celestial 
body in the same state where the actual order of the rows and 
columns do not matter (and can thus be freely swapped around). 
Star grid standardization means that the width and height of 
the grid will always be between 1 and 12, inclusive. And while 
there are a variety of celestial bodies in each grid, the number 
of states of those bodies is between 2 and 20, inclusive. The 
solution can be over 20 digits long, so return it as a decimal 
string. The intermediate values can also be large, so you will 
likely need to use at least 64-bit integers.

For example, consider w=2, h=2, s=2. We have a 2x2 grid where 
each celestial body is either in state 0 (for instance, silent) 
or state 1 (for instance, noisy). We can examine which grids are 
equivalent by swapping rows and columns.

00
00

In the above configuration, all celestial bodies are "silent" - 
that is, they have a state of 0 - so any swap of row or column 
would keep it in the same state.

00 | 00 | 01 | 10
01 | 10 | 00 | 00

1 celestial body is emitting noise - that is, has a state of 1 
- so swapping rows and columns can put it in any of the 4 
positions. All four of the above configurations are equivalent.

00 | 11
11 | 00

2 celestial bodies are emitting noise side-by-side. Swapping 
columns leaves them unchanged, and swapping rows simply moves 
them between the top and bottom. In both, the *groupings* are 
the same: one row with two bodies in state 0, one row with two 
bodies in state 1, and two columns with one of each state.

01 | 10
01 | 10

2 noisy celestial bodies adjacent vertically. This is symmetric 
to the side-by-side case, but it is different because there's no 
way to transpose the grid.

01 | 10
10 | 01

2 noisy celestial bodies diagonally. Both have 2 rows and 2 
columns that have one of each state, so they are equivalent to 
each other.

01 | 10 | 11 | 11
11 | 11 | 01 | 10

3 noisy celestial bodies, similar to the case where only one of 
four is noisy.

11
11

4 noisy celestial bodies.

There are 7 distinct, non-equivalent grids in total, so 
solution(2, 2, 2) would return 7.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown 
here.

-- Java cases --
Input:
Solution.solution(2, 2, 2)
Output:
    7

Input:
Solution.solution(2, 3, 4)
Output:
    430

-- Python cases --
Input:
solution.solution(2, 3, 4)
Output:
    430

Input:
solution.solution(2, 2, 2)
Output:
    7
'''
# Since this problem requires another level of math to solve it, I think its
# code is best written with Literate programming, a skill I rarely use for
# day-to-day work.
#
# https:#en.wikipedia.org/wiki/Literate_programming
#
# The result of Literate Programming is the comments on this file are not
# typical Javadoc (so don't blame me). Instead, it's my reasoning behind the
# computation.
#
# Kindly note that I cannot explain everything. Curious readers should learn a
# bit about Group theory to fully understand the terms used in the solution.
#
# "An introduction to group theory" by Tony Gaglione is a good resource (beside
# many other resources I use to grasp the basic of Group Theory).
#
# https:#wdjoyner.files.wordpress.com/2016/08/gaglione-gp-thry.pdf
#
# Since I'm not even an amateur mathematician, pardon me if some terms used
# below is incorrect or mismatches with their rigorous mathematics definition.
import math


def solution(width, height, states):
    '''
    We'll use Burnside's lemma to solve this problem.

    https:#en.wikipedia.org/wiki/Burnside%27s_lemma

    Our set X is all the possible states of the matrix. Size of X can be
    easily computed:

    |X| = W*H

    The group G that acts on it are the products of the row and column
    permutations. In math terms, the permutations groups are called Symmetric
    Group and denote as S_n, where n is the size of the set to be permuted.

    https:#en.wikipedia.org/wiki/Symmetric_group

    For our matrix of WxH cells, the column permutations is S_w and row
    permutations is S_h. Thus:

    G = S_w.S_h
    |G| = W!*H!

    Note that the dot `.` notation means the "multiplication" in Group
    Theory, while the asterisk `*` is our typical numeric multiplication.

    Unlike the cube's faces coloring example in Burnside's lemma article,
    there's too many action in G to list them all and derive number of fixed
    elements in X for each action. We need another way.

    From now on, we will use Cycle Notation to denote the permutation.

    https:#en.wikipedia.org/wiki/Permutation#Cycle_notation

    Let's use following example with specific permutations to get an
    intuitive idea how to solve it.

    - W=8, H=7.
    - Column permutation c=(0,1,2)(3,4). This fixes _3 columns_: 5, 6, 7.
    - Row permutation r=(0,1)(2,3,4). This fixes _2 rows_: 5, 6.

                            fixed
                            -----
              0 1 2   3 4   5 6 7
            +--------------------
           0| a a a   b b   m m m
           1| a a a   b b   m m m
            |
           2| d d d   e e   g g g
           3| d d d   e e   g g g
           4| d d d   e e   g g g
            |
    fixed |5| i i i   k k   F F F
          |6| i i i   k k   F F F

    We can see that the 2 permutations r and c split the matrix into multiple
    smaller one.

    Let's call M(a) to dente the sub-matrix consists of only a cells.
    Similar, M(F) is the one consists of only F cells.

    Let's also use |M(a)| to denote number of possible configuration of M(a).
    Thus, the number of fixed elements in X for this particular r.c
    permutation is:

    |X^(r.c)| = |M(a)| .|M(b)|...|M(F)|

    There's some properties that can help us to calculate some of those
    |M(x)|.

    - F cells are fixed by both r and c. So they can use any of S states.
    Thus: |M(F)| = S^(3*2) = S^6. It's example of sub-matrix that is entirely
    (2-side) fixed.

    - All columns of M(m) are fixed by r, so cells in same rows don't need
    have same state. However, c will swap row 0 and 1, in order to fix M(m),
    we need all cells in each of columns 5, 6, 7 to have same state. This
    leads to: |M(m)| = S^3

    - With same logic, we can calculate number of fixed elements of M(g),
    M(i), M(k). Including M(m), they are example for how to calculate number
    of sub-matrix that has 1 side fixed.

    Now, how do we calculate number of those sub-matrix that has 0-side
    fixed. Let's look closer to how cells in M(d) move after the
    permutations.

              0 1 2
            +------
           2| d d d
           3| d d d
           4| d d d

    The permutations affects M(d) is: c1=(0,1,2) and r1=(2,3,4). Let's use
    [x,y] notation to call the cell at column x and row y.  We can see that:

    - [0,2] move to [1,3]
    - [1,3] more to [2,4]
    - [2,4] more to [0,2]

    In order for M(d) to be fixed, it requires 3 cells [0,2], [1,3] and [2,4]
    to have same state. Similarly, following group of 3 cells must have same
    states:

    - [1,2], [2,3], [0,4]
    - [2,2], [0,3], [1,4]

    To visualize the finding, here's how M(d) should look like:

               0   1   2
            +-----------
           2| d1  d2  d3
           3| d3  d1  d2
           4| d2  d3  d1

    It's now clear that |M(d)| = S^3.

    Please try it yourself to see:

    - |M(a)| = S^1 = S
    - |M(b)| = S^2
    - |M(e)| = S

    We can see that our permutations split the sub-matrix into several
    disjoint circles, and:

    - Each cell belong to exactly and 1 circle, and move within it if we
    apply the permutations repetitively.
    - In order to fix the sub-matrix, it requires all cells in same circle to
    have same state.

    Let use len(r1) to denote the length of the row permutation r1. Similar,
    len(c1) means length of column permutation c1.

    It's easy to see that the size of the sub-matrix is len(c1).len(r1).

    You might also guess that the number of circles within each sub-matrix is
    also determined by the length of permutations. Indeed, it is.

    Think about how the top-left in sub-matrix travel in its circle if we
    apply the permutations repetitively. Let's say its original location is
    [0, 0] (relative to the sub-matrix location within the parent matrix).

    It needs len(r1) steps to go back to top row. For each steps, beside
    moving between rows, it also move between columns. Hence, by the time it
    go back to top row, its location should be:

    [len(r1) % len(c1), 0]

    If we repetitively apply k times len(r1) steps, then the cell location
    after that would be:

    [k * len(r1) % len(c1), 0]

    Our cycle length is determined by the smallest k such that:

    k*len(r1) % len(c1) == 0

    Thus

    k*len(r1) == lcm(len(r1), len(r2))

    where lcm(a, b) is the Least Common Multiple of a and b.

    Now, we can see that:

    |M(d)| = S^( len(r1)*len(c1) / lcm(len(r1),len(c1) )

    We can verify our examples again:

    - |M(a)| = S^(2*3/lcm(2,3)) = S^(6/6) = S
    - |M(b)| = S^(2*2/lcm(2,2)) = S^(4/2) = S^2
    - |M(d)| = S^(3*3/lcm(3,3)) = S^(9/3) = S^3
    - |M(e)| = S

    Now, with all the logic reasoned, we know what do implements:

    - Generate all the pairs (fixed_num, [l_0, l_1, ..., l_k]) from W Here,
    fixed_num is number of columns that is fixed by the permutation on W, l_i
    (where 0 <= i <= k) is length of the disjoint circles withing that
    permutation. Note that sum of fixed_num and all l_i must be equal to W.
    Let's call it per(W).

    - Similarly, generate per(H).

    - For each item in per(W), we calculate number of fixed matrices against
    it and all items in per(H) according to our logic.

    - The sum of all result from above steps, after divide for |G| is our
    final result.
    '''
    col_permutations = gen_permutations(width)
    row_permutations = gen_permutations(height)

    total = 0
    for cp in col_permutations:
        s = 0
        for rp in row_permutations:
            num_fixed_matrices = count_fixed_matrices(rp, cp, states)
            s += num_fixed_matrices
        total += s

    G = math.factorial(width) * math.factorial(height)
    result = total // G
    return str(result)


class Permutation:
    def __init__(self, fixed, cycles, count):
        self.fixed = fixed
        self.cycles = cycles
        self.count = count


def gen_permutations(n):
    result = []
    for fixed in range(n - 1):
        cycles_list = numbers_sum_to_n(n - fixed)
        for cycles in cycles_list:
            p = make_permutation(n, fixed, cycles)
            result.append(p)

    result.append(Permutation(n, [], 1))  # identity permutation
    return result


def make_permutation(n, fixed, cycles):
    count = math.comb(n, fixed)

    remains = n - fixed
    repeated_len, previous_len = 1, 0

    for ln in cycles:
        selections = math.comb(remains, ln)
        remains = remains - ln
        disjoint_cycles = math.factorial(ln - 1)
        count = count * selections * disjoint_cycles

        if previous_len == ln:
            repeated_len += 1
        else:
            count = count // math.factorial(repeated_len)
            repeated_len = 1
            previous_len = ln

    count = count // math.factorial(repeated_len)
    return Permutation(fixed, cycles, count)


def count_fixed_matrices(rp, cp, S):
    fixed = S ** (rp.fixed * cp.fixed)
    fixed *= rp.count
    fixed *= cp.count

    m = S ** (cp.fixed * len(rp.cycles))
    fixed *= m

    m = S ** (rp.fixed * len(cp.cycles))
    fixed *= m

    t = 0
    for lr in rp.cycles:
        for lc in cp.cycles:
            v = lr * lc // math.lcm(lr, lc)
            t += v

    m = S ** t
    fixed *= m
    return fixed


def numbers_sum_to_n(n):
    res = []
    ls = [0] * (n // 2 + 1)
    generate_numbers(n, ls, 0, 2, res)
    return res


def generate_numbers(n, ls, pos, start, res):
    if n == 0:
        res.append(ls[:pos])
        return

    for i in range(start, n + 1):
        ls[pos] = i
        generate_numbers(n - i, ls, pos + 1, i, res)


if __name__ == "__main__":
    inputs = [
        (1, 1, 1),
        (1, 1, 2),
        (1, 1, 3),
        (1, 1, 4),
        (2, 1, 1),
        (2, 1, 2),
        (2, 1, 3),
        (2, 2, 1),
        (2, 2, 2),
        (2, 2, 3),
        (2, 2, 4),
        (3, 2, 2),
        (3, 2, 3),
        (3, 2, 4),
        (3, 3, 2),
        (3, 3, 5),
        (3, 3, 10),
        (8, 3, 4),
        (2, 9, 7),
        (5, 5, 5),
        (12, 12, 20),
    ]

    answers = [
        "1",
        "2",
        "3",
        "4",
        "1",
        "3",
        "6",
        "1",
        "7",
        "27",
        "76",
        "13",
        "92",
        "430",
        "36",
        "57675",
        "27969700",
        "1774852035",
        "4498416692",
        "20834113243925",
        "97195340925396730736950973830781340249131679073592360856141700148734207997877978005419735822878768821088343977969209139721682171487959967012286474628978470487193051591840"
    ]

    correct = 0
    for input, answer in zip(inputs, answers):
        output = solution(*input)
        print("input :", input)
        print("output:", output)
        print("answer:", answer)
        print("----------------------")
        if output == answer:
            correct += 1
    print(f"Congratulations! You scored {correct} out of {len(answers)}.")

    import pdb
    pdb.set_trace()
