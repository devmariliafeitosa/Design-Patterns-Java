package abstractfactory.client;

import abstractfactory.factory.FurnitureFactory;
import abstractfactory.product.Chair;
import abstractfactory.product.Sofa;
import abstractfactory.product.CoffeeTable;

// Esta é a classe cliente. Ela só conhece as interfaces abstratas.
public class FurnitureApplication {
    private Chair chair;
    private Sofa sofa;
    private CoffeeTable table;

    // O cliente recebe a Fábrica Abstrata no construtor.
    public FurnitureApplication(FurnitureFactory factory) {
        // Usa a fábrica para criar produtos (sem saber se são Modern, Victorian ou ArtDeco)
        this.chair = factory.createChair(); 
        this.sofa = factory.createSofa();   
        this.table = factory.createCoffeeTable();
    }

    public void displayFurniture() {
        System.out.println("--- Novo Conjunto de Móveis Criado ---");
        
        // Chamadas de métodos dos produtos
        System.out.println("Cadeira: " + chair.getType());
        chair.sitOn();
        
        System.out.println("Sofá: " + sofa.getType());
        sofa.lieOn();
        
        System.out.println("Mesa: " + table.getType());
        table.putCoffee();
        
        System.out.println("--- Todos os móveis combinam! ---");
    }
}