create table Utilisateur (
    idUtilisateur int not null auto_increment,
    nom varchar(255) not null,
    prenom varchar(255) not null,
    email varchar(255) not null,
    motDePasse varchar(255) not null,
    primary key (idUtilisateur)
);

create table CategorieAnime (
    idCategorie int not null auto_increment,
    nom varchar(255) not null,
    primary key (idCategorie)
);

create table Anime (
    idAnime int not null auto_increment,
    nom varchar(255) not null,
    resumeAnime varchar(3000) not null,
    idCategorie int not null,
    primary key (idAnime),
    foreign key (idCategorie) references CategorieAnime(idCategorie)
);

create table Episode (
    idEpisode int not null auto_increment,
    nom varchar(255) not null,
    numeroEpisode int not null,
    idAnime int not null,
    lienEpisode varchar(255) not null,
    primary key (idEpisode),
    foreign key (idAnime) references Anime(idAnime)
);

