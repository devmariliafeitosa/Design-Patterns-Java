package abstractfactory.product;

public class ArtDecoCoffeeTable implements CoffeeTable {

    @Override
    public void putCoffee() {
        System.out.println("Colocando café em uma Mesa de Centro Art Deco: tampo espelhado e base em cromo.");
    }

    @Override
    public String getType() {
        return "Mesa de Centro Art Deco";
    }
}