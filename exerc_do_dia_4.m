%Exercício do dia 05/05 - LetsCodeOne%

clc; clear;

nome = input('\n Entre com o nome do atleta: \n', 's');
primeiro_salto = input('\n Entre com a distância do primeiro salto em metros: \n');
segundo_salto = input('\n Entre com a distância do segundo salto em metros: \n');
terceiro_salto = input('\n Entre com a distância do terceiro salto em metros: \n');
quarto_salto = input('\n Entre com a distância do quarto salto em metros: \n');
quinto_salto = input('\n Entre com a distância do quinto salto em metros: \n');

%ordenar saltos%
saltos = [primeiro_salto,segundo_salto,terceiro_salto,quarto_salto,quinto_salto];
melhor = primeiro_salto;
pior = primeiro_salto;

for i=2:5
    if(melhor < saltos(i))
        melhor = saltos(i);
    end
    if(pior > saltos(i))
        pior = saltos(i);
    end
end

%calculando média
soma = 0;
for i=1:5
    soma=soma+saltos(i);
end
soma = soma - (melhor+pior);
media = soma/3;

fprintf('Atleta: %s \n',nome);
fprintf('Primeiro Salto: %.2d \n ',primeiro_salto,' m');
fprintf('Segundo Salto: %.2d \n ',segundo_salto,' m');
fprintf('Terceiro Salto: %.2d \n ',terceiro_salto,' m');
fprintf('Quarto Salto: %.2d \n ',quarto_salto,' m');
fprintf('Quinto Salto: %.2d \n ',quinto_salto,' m');

fprintf('Melhor Salto: %.2d \n ', melhor,' m');
fprintf('Pior Salto: %.2d \n ', pior,' m');
fprintf('Média dos demais saltos: %.2d \n ', media,' m');

fprintf('Resultado Final: \n')
fprintf(nome,'%s: ',media,' %.2d m')