package prototype;

public class Demo {

    public static void main(String[] args) {
        
        System.out.println("--- 1. Demonstração do Registro de Protótipos ---");
        
        // 1. Configurando protótipos e adicionando ao Registro
        TransporteRegistry registro = new TransporteRegistry();
        
        // Protótipo 1: Carro popular vermelho
        Carro prototipoCarro1 = new Carro();
        prototipoCarro1.modelo = "Onix";
        prototipoCarro1.cor = "Vermelho";
        prototipoCarro1.ano = 2024;
        prototipoCarro1.precoBase = 70000.00;
        prototipoCarro1.numPortas = 4;
        registro.addItem("popular_vermelho", prototipoCarro1);
        
        // Protótipo 2: Avião comercial a jato
        Aviao prototipoAviao1 = new Aviao();
        prototipoAviao1.modelo = "Boeing 737";
        prototipoAviao1.cor = "Branco";
        prototipoAviao1.ano = 2020;
        prototipoAviao1.precoBase = 150000000.00;
        prototipoAviao1.numTurbinas = 2;
        registro.addItem("jato_comercial", prototipoAviao1);
        
        System.out.println("Protótipos configurados e no registro.");
        
        // 2. Criando novos objetos via clonagem do registro
        
        // Criando um novo Carro a partir do protótipo
        Carro novoCarro = (Carro) registro.getClone("popular_vermelho");
        // Altera APENAS o clone, o protótipo original permanece inalterado
        if (novoCarro != null) {
            novoCarro.cor = "Azul"; 
            novoCarro.precoBase = novoCarro.precoBase * 1.05; // Adiciona um upgrade
            System.out.println("\nCópia (Clone) de Carro Modificado:");
            System.out.println(novoCarro);
        }

        // Criando um novo Avião a partir do protótipo
        Aviao novoAviao = (Aviao) registro.getClone("jato_comercial");
        if (novoAviao != null) {
            novoAviao.modelo = "Airbus A320"; // Muda o modelo
            System.out.println("\nCópia (Clone) de Avião Modificado:");
            System.out.println(novoAviao);
        }
        
        // Tentativa de obter um ID inexistente
        registro.getClone("caminhao_carga");

        System.out.println("\n--- 2. Clonagem Direta (sem o registro) ---");
        
        // 3. Demonstração da clonagem direta
        Carro carroOriginal = new Carro();
        carroOriginal.modelo = "Fusca";
        carroOriginal.cor = "Verde";
        carroOriginal.ano = 1970;
        carroOriginal.precoBase = 15000.00;
        carroOriginal.numPortas = 2;
        
        // O cliente clona o objeto diretamente, sem saber sua classe concreta
        Transporte carroCopia = carroOriginal.clone(); 
        
        System.out.println("Carro Original: " + carroOriginal);
        
        // Modifica a cópia
        carroCopia.cor = "Amarelo";
        carroCopia.precoBase = 16500.00;
        
        System.out.println("Carro Cópia (Clone): " + carroCopia);
        System.out.println("\nO original não foi alterado: " + carroOriginal);
    }
}