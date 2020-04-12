CREATE TABLE PrimeraEtapa (
    Folio int (10),
    Origen varchar (50),
    Polisa int (10),
    Lista int (10),
    Deudor varchar (50),
    Direccion varchar (90),
    Municipio varchar (30),
    Adeudo int (7),
    Pago int (7),
    AdeudoPc int (7),
    FSuscrip varchar (20),
    FPago varchar(20),
    Interes10 int (14),
    Interes3 int (14),
    AdeMInte10 int (14),
    AdeMInte3 int (14)
);

CREATE TABLE SegundaEtapa (
    ExpedJudicial varchar (50),
    Admite varchar (1),
    FechaRequerimiento varchar (20),
    Cedula varchar (1),
    Oposicion varchar (1),
    ComenOposicion varchar (90),
    CitaFP varchar (20),
    Oficio varchar (1),
    Embargo int (4),
    ComenEmbargo varchar (90),
    Emplazado varchar (1),
    Dinero int (7)
);

CREATE TABLE TerceraEtapa (
    Contesta varchar (1),
    Rebeldia varchar (1),
    Terceria varchar (1),
    Audiencia varchar (20),
    Sentencia varchar (90),
    Incidente varchar (1)
);

alter table PrimeraEtapa
    add constraint Pk_Folio
primary key (Folio);
