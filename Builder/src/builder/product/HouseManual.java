package builder.product;

import java.util.ArrayList; // <--- ADICIONAR ESTA LINHA
import java.util.List; // <--- ADICIONAR ESTA LINHA

// Um produto relacionado que armazena informações sobre as partes da casa.
public class HouseManual {
    // Agora o Java reconhece List e ArrayList
    private List<String> instructions = new ArrayList<>();

    public void addInstruction(String instruction) {
        this.instructions.add(instruction);
    }

    public void printManual() {
        System.out.println("\n--- Manual de Instruções da Casa ---");
        for (String instruction : instructions) {
            System.out.println("Instrução: " + instruction);
        }
        System.out.println("----------------------------------");
    }
}