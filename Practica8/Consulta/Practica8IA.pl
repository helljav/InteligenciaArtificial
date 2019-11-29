%Animales carnivoros
animal(perro, carnivoro).
animal(aguila, carnivoro).
animal(buitre, carnivoro).
animal(cocodrilo, carnivoro).
animal(coyote, carnivoro).
animal(delfin, carnivoro).
animal(foca, carnivoro).
animal(harpia, carnivoro).
animal(hiena, carnivoro).
animal(leon, carnivoro).
animal(lobo, carnivoro).
animal(mapache, carnivoro).
animal(pelicano, carnivoro).
animal(pinguino, carnivoro).
animal(puma, carnivoro).
animal(serpiente, carnivoro).
animal(tiburon, carnivoro).
animal(tigre, carnivoro).
animal(araña, carnivoro).
animal(zorro, carnivoro).

%Animales Herbivoros
animal(conejo, herbivoro).
animal(caballo, herbivoro).
animal(cabra, herbivoro).
animal(canguro, herbivoro).
animal(cebra, herbivoro).
animal(ciervo, herbivoro).
animal(conejo, herbivoro).
animal(chinchilla, herbivoro).
animal(elefante, herbivoro).
animal(gacela, herbivoro).
animal(jirafa, herbivoro).
animal(koala, herbivoro).
animal(oruga, herbivoro).
animal(panda, herbivoro).
animal(oveja, herbivoro).
animal(rinoceronte, herbivoro).
animal(vaca, herbivoro).
animal(antilope, herbivoro).
animal(llama, herbivoro).
animal(tapir, herbivoro).

%Animales Omnivoros
animal(avestruz, omnivoro).
animal(cerdo, omnivoro).
animal(chimpance, omnivoro).
animal(coati, omnivoro).
animal(cuervo, omnivoro).
animal(erizo, omnivoro).
animal(gallina, omnivoro).
animal(ñandu, omnivoro).
animal(oso, omnivoro).
animal(piraña, omnivoro).
animal(roedor, omnivoro).
animal(humano, omnivoro).
animal(urraca, omnivoro).
animal(ardilla, omnivoro).

%Plantas Comestibles
plantaComestible(albahaca).
plantaComestible(dienteDeLeon).
plantaComestible(perejil).
plantaComestible(verdolaga).
plantaComestible(trebolRojo).
plantaComestible(romero).
plantaComestible(salvia).
plantaComestible(tomillo).
plantaComestible(menta).
plantaComestible(espinaca).
plantaComestible(achicoria).
plantaComestible(acelga).
plantaComestible(lechuga).
plantaComestible(esparragos).
plantaComestible(ortiga).
plantaComestible(arbolDeJudea).
plantaComestible(cebollino).
plantaComestible(calendula).
plantaComestible(savila).
plantaComestible(nopal).

%Reglas
come(X,Y) :- animal(X, carnivoro), animal(Y, herbivoro);%Carnivoro puede comer cualquier animal
			animal(X, carnivoro), animal(Y, omnivoro);
			animal(X, carnivoro), animal(Y, carnivoro) , X \= Y;
			animal(X, herbivoro), plantaComestible(Y);%Herbivoro>Planta
			animal(X, omnivoro), animal(Y, carnivoro);%Omnivoro puede comer cualquiera solo si es mas fuerte
			animal(X, omnivoro), animal(Y, herbivoro);
			animal(X, omnivoro), plantaComestible(Y).
			