% Prolog File
animal(aguila,carnivoro).
animal(anaconda,carnivoro)
animal(leopardo,carnivoro).
animal(arana,carnivoro).
animal(lobo,carnivoro).
animal(boa,carnivoro).	
animal(buho,carnivoro).	
animal(murcielago,carnivoro).
aniamal(caiman,carnivoro).
animal(orca,carnivoro).
animal(calamar,carnivoro).
animal(oso,carnivoro).
animal(tigre,carnivoro).
animal(pantera,carnivoro).
animal(cocodrilo,carnivoro).
animal(pelicano,carnivoro).
animal(hiena,carnivoro).
animal(tiburon,carnivoro).
animal(zorro,carnivoro).


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


plantaComestible(hiervabuena).
plantaComestible(alfalfa).
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
plantaComestible(albahaca).
plantaComestible(dienteDeLeon).
plantaComestible(perejil).
plantaComestible(verdolaga).
plantaComestible(trebolRojo).
plantaComestible(romero).


animal(avestruz, omnivoro).
animal(cerdo, omnivoro).
animal(chimpance, omnivoro).
animal(coati, omnivoro).
animal(cuervo, omnivoro).
animal(erizo, omnivoro).
animal(gallina, omnivoro).
animal(nandu, omnivoro).
animal(oso, omnivoro).
animal(pirana, omnivoro).
animal(roedor, omnivoro).
animal(humano, omnivoro).
animal(urraca, omnivoro).
animal(ardilla, omnivoro).
animal(mapache,omnivoro).
animal(raton,omnivoro).




come(X,Y):- animal(X,carnivoro), animal(Y,hervivoro); 
			animal(X, carnivoro), animal(Y,carnivoro), X\=Y;
			animal(X, carnivoro), animal(Y,omnivoro), X\=Y;
			animal(X, omnivoro), animal(Y,omnivoro), X\=Y;
			animal(X, omnivoro), animal(Y,carnivoro), X\=Y;
			animal(X, omnivoro), plantaComestible(Y);
			animal(X, herviboro),plantaComestible(Y).
			
