package abstractfactory.product;

public class ArtDecoChair implements Chair {

    @Override
    public void sitOn() {
        System.out.println("Sentando em uma Cadeira Art Deco: design angular e materiais exóticos.");
    }

    @Override
    public String getType() {
        return "Cadeira Art Deco";
    }
}