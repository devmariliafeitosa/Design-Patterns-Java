package builder.builder;

// Importa os produtos que cada builder pode retornar
import builder.product.House;
import builder.product.HouseManual;

public interface HouseBuilder {
    // 1. Reinicia o Builder para criar um novo produto.
    void reset(); 

    // Etapas de construção comuns
    void buildWalls(int number);
    void buildDoors(int number);
    void buildWindows(int number);
    void buildRoof();
    
    // Etapas opcionais/extensões
    void buildGarage();
    void buildGarden();

    // 2. Retorna o produto final (pode ser House ou HouseManual)
    // O retorno é genérico (Object), mas em Java moderno, usaríamos generics
    // Para simplificar, vamos retornar House/HouseManual diretamente nas concretas.
    House getHouseResult(); 
    HouseManual getManualResult();
}