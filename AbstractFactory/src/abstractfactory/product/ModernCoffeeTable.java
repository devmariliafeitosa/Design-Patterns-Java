package abstractfactory.product;

public class ModernCoffeeTable implements CoffeeTable {

    @Override
    public void putCoffee() {
        System.out.println("Colocando café em uma Mesa de Centro Moderna: superfície de vidro elegante.");
    }

    @Override
    public String getType() {
        return "Mesa de Centro Moderna";
    }
}