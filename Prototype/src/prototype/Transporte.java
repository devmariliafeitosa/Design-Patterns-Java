package prototype;

// A superclasse abstrata que implementa Cloneable para habilitar o Prototype.
public abstract class Transporte implements Cloneable {

    public String modelo;
    public String cor;
    public int ano;
    public double precoBase;
    
    // Construtor padrão
    public Transporte() { }

    // Construtor para clonagem: recebe um objeto Transporte para copiar dados
    public Transporte(Transporte origem) {
        if (origem != null) {
            this.modelo = origem.modelo;
            this.cor = origem.cor;
            this.ano = origem.ano;
            this.precoBase = origem.precoBase;
        }
    }

    // Método abstrato para clonar. Cada subclasse deve implementar sua lógica específica.
    public abstract Transporte clone();
    
    // Método abstrato para exibir detalhes específicos.
    public abstract String getTipo();

    @Override
    public String toString() {
        return "Tipo: " + getTipo() + 
               ", Modelo: " + modelo + 
               ", Cor: " + cor + 
               ", Ano: " + ano + 
               ", Preço Base: R$" + String.format("%.2f", precoBase);
    }
}