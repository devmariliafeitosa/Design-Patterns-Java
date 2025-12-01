package factorymethod.logistics;

import factorymethod.transport.Transport;

/**
 * Criador Abstrato: Declara o método fábrica, que deve retornar um objeto do tipo Transport.
 * Também contém alguma lógica central (planDelivery) que é independente do tipo de transporte.
 */
public abstract class Logistics {
    
    // O método fábrica. Subclasses o sobrescreverão para retornar produtos concretos diferentes.
    protected abstract Transport createTransport();
    
    // Lógica principal do criador. Usa o método fábrica para obter um objeto produto 
    // e então trabalha com ele, independentemente do tipo concreto.
    public void planDelivery() {
        // 1. O método fábrica é chamado (polimorfismo).
        Transport transport = createTransport();
        
        // 2. A lógica de negócio usa o produto (Transport), mas só conhece a interface.
        System.out.println("--- Planejamento de Entrega ---");
        System.out.println("A logística principal está preparando a entrega...");
        transport.deliver();
        System.out.println("---------------------------------");
    }
}