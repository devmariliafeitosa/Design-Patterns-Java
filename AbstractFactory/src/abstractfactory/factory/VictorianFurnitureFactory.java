    package abstractfactory.factory;

import abstractfactory.product.Chair;
import abstractfactory.product.Sofa;
import abstractfactory.product.CoffeeTable;
import abstractfactory.product.VictorianChair; // Importa produtos concretos
import abstractfactory.product.VictorianSofa;
import abstractfactory.product.VictorianCoffeeTable;

public class VictorianFurnitureFactory implements FurnitureFactory {

    @Override
    public Chair createChair() {
        // Retorna o produto concreto Vitoriano
        return new VictorianChair();
    }

    @Override
    public Sofa createSofa() {
        // Retorna o produto concreto Vitoriano
        return new VictorianSofa();
    }

    @Override
    public CoffeeTable createCoffeeTable() {
        // Retorna o produto concreto Vitoriano
        return new VictorianCoffeeTable();
    }
}