package abstractfactory.factory;

import abstractfactory.product.Chair;
import abstractfactory.product.Sofa;
import abstractfactory.product.CoffeeTable;
import abstractfactory.product.ModernChair; // Importa o produto concreto
import abstractfactory.product.ModernSofa;
import abstractfactory.product.ModernCoffeeTable;

public class ModernFurnitureFactory implements FurnitureFactory {
    @Override
    public Chair createChair() {
        return new ModernChair();
    }

    @Override
    public Sofa createSofa() {
        return new ModernSofa();
    }

    @Override
    public CoffeeTable createCoffeeTable() {
        return new ModernCoffeeTable();
    }
}