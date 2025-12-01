package abstractfactory.factory;

import abstractfactory.product.Chair;
import abstractfactory.product.Sofa;
import abstractfactory.product.CoffeeTable;
import abstractfactory.product.ArtDecoChair; // Importa produtos concretos Art Deco
import abstractfactory.product.ArtDecoSofa;
import abstractfactory.product.ArtDecoCoffeeTable;

public class ArtDecoFurnitureFactory implements FurnitureFactory {

    @Override
    public Chair createChair() {
        // Retorna o produto concreto Art Deco
        return new ArtDecoChair();
    }

    @Override
    public Sofa createSofa() {
        // Retorna o produto concreto Art Deco
        return new ArtDecoSofa();
    }

    @Override
    public CoffeeTable createCoffeeTable() {
        // Retorna o produto concreto Art Deco
        return new ArtDecoCoffeeTable();
    }
}