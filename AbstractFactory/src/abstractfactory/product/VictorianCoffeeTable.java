package abstractfactory.product;

public class VictorianCoffeeTable implements CoffeeTable {

    @Override
    public void putCoffee() {
        System.out.println("Colocando café em uma Mesa de Centro Vitoriana: base esculpida e acabamento clássico.");
    }

    @Override
    public String getType() {
        return "Mesa de Centro Vitoriana";
    }
}
