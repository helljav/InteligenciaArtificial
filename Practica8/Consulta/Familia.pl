% En padre, madre, y pariente,
% el primer argummento es el padre/madre y el segundo argumento es el hijo.

padre(michael, cathy).
padre(michael, sharon).
padre(charles, michael).
padre(charles, julie).
padre(jim, melody).
padre(jim, crystal).
padre(elmo, jim).
padre(greg, stephanie).
padre(greg, danielle).
padre(xavier, andrea).
padre(joaquin, xavier).
padre(miguel, trini).

madre(melody, cathy).
madre(melody, sharon).
madre(hazel, michael).
madre(hazel, julie).
madre(eleanor, melody).
madre(eleanor, crystal).
madre(crystal, stephanie).
madre(crystal, danielle).
madre(trini, andrea).
madre(pilar, xavier).
madre(montse, trini).

pariente(X, Y) :- padre(X, Y).
pariente(X, Y) :- madre(X, Y).

hermanos(X,Y) :- madre(Z,X), madre(Z,Y), X \= Y.

abuelo(X, Z) :- padre(X, Y), pariente(Y, Z).
abuela(X, Z) :- madre(X, Y), pariente(Y, Z).

bisabuelo(X,Z) :- padre(X,Y1), pariente(Y1,Y2), pariente(Y2,Z).
bisabuelo(X,Z) :- madre(X,Y1), pariente(Y1,Y2), pariente(Y2,Z).
