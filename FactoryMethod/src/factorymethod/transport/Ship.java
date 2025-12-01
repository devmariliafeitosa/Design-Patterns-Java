package factorymethod.transport;

/**
 * Produto Concreto 2: Implementação do transporte por navio.
 */
public class Ship implements Transport {
    @Override
    public void deliver() {
        System.out.println("🚢 Entrega por mar em um contêiner.");
    }
}