package prototype;

// Classe concreta para Carro.
public class Carro extends Transporte {
    
    public int numPortas;
    
    // Construtor padrão
    public Carro() { }

    // Construtor de clonagem
    public Carro(Carro origem) {
        super(origem); // Chama o construtor da superclasse para copiar atributos básicos
        if (origem != null) {
            this.numPortas = origem.numPortas; // Copia atributo específico
        }
    }

    @Override
    public Transporte clone() {
        // Retorna uma nova instância de Carro, usando o construtor de clonagem
        // para copiar os dados do objeto atual (this).
        return new Carro(this);
    }

    @Override
    public String getTipo() {
        return "Carro";
    }

    @Override
    public String toString() {
        return super.toString() + ", Portas: " + numPortas;
    }
}