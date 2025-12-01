package builder.director;

import builder.builder.HouseBuilder;

// O Director define a ordem de construção.
public class Director {

    // Define uma configuração básica de construção
    public void constructSimpleHouse(HouseBuilder builder) {
        builder.reset();
        builder.buildWalls(4);
        builder.buildDoors(1);
        builder.buildWindows(2);
        builder.buildRoof();
    }

    // Define uma configuração de construção complexa
    public void constructLuxuryHouse(HouseBuilder builder) {
        builder.reset();
        builder.buildWalls(6);
        builder.buildDoors(3);
        builder.buildWindows(8);
        builder.buildRoof();
        builder.buildGarage(); // Adiciona extras
        builder.buildGarden();
    }
    
    // Opcional: permite mudar o builder em tempo de execução
    private HouseBuilder builder;
    public void changeBuilder(HouseBuilder builder) {
        this.builder = builder;
    }
}