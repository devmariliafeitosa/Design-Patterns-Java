package abstractfactory.factory;

import abstractfactory.product.Chair;
import abstractfactory.product.Sofa;
import abstractfactory.product.CoffeeTable;

public interface FurnitureFactory {
    Chair createChair();
    Sofa createSofa();
    CoffeeTable createCoffeeTable();
}