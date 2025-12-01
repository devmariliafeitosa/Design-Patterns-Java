package factorymethod.transport;

/**
 * Produto Concreto 1: Implementação do transporte por caminhão.
 * Implementa a interface Transport.
 */
public class Truck implements Transport {
    
    /**
     * Implementação do método de entrega para caminhões.
     */
    @Override
    public void deliver() {
        System.out.println("🚚 Entrega por terra em uma caixa.");
    }
}