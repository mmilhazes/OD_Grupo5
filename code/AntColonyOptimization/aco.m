clc;
clear;
close all;

tic
%% Problem Definition

model = CreateModel_aco();

CostFunction = @(tour) TourLength(tour, model);

%num of nodes
nVar = 53;


%% ACO Parameters

MaxIt = 200;      % Maximum Number of Iterations

nAnt = 200;        % Number of Ants (Population Size)

Q = 1;

tau0 = 10*Q/(nVar*mean(model.D(:)));	% Initial Pheromone

alpha = 2;        % Pheromone Exponential Weight
beta = 5;         % Heuristic Exponential Weight

rho = 0.15;       % Evaporation Rate

nteste = 15;    %num of tests

BestSolT = zeros(nteste,1); %Best Solution of every test

AvgSolT = zeros(nteste,1);  %Average Solution of every test

WorstSolT = zeros(nteste,1);    %Worst Solution of every test

BestSolTourT = zeros(nteste,nVar); %Tour of Best solution of every test


for teste= 1:nteste
    
    %% Initialization

    eta = 1./model.D;             % Heuristic Information Matrix

    tau = tau0*ones(nVar, nVar);   % Pheromone Matrix

    BestCost = zeros(MaxIt, 1);    % Array to Hold Best Cost Values
    BestCostT = zeros(MaxIt+1, 1);  % Array to Hold Best Cost Values with initial cost
    BestCostT(1,1) = inf;   % initial cost (later is deleted)
    
    WorstCost = zeros(MaxIt, 1); % Array to Hold Worst Cost Values
    WorstCostT = zeros(MaxIt+1, 1); % Array to Hold Worst Cost Values with initial cost
    WorstCostT(1,1) = 0;    % initial cost (later is deleted)
    
    AvgSol = zeros(MaxIt,1); % Array to hold the average cost

    % Empty Ant
    empty_ant.Tour = [];
    empty_ant.Cost = [];

    % Ant Colony Matrix
    ant = repmat(empty_ant, nAnt, 1);

    % Best Ant
    BestSol.Cost = inf;

    %Worst Ant
    WorstSol.Cost = 0;

    AllCost = zeros(nAnt,1);    % Array with every ant solution
    
    Iter = zeros(MaxIt,1);  % Array with Iterations
    %% ACO Main Loop

        for it = 1:MaxIt
            Iter(it,1) = it; 
            
            % Move Ants
            for k = 1:nAnt

                ant(k).Tour = randi([1 nVar]);

                for l = 2:nVar

                    i = ant(k).Tour(end);

                    P = tau(i, :).^alpha.*eta(i, :).^beta;

                    P(ant(k).Tour) = 0;

                    P = P/sum(P);

                    j = RouletteWheelSelection(P);

                    ant(k).Tour = [ant(k).Tour j];

                end
                
                % Cost of ant k tour
                ant(k).Cost = CostFunction(ant(k).Tour);
                antcost = CostFunction(ant(k).Tour);
                
                % check best and worst solution
                if ant(k).Cost<BestSol.Cost
                    BestSol = ant(k);
                end

                if ant(k).Cost>WorstSol.Cost
                    WorstSol = ant(k);
                end
                
                % store cost
                AllCost(k,1) = antcost;
                
            end

            % Update Pheromones
            for k = 1:nAnt

                tour = ant(k).Tour;

                tour = [tour tour(1)]; %#ok

                for l = 1:nVar

                    i = tour(l);
                    j = tour(l+1);

                    tau(i, j) = tau(i, j)+Q/ant(k).Cost;

                end

            end

            % Evaporation
            tau = (1-rho)*tau;

            % Store Best Cost
            BestCost2(it) = BestSol.Cost;
            BestCost(it) = min(AllCost);
            
            if BestCost(it)<BestCostT(it)
                BestCostT(it+1) = BestCost(it);
            else
                BestCostT(it+1) = BestCostT(it);
            end
            
            
            %Store Worsrt cost
            WorstCost2(it) = WorstSol.Cost;
            WorstCost(it) = max(AllCost);
            
            if WorstCost(it)>WorstCostT(it)
                WorstCostT(it+1) = WorstCost(it);
            else
                WorstCostT(it+1) = WorstCostT(it);
            end

            % Store average solution
            AvgSol(it) = sum(AllCost)/nAnt;

        end

    disp(['Iteration ' num2str(it) ': Best Cost = ' num2str(BestCost(it))]);
    disp(['Iteration ' num2str(it) ': Worst Cost = ' num2str(WorstCost(it))]);
    disp(['Iteration ' num2str(it) ': Average Cost = ' num2str(AvgSol(it))]);
    %disp(BestSol.Tour);
    
    % Store solution of the test
    BestSolT(teste,1) = BestCost(MaxIt);
    BestSolTourT(teste,:)=BestSol.Tour;
    AvgSolT(teste,1) = AvgSol(MaxIt);
    WorstSolT(teste,1) = WorstCost(MaxIt);
    
    % delete first value
    BestCostT(BestCostT == inf) = [];
    WorstCostT(WorstCostT == 0) = [];
end

% Averages of each test, best indvidual solution and tour
AvgBestSol = sum(BestSolT)/nteste
AvgAvgSol = sum(AvgSolT)/nteste
AvgWorstSol = sum(WorstSolT)/nteste
BestSol = min(BestSolT)
BestSolTour = BestSolTourT(BestSolT == BestSol,:)

%% Results

%plot best and avg cost for a test
figure;
plot(Iter, BestCostT, 'b-', Iter, AvgSol, 'r-');
xlabel('Iteration');
ylabel('Cost');
legend('Best Solution','Average Solution');
grid on;

toc