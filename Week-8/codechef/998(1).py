"""Explanation:
Example case 1: The total time given to both clocks after 1010 turns is 2⋅(180+10)=3802⋅(180+10)=380 seconds. 
The total time left at the end is 0+2=20+2=2 seconds. The duration of the game is 380−2=378380−2=378 seconds.
Example case 3: The total time given to both clocks after 1212 turns is 2⋅(180+12)=3842⋅(180+12)=384 seconds. 
The total time left at the end is 192+192=384192+192=384 seconds. The duration of the game is 384−384=0384−384=0 seconds."""
for T in range(0, int(input())):
    N, A, B = input().split()
    N, A, B = int(N), int(A), int(B)
    totaltime = 2 * (180 + N)
    timeleft = A + B
    duration_of_game = totaltime - timeleft
    print(duration_of_game)
