(define (domain solitaire)
(:requirements :strips)
(:predicates (Full ?i) (Straight-line ?l ?m ?n))
(:action Move-Ahead
:parameters (?l ?m ?n)
:precondition (and (Full ?l) (Full ?m) (not (Full ?n)) (Straight-line ?l ?m ?n) )
:effect (and (not (Full ?l)) (not (Full ?m))  (Full ?n) ))
(:action Move-Behind
:parameters (?l ?m ?n)
:precondition (and (Full ?n) (Full ?m) (not (Full ?l)) (Straight-line ?l ?m ?n) )
:effect (and (not (Full ?n)) (not (Full ?m))  (Full ?l) ))

)
