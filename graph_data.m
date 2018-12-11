
%paths:
AVL1Path = fullfile('Performance','performanceAvl1.txt');
AVL2Path = fullfile('Performance','performanceAvl2.txt');
Dic1Path = fullfile('Performance','performanceDic1.txt');
Dic2Path = fullfile('Performance','performanceDic2.txt');

%graph limits:
plotLimits = [-Inf Inf -0.1 Inf];

figure

AVL1ID = fopen(AVL1Path);
Dic1ID = fopen(Dic1Path);
AVL1Scan = textscan(AVL1ID,'%u %f');
Dic1Scan = textscan(Dic1ID, '%u %f');
fclose(AVL1ID);
fclose(Dic1ID);
plot(AVL1Scan{1},AVL1Scan{2},Dic1Scan{1},Dic1Scan{2},'--')
title('AVLLinkedList vs Python Dictionary: delete.');
xlabel('N: number of elements.');
ylabel('Time: seconds.');
axis(plotLimits);

figure

AVL2ID = fopen(AVL2Path);
Dic2ID = fopen(Dic2Path);
AVL2Scan = textscan(AVL2ID,'%u %f');
Dic2Scan = textscan(Dic2ID, '%u %f');
fclose(AVL2ID);
fclose(Dic2ID);
plot(AVL2Scan{1},AVL2Scan{2},Dic2Scan{1},Dic2Scan{2},'--')
title('AVLLinkedList vs Python Dictionary: find.');
xlabel('N: number of elements.');
ylabel('Time: seconds.');
axis(plotLimits);

