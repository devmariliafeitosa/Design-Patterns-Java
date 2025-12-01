package factorymethod.client;

import factorymethod.logistics.Logistics;
import factorymethod.logistics.RoadLogistics;
import factorymethod.logistics.SeaLogistics;

/**
 * Cliente: O cliente usa a interface do Criador (Logistics) e não se importa com 
 * qual Criador Concreto ou Produto Concreto está sendo usado.
 */
public class Main {
    
    public static void main(String[] args) {
        // Exemplo 1: Necessidade de logística terrestre
        Logistics roadLogistics = new RoadLogistics();
        System.out.println("== Logística 1: Terrestre ==");
        roadLogistics.planDelivery(); 
        
        System.out.println("\n");
        
        // Exemplo 2: Necessidade de logística marítima
        Logistics seaLogistics = new SeaLogistics();
        System.out.println("== Logística 2: Marítima ==");
        seaLogistics.planDelivery();
    }
}