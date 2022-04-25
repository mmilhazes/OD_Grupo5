function model = CreateModel()

    % read input table and create the model, either 'matrix_53.csv' or 'matrix_100.csv'. By
    % changing the input table, nVar in aco.m should match the number of
    % nodes
    n = 53;
    D = readtable('matrix_53.csv');
    D = table2array(D);
    
    model.n = n;
    model.D = D;
    
end