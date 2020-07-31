#-------------------#
# Sets, parameters, #
#     variables     #
#-------------------#

# Size of the subgrids
param s := 3;
set S := 1..s;

# Size of the sudoku
param n := s^2;
set N := 1..n;

# Auxiliary set for the subgrid constraint
set A := 0..n-s by s;

# Digits known a priori; to be set in the data section
param G{N,N} integer;

# Decision variable X[i,j,k]: if digit k is assigned to row i and column j
var X{N,N,N} binary;

# Dummy integer variables for divisibility constraints
var dummy1  integer, >= 0;
var dummy2  integer, >= 0;
var dummy3  integer, >= 0;
var dummy4  integer, >= 0;
var dummy5  integer, >= 0;
var dummy6  integer, >= 0;
var dummy7  integer, >= 0;
var dummy8  integer, >= 0;
var dummy9  integer, >= 0;
var dummy10 integer, >= 0;
var dummy11 integer, >= 0;


#-------------#
# Constraints #
#-------------#

#
# Classic sudoku constraints
#

# Each digit appears once per row
subject to row{i in N, k in N}:
    sum{j in N} X[i, j, k] = 1;

# Each digit appears once per column
subject to column{j in N, k in N}:
    sum{i in N} X[i, j, k] = 1;

# Each digit appears once per subgrid
subject to subgrid{k in N, u in A, v in A}:
    sum{i in S, j in S} X[i+u, j+v, k] = 1;

# Only one digit per cell
subject to cell{i in N, j in N}:
    sum{k in N} X[i, j, k] = 1;

# Given digits must be respected
subject to given{i in N, j in N: G[i, j] <> 0}:
    X[i, j, G[i, j]] = 1;

#
# Divisibility constraints
#

# 2 divides 10, so we only need to check the last cell

subject to multiple_row2_left:
    sum{k in N} (X[2, 9, k] * k) = dummy1 * 2;

subject to multiple_row8_right:
    sum{k in N} (X[8, 1, k] * k) = dummy3 * 2;

subject to multiple_col3_up:
    sum{k in N} (X[9, 3, k] * k) = dummy2 * 2;


# 4, 8 and 125 divide 1000, so we only need to check the 3 last cells

subject to multiple_row3_left:
    sum{k in N, j in 7..9} (X[3, j, k] * k * 10^(9-j)) = dummy4 * 125;

subject to multiple_row8_left:
    sum{k in N, j in 7..9} (X[8, j, k] * k * 10^(9-j)) = dummy5 * 8;

subject to multiple_col1_up:
    sum{k in N, i in 7..9} (X[i, 1, k] * k * 10^(9-i)) = dummy6 * 4;

subject to multiple_col9_up:
    sum{k in N, i in 7..9} (X[i, 9, k] * k * 10^(9-i)) = dummy7 * 4;


# for all other values, every cell must be taken into account

subject to multiple_col6_up:
    sum{k in N, i in N} (X[i, 6, k] * k * 10^(9-i)) = dummy8 * 11;

subject to multiple_row1_right:
    sum{k in N, j in N} (X[1, j, k] * k * 10^(j-1)) = dummy9 * 22;

subject to multiple_col3_down:
    sum{k in N, i in N} (X[i, 3, k] * k * 10^(i-1)) = dummy10 * 17;

subject to multiple_col1_down:
    sum{k in N, i in N} (X[i, 1, k] * k * 10^(i-1)) = dummy11 * 257;


#------#
# Data #
#------#

data;

# The digits below were found by some unremarkable heuristics.
# We used the fact that the center subgrid was a magic square, together
# with the forward and backward divisibility of row 5 and column 7,
# to uniquely determine those values.
# G[1, 6] and G[3, 9] being equal to 5 followed from the simple observation
# that multiples of 5 end with either 5 or 0, from which only 5 is valid in sudoku.

# This was enough to speed up our integer program so it is now solvable in a couple of seconds.

param G default 0:
          1 2 3  4 5 6  7 8 9 :=
1         . . .  . . 5  7 . .
2         . . .  . . .  4 . .
3         . . .  . . .  1 . 5

4         . . .  4 9 2  6 . .
5         9 6 8  3 5 7  2 4 1
6         . . .  8 1 6  9 . .

7         . . .  . . .  8 . .
8         . . .  . . .  3 . .
9         . . .  . . .  5 . . ;


#-------#
# Solve #
#-------#

# Ensure integrality and deterministic results
option cplex_options "integrality=0 parallelmode=1";

solve;


#--------#
# Report #
#--------#

# Print solution

for {j in N}
    printf "----";
printf "-\n";

for {i in N} {
    printf "|";
    for {j in N} {
        for {k in N}
            if (X[i, j, k] == 1) then
                printf "%3d", k;
        if (j mod s == 0) then
            printf "  |";
    }
    printf "\n";
    if (i mod s == 0) then {
        for {j in N}
            printf "----";
        printf "-\n";
    }
}

