// codigo para cypher neo4j
/*
The Legend of Zelda: Breath of the Wild 2017
The Last of Us  2013
Mass Effect 2   2010
The Witcher III 3 Wild Hunt 2015
God of War  2018
Grand Theft Auto V  2013
Overwatch   2016
Red Dead Redemption 2018
Fortnite    2017
Bayonetta 2 2014
Cuphead 2017
Super Mario Odyssey 2017
BioShock Infinite   2013
Spider-Man  2018
Portal 2    2011
The Elder Scrolls V: Skyrim 2011
Minecraft   2011
Undertale   2015
Nier: Automata  2017
Outer Wilds 2019
Tales of Phantasia  1995
Hollow Knight   2017
Half-Life   1998
Left 4 Dead 2   2009
Bully   2006


*/
/* Desarrolladores de videojuegos 
    Nintendo EPD
    Naughty Dog
    BioWare
    CD Projekt Red
    Santa Monica Studio
    Rockstar North
    Blizzard Entertainment
    Rockstar Games
    Epic Games
    PlatinumGames
    StudioMDHR
    Nintendo EPD
    Ghost Story Games
    Insomniac Games
    Valve Corporation
    Bethesda Game Studios
    Mojang Studios
    Toby Fox
    PlatinumGames
    Mobius Digital

*/
/*Crear nodos para representar videojuegos con propiedades de nombre
y año de lanzamiento*/

CREATE (zelda:Game {name: 'The Legend of Zelda', year: 2017}) return zelda;
CREATE (lastofus:Game {name: 'The Last of Us', year: 2013}) return lastofus;
CREATE (masseffect:Game {name: 'Mass Effect 2', year: 2010}) return masseffect;
CREATE (witcher:Game {name: 'The Witcher III: Wild Hunt', year: 2015}) return witcher;
CREATE (godofwar:Game {name: 'God of War', year: 2018}) return godofwar;
CREATE (gta:Game {name: 'Grand Theft Auto V', year: 2013}) return gta;
CREATE (overwatch:Game {name: 'Overwatch', year: 2016}) return overwatch;
CREATE (reddead:Game {name: 'Red Dead Redemption', year: 2018}) return reddead;
CREATE (fortnite:Game {name: 'Fortnite', year: 2017}) return fortnite;
CREATE (bayonetta:Game {name: 'Bayonetta 2', year: 2014}) return bayonetta;
CREATE (cuphead:Game {name: 'Cuphead', year: 2017}) return cuphead;
CREATE (mario:Game {name: 'Super Mario Odyssey', year: 2017}) return mario;
CREATE (bioshock:Game {name: 'BioShock Infinite', year: 2013}) return bioshock;
CREATE (spiderman:Game {name: 'Spider-man', year: 2018}) return spiderman;
CREATE (portal:Game {name: 'Portal 2', year: 2011}) return portal;
CREATE (skyrim:Game {name: 'The Elder Scrolls V: Skyrim', year: 2011}) return skyrim;
CREATE (minecraft:Game {name: 'Minecraft', year: 2011}) return minecraft;
CREATE (undertale:Game {name: 'Undertale', year: 2015}) return undertale;
CREATE (nier:Game {name: 'Nier: Automata', year: 2017}) return nier;
CREATE (outerwilds:Game {name: 'Outer Wilds', year: 2019}) return outerwilds;
CREATE (tales:Game {name: 'Tales of Phantasia', year: 1995}) return tales;
CREATE (hollowknight:Game {name: 'Hollow Knight', year: 2017}) return hollowknight;
CREATE (halflife:Game {name: 'Half-Life', year: 1998}) return halflife;
CREATE (left4dead:Game {name: 'Left 4 Dead 2', year: 2009}) return left4dead;
CREATE (bully:Game {name: 'Bully', year: 2006}) return bully;
MATCH (G:Game) RETURN G;
/*Crear nodos para representar desarrolladores de videojuegos con propiedades de nombre*/
CREATE (nintendo:Developer {name: 'Nintendo EPD'}) return nintendo;
CREATE (naughtydog:Developer {name: 'Naughty Dog'}) return naughtydog;
CREATE (bioware:Developer {name: 'BioWare'}) return bioware;
CREATE (cdprojekt:Developer {name: 'CD Projekt Red'}) return cdprojekt;
CREATE (santamonica:Developer {name: 'Santa Monica Studio'}) return santamonica;
CREATE (rockstarnorth:Developer {name: 'Rockstar North'}) return rockstarnorth;
CREATE (blizzard:Developer {name: 'Blizzard Entertainment'}) return blizzard;
CREATE (rockstargames:Developer {name: 'Rockstar Games'}) return rockstargames;
CREATE (epicgames:Developer {name: 'Epic Games'}) return epicgames;
CREATE (platinumgames:Developer {name: 'PlatinumGames'}) return platinumgames;
CREATE (studioMDHR:Developer {name: 'StudioMDHR'}) return studioMDHR;
CREATE (ghoststory:Developer {name: 'Ghost Story Games'}) return ghoststory;
CREATE (insomniac:Developer {name: 'Insomniac Games'}) return insomniac;
CREATE (valve:Developer {name: 'Valve Corporation'}) return valve;
CREATE (bethesda:Developer {name: 'Bethesda Game Studios'}) return bethesda;
CREATE (mojang:Developer {name: 'Mojang Studios'}) return mojang;
CREATE (tobyfox:Developer {name: 'Toby Fox'}) return tobyfox;
CREATE (mobius:Developer {name: 'Mobius Digital'}) return mobius;
CREATE (namco:Developer {name: 'Namco'}) return namco;
CREATE (teamcherry:Developer {name: 'Team Cherry'}) return teamcherry;
MATCH (D:Developer) RETURN D;
/*Crear relaciones entre los nodos de videojuegos y desarrolladores*/
MATCH (zelda:Game {name: 'The Legend of Zelda'}), (nintendo:Developer {name: 'Nintendo EPD'})
CREATE (nintendo)-[:DEVELOPED]->(zelda) return nintendo, zelda;

MATCH (lastofus:Game {name: 'The Last of Us'}), (naughtydog:Developer {name: 'Naughty Dog'})
CREATE (naughtydog)-[:DEVELOPED]->(lastofus) return naughtydog, lastofus;

MATCH (masseffect:Game {name: 'Mass Effect 2'}), (bioware:Developer {name: 'BioWare'})
CREATE (bioware)-[:DEVELOPED]->(masseffect) return bioware, masseffect;

MATCH (witcher:Game {name: 'The Witcher III: Wild Hunt'}), (cdprojekt:Developer {name: 'CD Projekt Red'})
CREATE (cdprojekt)-[:DEVELOPED]->(witcher) return cdprojekt, witcher;

MATCH (godofwar:Game {name: 'God of War'}), (santamonica:Developer {name: 'Santa Monica Studio'})
CREATE (santamonica)-[:DEVELOPED]->(godofwar) return santamonica, godofwar;

MATCH (gta:Game {name: 'Grand Theft Auto V'}), (rockstarnorth:Developer {name: 'Rockstar North'})
CREATE (rockstarnorth)-[:DEVELOPED]->(gta) return rockstarnorth, gta;

MATCH (overwatch:Game {name: 'Overwatch'}), (blizzard:Developer {name: 'Blizzard Entertainment'})
CREATE (blizzard)-[:DEVELOPED]->(overwatch) return blizzard, overwatch;

MATCH (reddead:Game {name: 'Red Dead Redemption'}), (rockstargames:Developer {name: 'Rockstar Games'})
CREATE (rockstargames)-[:DEVELOPED]->(reddead) return rockstargames, reddead;

MATCH (fortnite:Game {name: 'Fortnite'}), (epicgames:Developer {name: 'Epic Games'})
CREATE (epicgames)-[:DEVELOPED]->(fortnite) return epicgames, fortnite;

MATCH (bayonetta:Game {name: 'Bayonetta 2'}), (platinumgames:Developer {name: 'PlatinumGames'})
CREATE (platinumgames)-[:DEVELOPED]->(bayonetta) return platinumgames, bayonetta;

MATCH (cuphead:Game {name: 'Cuphead'}), (studioMDHR:Developer {name: 'StudioMDHR'})
CREATE (studioMDHR)-[:DEVELOPED]->(cuphead) return studioMDHR, cuphead;

MATCH (mario:Game {name: 'Super Mario Odyssey'}), (nintendo:Developer {name: 'Nintendo EPD'})
CREATE (nintendo)-[:DEVELOPED]->(mario) return nintendo, mario;

MATCH (bioshock:Game {name: 'BioShock Infinite'}), (ghoststory:Developer {name: 'Ghost Story Games'})
CREATE (ghoststory)-[:DEVELOPED]->(bioshock) return ghoststory, bioshock;

MATCH (spiderman:Game {name: 'Spider-man'}), (insomniac:Developer {name: 'Insomniac Games'})
CREATE (insomniac)-[:DEVELOPED]->(spiderman) return insomniac, spiderman;

MATCH (portal:Game {name: 'Portal 2'}), (valve:Developer {name: 'Valve Corporation'})
CREATE (valve)-[:DEVELOPED]->(portal) return valve, portal;

MATCH (skyrim:Game {name: 'The Elder Scrolls V: Skyrim'}), (bethesda:Developer {name: 'Bethesda Game Studios'})
CREATE (bethesda)-[:DEVELOPED]->(skyrim) return bethesda, skyrim;

MATCH (minecraft:Game {name: 'Minecraft'}), (mojang:Developer {name: 'Mojang Studios'})
CREATE (mojang)-[:DEVELOPED]->(minecraft) return mojang, minecraft;

MATCH (undertale:Game {name: 'Undertale'}), (tobyfox:Developer {name: 'Toby Fox'})
CREATE (tobyfox)-[:DEVELOPED]->(undertale) return tobyfox, undertale;

MATCH (nier:Game {name: 'Nier: Automata'}), (platinumgames:Developer {name: 'PlatinumGames'})
CREATE (platinumgames)-[:DEVELOPED]->(nier) return platinumgames, nier;

MATCH (outerwilds:Game {name: 'Outer Wilds'}), (mobius:Developer {name: 'Mobius Digital'})
CREATE (mobius)-[:DEVELOPED]->(outerwilds) return mobius, outerwilds;

MATCH (tales:Game {name: 'Tales of Phantasia'}), (namco:Developer {name: 'Namco'})
CREATE (namco)-[:DEVELOPED]->(tales) return namco, tales;

MATCH (hollowknight:Game {name: 'Hollow Knight'}), (teamcherry:Developer {name: 'Team Cherry'})
CREATE (teamcherry)-[:DEVELOPED]->(hollowknight) return teamcherry, hollowknight;

MATCH (halflife:Game {name: 'Half-Life'}), (valve:Developer {name: 'Valve Corporation'})
CREATE (valve)-[:DEVELOPED]->(halflife) return valve, halflife;

MATCH (left4dead:Game {name: 'Left 4 Dead 2'}), (valve:Developer {name: 'Valve Corporation'})
CREATE (valve)-[:DEVELOPED]->(left4dead) return valve, left4dead;

MATCH (bully:Game {name: 'Bully'}), (rockstargames:Developer {name: 'Rockstar Games'})
CREATE (rockstargames)-[:DEVELOPED]->(bully) return rockstargames, bully;

MATCH (D:Developer)-[:DEVELOPED]->(G:Game) RETURN D, G;
/*Crear nodos para representar jugadores con propiedades de nombre
y país.*/

CREATE (player1:Player {name: 'Lucia Villar', country: 'Canada'}) return player1;
CREATE (player2:Player {name: 'Juan Perez', country: 'Mexico'}) return player2;
CREATE (player3:Player {name: 'Maria Lopez', country: 'Canada'}) return player3;
CREATE (player4:Player {name: 'John Doe', country: 'USA'}) return player4;
CREATE (player5:Player {name: 'Adam Quesada', country: 'Canada'}) return player5;

/* Crear relaciones para representar que jugadores juegan ciertos
juegos. */

MATCH (player1:Player {name: 'Lucia Villar'}), (zelda:Game {name: 'The Legend of Zelda'})
CREATE (player1)-[:PLAYS]->(zelda) return player1, zelda;

MATCH (player1:Player {name: 'Lucia Villar'}),(gta:Game {name: 'Grand Theft Auto V'})
CREATE (player1)-[:PLAYS]->(gta) return player1, gta;

MATCH (player1:Player {name: 'Lucia Villar'}),(cuphead:Game {name: 'Cuphead'})
CREATE (player1)-[:PLAYS]->(cuphead) return player1, cuphead;

MATCH (player1:Player {name: 'Lucia Villar'}),(skyrim:Game {name: 'The Elder Scrolls V: Skyrim'})
CREATE (player1)-[:PLAYS]->(skyrim) return player1, skyrim;

MATCH (player1:Player {name: 'Lucia Villar'}),(tales:Game {name: 'Tales of Phantasia'})
CREATE (player1)-[:PLAYS]->(tales) return player1, tales;

/*
MATCH (player1:Player {name: 'Lucia Villar'}),
      (zelda:Game {name: 'The Legend of Zelda: Breath of the Wild'}),
      (gta:Game {name: 'Grand Theft Auto V'}),
      (cuphead:Game {name: 'Cuphead'}),
      (skyrim:Game {name: 'The Elder Scrolls V: Skyrim'}),
      (tales:Game {name: 'Tales of Phantasia'})
CREATE (player1)-[:PLAYS]->(zelda),
       (player1)-[:PLAYS]->(gta),
       (player1)-[:PLAYS]->(cuphead),
       (player1)-[:PLAYS]->(skyrim),
       (player1)-[:PLAYS]->(tales)
RETURN player1, zelda, gta, cuphead, skyrim, tales;
*/


MATCH (player2:Player {name: 'Juan Perez'}), (lastofus:Game {name: 'The Last of Us'})
CREATE (player2)-[:PLAYS]->(lastofus) return player2, lastofus;

MATCH (player2:Player {name: 'Juan Perez'}),(overwatch:Game {name: 'Overwatch'})
CREATE (player2)-[:PLAYS]->(overwatch) return player2, overwatch;

MATCH (player2:Player {name: 'Juan Perez'}),(mario:Game {name: 'Super Mario Odyssey'})
CREATE (player2)-[:PLAYS]->(mario) return player2, mario;

MATCH (player2:Player {name: 'Juan Perez'}),(minecraft:Game {name: 'Minecraft'})
CREATE (player2)-[:PLAYS]->(minecraft) return player2, minecraft;

MATCH (player2:Player {name: 'Juan Perez'}),(hollowknight:Game {name: 'Hollow Knight'})
CREATE (player2)-[:PLAYS]->(hollowknight) return player2, hollowknight;

/* MATCH (player2:Player {name: 'Juan Perez'}),
      (lastofus:Game {name: 'The Last of Us'}),
      (overwatch:Game {name: 'Overwatch'}),
      (mario:Game {name: 'Super Mario Odyssey'}),
      (minecraft:Game {name: 'Minecraft'}),
      (hollowknight:Game {name: 'Hollow Knight'})
CREATE (player2)-[:PLAYS]->(lastofus),
       (player2)-[:PLAYS]->(overwatch),
       (player2)-[:PLAYS]->(mario),
       (player2)-[:PLAYS]->(minecraft),
       (player2)-[:PLAYS]->(hollowknight)
RETURN player2, lastofus, overwatch, mario, minecraft, hollowknight;
*/

MATCH (player3:Player {name: 'Maria Lopez'}), (masseffect:Game {name: 'Mass Effect 2'})
CREATE (player3)-[:PLAYS]->(masseffect) return player3, masseffect;

MATCH (player3:Player {name: 'Maria Lopez'}),(reddead:Game {name: 'Red Dead Redemption'})
CREATE (player3)-[:PLAYS]->(reddead) return player3, reddead;

MATCH (player3:Player {name: 'Maria Lopez'}),(bioshock:Game {name: 'BioShock Infinite'})
CREATE (player3)-[:PLAYS]->(bioshock) return player3, bioshock;

MATCH (player3:Player {name: 'Maria Lopez'}),(undertale:Game {name: 'Undertale'})
CREATE (player3)-[:PLAYS]->(undertale) return player3, undertale;

MATCH (player3:Player {name: 'Maria Lopez'}),(halflife:Game {name: 'Half-Life'})
CREATE (player3)-[:PLAYS]->(halflife) return player3, halflife;
/*
MATCH (player3:Player {name: 'Maria Lopez'}),
      (masseffect:Game {name: 'Mass Effect 2'}),
      (reddead:Game {name: 'Red Dead Redemption'}),
      (bioshock:Game {name: 'BioShock Infinite'}),
      (undertale:Game {name: 'Undertale'}),
      (halflife:Game {name: 'Half-Life'})
CREATE (player3)-[:PLAYS]->(masseffect),
       (player3)-[:PLAYS]->(reddead),
       (player3)-[:PLAYS]->(bioshock),
       (player3)-[:PLAYS]->(undertale),
       (player3)-[:PLAYS]->(halflife)
RETURN player3, masseffect, reddead, bioshock, undertale, halflife;
*/

MATCH (player4:Player {name: 'Bob'}), (witcher:Game {name: 'The Witcher III: Wild Hunt'})
CREATE (player4)-[:PLAYS]->(witcher) return player4, witcher;

MATCH (player4:Player {name: 'Bob'}),(fortnite:Game {name: 'Fortnite'})
CREATE (player4)-[:PLAYS]->(fortnite) return player4, fortnite;

MATCH (player4:Player {name: 'Bob'}),(spiderman:Game {name: 'Spider-man'})
CREATE (player4)-[:PLAYS]->(spiderman) return player4, spiderman;

MATCH (player4:Player {name: 'Bob'}),(nier:Game {name: 'Nier: Automata'})
CREATE (player4)-[:PLAYS]->(nier) return player4, nier;

MATCH (player4:Player {name: 'Bob'}),(left4dead:Game {name: 'Left 4 Dead 2'})
CREATE (player4)-[:PLAYS]->(left4dead) return player4, left4dead;

/*
MATCH (player4:Player {name: 'Bob'}),
      (witcher:Game {name: 'The Witcher III: Wild Hunt'}),
      (fortnite:Game {name: 'Fortnite'}),
      (spiderman:Game {name: 'Spider-man'}),
      (nier:Game {name: 'Nier: Automata'}),
      (left4dead:Game {name: 'Left 4 Dead 2'})
CREATE (player4)-[:PLAYS]->(witcher),
       (player4)-[:PLAYS]->(fortnite),
       (player4)-[:PLAYS]->(spiderman),
       (player4)-[:PLAYS]->(nier),
       (player4)-[:PLAYS]->(left4dead)
RETURN player4, witcher, fortnite, spiderman, nier, left4dead;
*/

MATCH (player5:Player {name: 'Alice'}), (godofwar:Game {name: 'God of War'})
CREATE (player5)-[:PLAYS]->(godofwar) return player5, godofwar;

MATCH (player5:Player {name: 'Alice'}),(bayonetta:Game {name: 'Bayonetta 2'})
CREATE (player5)-[:PLAYS]->(bayonetta) return player5, bayonetta;

MATCH (player5:Player {name: 'Alice'}),(portal:Game {name: 'Portal 2'})
CREATE (player5)-[:PLAYS]->(portal) return player5, portal;

MATCH (player5:Player {name: 'Alice'}),(outerwilds:Game {name: 'Outer Wilds'})
CREATE (player5)-[:PLAYS]->(outerwilds) return player5, outerwilds;

MATCH (player5:Player {name: 'Alice'}),(bully:Game {name: 'Bully'})
CREATE (player5)-[:PLAYS]->(bully) return player5, bully;

MATCH (player5:Player {name: 'Alice'}),(bully:Game {name: 'Minecraft})
CREATE (player5)-[:PLAYS]->(bully) return player5, bully;

/*
MATCH (player5:Player {name: 'Alice'}),
      (godofwar:Game {name: 'God of War'}),
      (bayonetta:Game {name: 'Bayonetta 2'}),
      (portal:Game {name: 'Portal 2'}),
      (outerwilds:Game {name: 'Outer Wilds'}),
      (bully:Game {name: 'Bully'})
      (minecraft:Game {name: 'Minecraft'})
CREATE (player5)-[:PLAYS]->(godofwar),
       (player5)-[:PLAYS]->(bayonetta),
       (player5)-[:PLAYS]->(portal),
       (player5)-[:PLAYS]->(outerwilds),
       (player5)-[:PLAYS]->(bully)
        (player5)-[:PLAYS]->(minecraft)
RETURN player5, godofwar, bayonetta, portal, outerwilds, bully;
*/

MATCH (P:Player)-[:PLAYS]->(G:Game) RETURN P, G;
MATCH (player:Player {name: 'Alice'})-[:PLAYS]->(game:Game)
RETURN game;
MATCH (player:Player)-[:PLAYS]->(minecraft:Game {name: 'Minecraft'})
RETURN player,minecraft;
MATCH (zelda:Game {name: 'The Legend of Zelda'})
SET zelda.year = 1987
RETURN zelda;
MATCH (n:Player {name: 'Bob'})
REMOVE n.country
RETURN n;
MATCH (developer:Developer)-[:DEVELOPED]->(game:Game)
RETURN developer.name AS Developer, COUNT(game) AS NumberOfGames
MATCH (player:Player)-[:PLAYS]->(game:Game)
WHERE player.country = 'Canada'
RETURN player.name AS Player, game.name AS Game
MATCH (game:Game)
WITH datetime().year - game.year AS gameAge
RETURN avg(gameAge) AS averageGameAge


/* Crear relaciones de amistad entre jugadores y encontrar juegos
jugados por grupos de amigos. */

MATCH (player1:Player {name: 'Lucia Villar'}), (player2:Player {name: 'Juan Perez'})
CREATE (player1)-[:FRIENDS]->(player2) return player1, player2;

MATCH (player1:Player {name: 'Lucia Villar'}), (player3:Player {name: 'Maria Lopez'})
CREATE (player1)-[:FRIENDS]->(player3) return player1, player3;

MATCH (player1:Player {name: 'Lucia Villar'}), (player4:Player {name: 'Bob'})
CREATE (player1)-[:FRIENDS]->(player4) return player1, player4;

MATCH (player1:Player {name: 'Lucia Villar'}), (player5:Player {name: 'Alice'})
CREATE (player1)-[:FRIENDS]->(player5) return player1, player5;

/*
MATCH (player1:Player {name: 'Lucia Villar'}),
      (player2:Player {name: 'Juan Perez'}),
      (player3:Player {name: 'Maria Lopez'}),
      (player4:Player {name: 'Bob'}),
      (player5:Player {name: 'Alice'})
CREATE (player1)-[:FRIENDS]->(player2),
       (player1)-[:FRIENDS]->(player3),
       (player1)-[:FRIENDS]->(player4),
       (player1)-[:FRIENDS]->(player5)
RETURN player1, player2, player3, player4, player5;
*/

MATCH (player1:Player {name: 'Lucia Villar'})-[:FRIENDS]->(player2:Player)
MATCH (player2)-[:PLAYS]->(game:Game)
RETURN player2, game;

MATCH (player:Player)-[:FRIENDS]->(friend:Player)
RETURN player, friend;

MATCH (player:Player)-[:FRIENDS]->(friend:Player)
MATCH (friend)-[:PLAYS]->(game:Game)
RETURN player, friend, game;


/* Identificar comunidades de jugadores que juegan los mismos juegos. */


