% Sintomas
sintomade(cansancio,rinitis).
sintomade(tos,rinitis).
sintomade(dolorcabeza,rinitis).
sintomade(secrecion,rinitis).


sintomade(escalofrios,gripe).
sintomade(tos, gripe). %la tos es síntoma de gripe
sintomade(cansancio, gripe). %el cansancio es síntoma de gripe
sintomade(fiebre, gripe). %la fiebre es síntoma de gripe
sintomade(dolorcabeza, gripe). %dolor de cabeza es síntoma de gripe
sintomade(secrecion, gripe).


sintomade(cansancio,diabetes).
sintomade(debilidad,diabetes).
sintomade(dolorarticulaciones,diabetes).


sintomade(apatia,hipotiroidismo).
sintomade(cansancio,hipotiroidismo).
sintomade(dolorarticulaciones,hipotiroidismo).

sintomade(cansancio,anemia).
sintomade(debilidad,anemia).

sintomade(cansancio,obesidad).
sintomade(apatia,obesidad).
sintomade(dolorarticulaciones,obesidad).

%Especialidades

especialistade(otorrinolaringologo, gripe).
especialistade(otorrinolaringologo, rinitis).

especialistade(endocrinologo, diabetes).
especialistade(endocrinologo, hipotiroidismmo).

especialistade(nutriologo, anemia).
especialistade(nutriologo, obesidad).

especialistade(medicogeneral, gripe).
especialistade(medicogenral, anemia).

%Consultas
%buscar([Sint],Enf,1,Esp):-sintomade(Sint,Enf),especialistade(Esp,Enf).
%buscar([Sint|Ls],Enf,Cant,Esp) :- sintomade(Sint,Enf),especialistade(Esp,Enf),buscar(Ls,Enf,T,Esp), Cant is T+1.

buscar([],Enf,0,Esp).
buscar(Sint,Enf,1,Esp):-sintomade(Sint,Enf),especialistade(Esp,Enf).
buscar([Sint],Enf,1,Esp):-sintomade(Sint,Enf),especialistade(Esp,Enf).
buscar([Sint|Ls],Enf,Cant,Esp) :-sintomade(Sint,Enf),especialistade(Esp,Enf), buscar(Sint ,Enf, S1, Esp),buscar(Ls,Enf2,S2,Esp2), Cant is S1+S2.






