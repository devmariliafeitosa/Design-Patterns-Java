package builder.director;

import builder.builder.StandardHouseBuilder;
import builder.product.House;

public class Main {
    public static void main(String[] args) {
        // 1. Criar o Director e o Builder Concreto
        Director director = new Director();
        StandardHouseBuilder builder = new StandardHouseBuilder();
        
        // Atribui o Builder ao Director
        // O Director agora pode construir qualquer coisa com este Builder
        // (Isso é opcional, mas facilita a reutilização de sequências)
        // director.changeBuilder(builder); 

        // 2. Construção da Casa Simples
        System.out.println("Construindo uma Casa Simples...");
        director.constructSimpleHouse(builder);
        
        // 3. Obter o Produto Final (House)
        House simpleHouse = builder.getHouseResult();
        simpleHouse.show();


        // 4. Construção da Casa de Luxo
        System.out.println("\nConstruindo uma Casa de Luxo...");
        director.constructLuxuryHouse(builder);
        
        // 5. Obter o Segundo Produto Final (House)
        House luxuryHouse = builder.getHouseResult();
        luxuryHouse.show();
        
        // 6. Construção Customizada (Sem o Director)
        System.out.println("\nConstrução Customizada (Apenas Walls e Roof)...");
        builder.reset();
        builder.buildWalls(10);
        builder.buildRoof();
        House customHouse = builder.getHouseResult();
        customHouse.show();
    }
}