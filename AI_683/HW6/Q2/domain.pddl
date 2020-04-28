(define (domain tower-of-hanoi2)
(:requirements :strips)
(:predicates (Top ?i) (Disk-On ?j ?k) (Valid-Placement ?l ?m))
(:action Move
:parameters (?disc ?From ?To)
:precondition (and (Top ?disc) (Top ?To) (Valid-Placement ?To ?disc) (Disk-On ?disc ?From))
:effect (and (Disk-On ?disc ?To) (Top ?From) (not (Top ?To)) (not (Disk-On ?disc ?From)) ))
)