algorithm stable_matching is
    Initialize m ∈ M and w ∈ W to free
    while ∃ free man m who has a woman w to propose to do
        w := first woman on m's list to whom m has not yet proposed
        if ∃ some pair (m', w) then
            if w prefers m to m' then
                m' becomes free
                (m, w) become engaged
            end if
        else
            (m, w) become engaged
        end if
    repeat