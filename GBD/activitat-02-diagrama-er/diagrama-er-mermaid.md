```mermaid
erDiagram
    Personatge {
        string DNI PK "NOT NULL"
        string Nom "NOT NULL"
        string Cognom
        int Vida
        int Força
        int Agilitat
        string Carisma
    }
    Habilitat {
        int Codi PK "NOT NULL"
        string Nom "NOT NULL"
        int Cost
        int Dany
        int Cooldown
        string Tipus "NOT NULL"
    }
    Item {
        int Codi PK "NOT NULL"
        string Nom "NOT NULL"
        int Equipable
        int Comerciable "NOT NULL"
        string Tipus
        int Pes "NOT NULL"
        string Qualitat "NOT NULL"
        float MesuraX "NOT NULL"  
        float MesuraY "NOT NULL"
        float MesuraZ "NOT NULL"
    }
    Mascota {
        int Num.Chip PK "NOT NULL"
        string Nom "NOT NULL"
        int Motxilla
    }
    Enemic {
        int Codi PK "NOT NULL"
        string Nom "NOT NULL"
        string Tipus "NOT NULL"
        int Nivell "NOT NULL"
        int Vida
        int Força
        int Agilitat
        string Carisma
    }
    Habilitat }o--o{ Habilitat : combina__amb
    Personatge }o--o{ Habilitat : poseeix
    Personatge }o--o{ Item : equipa
    Personatge ||--|| Mascota : acompanya
    Mascota ||--|| Item : carrega
    Enemic }o--o{ Habilitat : enfrenta
    Personatge }o--o{ Enemic : enfrenta
```
