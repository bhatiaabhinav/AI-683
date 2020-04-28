(define (problem 15-peg-solitaire)
(:domain solitaire)
(:objects S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11 S12 S13 S14 S15)
(:init
(not (Full S1)) (Full S2) (Full S3) (Full S4) (Full S5) (Full S6) (Full S7) (Full S8) (Full S9) (Full S10) (Full S11) (Full S12) (Full S13) (Full S14) (Full S15)
(Straight-line S1 S2 S4) (Straight-line S2 S4 S7) (Straight-line S4 S7 S11) (Straight-line S1 S3 S6) (Straight-line S3 S6 S10) (Straight-line S6 S10 S15) 
(Straight-line S11 S12 S13) (Straight-line S12 S13 S14) (Straight-line S13 S14 S15) (Straight-line S2 S5 S9) (Straight-line S5 S9 S14) (Straight-line S3 S5 S8) 
(Straight-line S5 S8 S12) (Straight-line S7 S8 S9) (Straight-line S8 S9 S10) (Straight-line S4 S8 S13)(Straight-line S6 S9 S13) (Straight-line S4 S5 S6) )

(:goal (and (Full S1) (not (Full S2)) (not (Full S3)) (not (Full S4)) (not (Full S5)) (not (Full S6)) (not (Full S7)) (not (Full S8)) (not (Full S9)) (not (Full S10)) (not (Full S11)) (not (Full S12)) (not (Full S13)) (not (Full S14)) (not (Full S15))
))
)