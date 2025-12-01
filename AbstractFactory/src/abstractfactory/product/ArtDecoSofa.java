package abstractfactory.product;

public class ArtDecoSofa implements Sofa {

    @Override
    public void lieOn() {
        System.out.println("Deitando em um Sofá Art Deco: simétrico, com linhas limpas e tecidos luxuosos.");
    }

    @Override
    public String getType() {
        return "Sofá Art Deco";
    }
}