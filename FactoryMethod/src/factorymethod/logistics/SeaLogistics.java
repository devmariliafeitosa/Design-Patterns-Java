package factorymethod.logistics;

import factorymethod.transport.Transport;
import factorymethod.transport.Ship;

/**
 * Criador Concreto 2: Sobrescreve o método fábrica para retornar um Navio.
 */
public class SeaLogistics extends Logistics {
    @Override
    protected Transport createTransport() {
        // Retorna o produto concreto Ship
        return new Ship();
    }
}