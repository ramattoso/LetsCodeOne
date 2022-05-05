%%%% Exercício 3 - LetsCodeOne %%%%
n = input('\n Entre com o número de linhas: \n');
for i=1:n
    for j=1:n
        if i==j
            fprintf(' + ')
        else
            fprintf(' * ')
        end
    end
    fprintf('\n')
end