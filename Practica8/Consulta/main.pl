
:-consult('movies.txt').
	
/**********************************/
/*********** CONSULTAR *************/
/**********************************/

%Info de Pelicula	
infoMovie(M):-
	movie(M,Y),
	director(M,D),
	findall((A1,R1),actor(M,A1,R1),Actores),
	findall((A2,R2),actress(M,A2,R2),Actrices),
	nl,
	write('Pelicula: '),
	write(M),
	nl,
	write('Anio: '),
	write(Y),
	nl,
	write('Director: '),
	write(D),
	nl,
	write('Actores: '),
	write(Actores),
	nl,
	write('Actrices: '),
	write(Actrices).
	
	
/*********************************/
/*********** AGREGAR *************/
/*********************************/
		
%Agregar Pelicula
addMovie(P,Y):-
	assert(movie(P,Y)).
	

/***********************************/
/*********** MODIFICAR *************/
/***********************************/

%Modificar Pelicula
updateMovie(M1,M2,Y1,Y2):-
	
	movie(M1,Y1),
	findall(D,director(M1,D),Directores),
	findall((A1,P1),actor(M1,A1,P1),Actores),
	findall((A2,P2),actress(M1,A2,P2),Actrices),
	
	% Elimina dependencias
	retract(movie(M1,Y1)),
	retractall(director(M1,_)),
	retractall(actor(M1,_,_)),
	retractall(actress(M1,_,_)),

	% Crea nuevas dependencias
	assert(movie(M2,Y2)),
	(member(X,Directores),assert(director(M2,X)),fail;true),
	(member((A,R),Actores),assert(actor(M2,A,R)),fail;true),
	(member((A,R),Actrices),assert(actress(M2,A,R)),fail;true).

/**********************************/
/*********** ELIMINAR *************/
/**********************************/

%Eliminar Pelicula
deleteMovie(M,Y):-
	retract(movie(M,Y)),
	retractall(director(M,_)),
	retractall(actor(M,_,_)),
	retractall(actress(M,_,_)).


/***************/
/**** OTROS ****/
/***************/
	
%Guardar Estado	
guardaEstado():-
	open('movies.txt',write,S),
	set_output(S),
	listing(movie/2),
	listing(director/2),
	listing(actor/3),
	listing(actress/3),
	nl(S),
	close(S).

%customQuery
customQuery(C):-
	C,
	write(C),nl,
	fail;true.
	
%member para pruebas	
member(X,[X|Xs]).
member(X,[Y|Xs]):-member(X,Xs).