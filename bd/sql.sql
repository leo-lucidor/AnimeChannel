create table Utilisateur (
    idUtilisateur int not null auto_increment,
    nom varchar(255) not null,
    prenom varchar(255) not null,
    email varchar(255) not null unique,
    motDePasse varchar(255) not null,
    primary key (idUtilisateur)
);

create table CategorieAnime (
    idCategorie int not null auto_increment,
    nomC varchar(255) not null,
    primary key (idCategorie)
);

create table Anime (
    idAnime int not null auto_increment,
    nomA varchar(255) not null,
    resumeAnime varchar(3000) not null,
    idCategorie int not null,
    primary key (idAnime),
    foreign key (idCategorie) references CategorieAnime(idCategorie)
);

create table Episode (
    idEpisode int not null auto_increment,
    nomE varchar(255) not null,
    numeroEpisode int not null,
    idAnime int not null,
    lienEpisode varchar(255) not null,
    primary key (idEpisode),
    foreign key (idAnime) references Anime(idAnime)
);

insert into CategorieAnime (nom) values ('Isekai');
insert into CategorieAnime (nom) values ('Shonen');
insert into CategorieAnime (nom) values ('Shojo');
insert into CategorieAnime (nom) values ('Seinen');
insert into CategorieAnime (nom) values ('Josei');
insert into CategorieAnime (nom) values ('Kodomo');
insert into CategorieAnime (nom) values ('Ecchi');
insert into CategorieAnime (nom) values ('Harem');
insert into CategorieAnime (nom) values ('Yaoi');
insert into CategorieAnime (nom) values ('Yuri');
insert into CategorieAnime (nom) values ('Mecha');


insert into Anime (nomA, resumeAnime, idCategorie) values ('Re:Zero kara Hajimeru Isekai Seikatsu', 'Subaru Natsuki est un lycéen qui a été invoqué dans un autre monde. Alors qu''il se promenait dans la ville, Subaru est soudainement aspiré dans un monde parallèle. Sans avertissement, une boule de lumière l''entraîne dans un autre monde où il est accueilli par une fille aux cheveux argentés. La fille se présente comme Satella, et elle est venue chercher un insigne volé par un voleur. Lorsque Subaru et Satella sont attaqués par des bandits, Subaru découvre qu''il a le pouvoir de remonter le temps et de revenir à un point de sauvegarde précédent. Le problème, c''est qu''il est le seul à se souvenir de ce qui s''est passé dans le passé, et personne d''autre ne semble remarquer que le temps a été remonté.', 1);

insert into Episode (nomE, numeroEpisode, idAnime, lienEpisode) values ('Re:Zero kara Hajimeru Isekai Seikatsu', 1, 1, 'https://streamtape.com/e/m7b0BmOZZVCbbdZ/');
insert into Episode (nomE, numeroEpisode, idAnime, lienEpisode) values ('Re:Zero kara Hajimeru Isekai Seikatsu', 2, 1, 'https://streamtape.com/e/m7b0BmOZZVCbbdZ/');
insert into Episode (nomE, numeroEpisode, idAnime, lienEpisode) values ('Re:Zero kara Hajimeru Isekai Seikatsu', 3, 1, 'https://streamtape.com/e/m7b0BmOZZVCbbdZ/');