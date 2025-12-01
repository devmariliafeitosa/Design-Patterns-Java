package abstractfactory.product;

public class VictorianChair implements Chair {

    @Override
    public void sitOn() {
        System.out.println("Sentando em uma Cadeira Vitoriana: estofado detalhado com encosto alto.");
    }

    @Override
    public String getType() {
        return "Cadeira Vitoriana";
    }
}