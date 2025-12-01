package abstractfactory.product;

public class ModernSofa implements Sofa {

    @Override
    public void lieOn() {
        System.out.println("Deitando em um Sofá Moderno: design minimalista e confortável.");
    }

    @Override
    public String getType() {
        return "Sofá Moderno";
    }
}