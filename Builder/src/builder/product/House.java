package builder.product;

import java.util.ArrayList;
import java.util.List;

// O Produto (House) é o objeto complexo que está sendo construído.
public class House {
    private List<String> parts = new ArrayList<>();

    // Adiciona uma "parte" à casa (parede, porta, telhado, etc.)
    public void add(String part) {
        this.parts.add(part);
    }

    public void show() {
        System.out.println("--- Configuração da Casa ---");
        System.out.println("Partes construídas: " + parts.size());
        for (String part : parts) {
            System.out.println("  - " + part);
        }
        System.out.println("--------------------------");
    }
}