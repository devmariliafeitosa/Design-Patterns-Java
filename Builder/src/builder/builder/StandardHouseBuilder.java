package builder.builder;

import builder.product.House;
import builder.product.HouseManual; // Importa para o método getManualResult

// Constrói o objeto House
public class StandardHouseBuilder implements HouseBuilder {
    private House house;

    public StandardHouseBuilder() {
        this.reset();
    }

    // Método que reinicia o produto complexo
    @Override
    public void reset() {
        this.house = new House();
    }

    @Override
    public void buildWalls(int number) {
        this.house.add("Construção de " + number + " paredes de tijolo.");
    }

    @Override
    public void buildDoors(int number) {
        this.house.add("Instalação de " + number + " portas de segurança.");
    }

    @Override
    public void buildWindows(int number) {
        this.house.add("Instalação de " + number + " janelas de vidro duplo.");
    }

    @Override
    public void buildRoof() {
        this.house.add("Construção de telhado com telhas cerâmicas.");
    }
    
    // Etapa Opcional
    @Override
    public void buildGarage() {
        this.house.add("Construção de Garagem anexa.");
    }
    
    // Etapa Opcional
    @Override
    public void buildGarden() {
        this.house.add("Criação de Jardim frontal.");
    }

    // Retorna o produto House e reseta o builder para iniciar uma nova construção
    @Override
    public House getHouseResult() {
        House product = this.house;
        this.reset(); // Limpa o builder após retornar o produto
        return product;
    }
    
    // Retorna o produto HouseManual (neste caso, retorna null pois ele constrói a House)
    @Override 
    public HouseManual getManualResult() { 
        return null; 
    }
}