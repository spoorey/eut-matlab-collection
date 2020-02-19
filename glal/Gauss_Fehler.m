% Gauss-Fehlerfortpflanzung für eine beliebige Formel, bestehend aus
% Messwerten
% Autor: David Spörri
formel = input('Gib deine Formel ein:\n', 's');
formel = str2sym(formel);

vars = symvar(char(formel));

fehlers = '';
for i=1:length(vars)
    varname=vars(i);
    varname=char(varname(1));

    abl = char(diff(formel, varname));
    delta = strcat('delta_', varname, '^2');
    fehler = strcat('(((', abl, ')^2)*(', delta, '))');
    if (isempty(fehlers))
        fehlers = fehler;
    else
        fehlers = strcat(fehlers, ' + ', fehler);
    end
end


fehlers = str2sym(fehlers);
fehlers = simplify(fehlers);
fehlers = char(fehlers);
fehlers = strcat('sqrt(', fehlers, ')');
disp('Fehlerfortpflanzung: ');
disp(char(fehlers));
