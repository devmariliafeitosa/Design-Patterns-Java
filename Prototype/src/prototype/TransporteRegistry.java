package prototype;

import java.util.HashMap;
import java.util.Map;

// O Registro de Protótipos armazena objetos pré-configurados para clonagem.
public class TransporteRegistry {
    
    private Map<String, Transporte> itens = new HashMap<>();

    // Adiciona um protótipo ao registro
    public void addItem(String id, Transporte prototipo) {
        itens.put(id, prototipo);
    }

    // Retorna uma CÓPIA (clone) do protótipo solicitado pelo ID.
    // O retorno é o clone, não o objeto original.
    public Transporte getClone(String id) {
        Transporte prototipo = itens.get(id);
        if (prototipo == null) {
            System.out.println("Protótipo com ID '" + id + "' não encontrado.");
            return null;
        }
        // DELEGA a clonagem ao próprio objeto
        return prototipo.clone();
    }
}