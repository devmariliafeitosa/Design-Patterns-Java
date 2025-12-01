package abstractfactory.client;

import abstractfactory.factory.FurnitureFactory;
import abstractfactory.factory.ModernFurnitureFactory;
import abstractfactory.factory.VictorianFurnitureFactory;
import abstractfactory.factory.ArtDecoFurnitureFactory; // Importa a nova fábrica

public class Main {
    public static void main(String[] args) {
        // 1. Defina o estilo (configuração da aplicação)
        String style = "ArtDeco"; 
        
        // TESTE: Mude para "Modern" ou "Victorian" para testar
        
        FurnitureFactory factory;

        // 2. Seleção da fábrica concreta dependendo da configuração
        if (style.equalsIgnoreCase("Modern")) {
            factory = new ModernFurnitureFactory();
        } else if (style.equalsIgnoreCase("Victorian")) {
            factory = new VictorianFurnitureFactory();
        } else if (style.equalsIgnoreCase("ArtDeco")) {
            // A fábrica que acabamos de criar!
            factory = new ArtDecoFurnitureFactory();
        } else {
            System.out.println("Estilo de móvel desconhecido: " + style + ". Usando Moderno como padrão.");
            factory = new ModernFurnitureFactory();
        }

        // 3. Passa o objeto de fábrica (abstrata) para o código cliente
        // O cliente só conhece a interface FurnitureFactory.
        FurnitureApplication app = new FurnitureApplication(factory);
        
        // 4. Executa o cliente para criar e exibir os móveis
        app.displayFurniture();
    }
}