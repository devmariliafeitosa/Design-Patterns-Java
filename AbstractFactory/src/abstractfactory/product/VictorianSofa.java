package abstractfactory.product;

public class VictorianSofa implements Sofa {

    @Override
    public void lieOn() {
        System.out.println("Deitando em um Sofá Vitoriano: com ricos detalhes em madeira e veludo.");
    }

    @Override
    public String getType() {
        return "Sofá Vitoriano";
    }
}