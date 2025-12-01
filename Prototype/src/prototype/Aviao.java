package prototype;

// Classe concreta para Avião.
public class Aviao extends Transporte {
    
    public int numTurbinas;
    
    // Construtor padrão
    public Aviao() { }
    
    // Construtor de clonagem
    public Aviao(Aviao origem) {
        super(origem); // Chama o construtor da superclasse para copiar atributos básicos
        if (origem != null) {
            this.numTurbinas = origem.numTurbinas; // Copia atributo específico
        }
    }

    @Override
    public Transporte clone() {
        // Retorna uma nova instância de Aviao, usando o construtor de clonagem
        // para copiar os dados do objeto atual (this).
        return new Aviao(this);
    }

    @Override
    public String getTipo() {
        return "Avião";
    }

    @Override
    public String toString() {
        return super.toString() + ", Turbinas: " + numTurbinas;
    }
}