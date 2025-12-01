package factorymethod.logistics;

import factorymethod.transport.Transport;
import factorymethod.transport.Truck;

/**
 * Criador Concreto 1: Sobrescreve o método fábrica para retornar um Caminhão.
 */
public class RoadLogistics extends Logistics {
    @Override
    protected Transport createTransport() {
        // Retorna o produto concreto Truck
        return new Truck();
    }
}