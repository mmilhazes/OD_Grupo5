function j = RouletteWheelSelection(P)
%random number generator

    r = rand;
    
    C = cumsum(P);
    
    j = find(r <= C, 1, 'first');

end