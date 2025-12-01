package abstractfactory.product;

// Simplificando, todas as concretas podem ir neste pacote por agora
public class ModernChair implements Chair {
    @Override
    public void sitOn() {
        System.out.println("Sentando em uma Cadeira Moderna.");
    }
    @Override
    public String getType() {
        return "Cadeira Moderna";
    }
}