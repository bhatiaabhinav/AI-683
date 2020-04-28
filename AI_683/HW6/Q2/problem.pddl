
(define (problem hanoi3)
(:domain tower-of-hanoi2)
(:objects A B C D1 D2 D3)
(:init
(Top B) (Top C) (Top D1)
(Valid-Placement D2 D1) (Valid-Placement D3 D1) (Valid-Placement D3 D2) 
(Valid-Placement A D1) (Valid-Placement A D2) (Valid-Placement A D3) 
(Valid-Placement B D1) (Valid-Placement B D2) (Valid-Placement B D3) 
(Valid-Placement C D1) (Valid-Placement C D2) (Valid-Placement C D3) 
(Disk-On D3 A)  (Disk-On D2 D3) (Disk-On D1 D2))
(:goal (and (Disk-On D3 C)  (Disk-On D2 D3) (Disk-On D1 D2)))
)