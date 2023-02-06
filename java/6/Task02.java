package hw06;

import java.util.HashSet;
import java.util.Set;

public class Task02 {
    public static void main(String[] args) {
        Set<Laptop> laptops = getLaptopSet(100);
        printLaptops(laptops);
    }

    /** Creates a set of Laptops.
    * @param listSize   a set size
    * @return           a set of Laptop Objects
    */
    public static Set<Laptop> getLaptopSet(int listSize) {
        Set<Laptop> laptops = new HashSet<>();
        for (int i = 0; i < listSize; i++) {
            laptops.add(Laptop.generateLaptop());
        }
        return laptops;
    }

    /** Prints to a console a set of Laptops.
    * @param laptops    a set of Laptops
    */
    public static void printLaptops(Set<Laptop> laptops) {
        System.out.println(resultMsg);
        int i = 1;
        for (Laptop laptop : laptops) {
            System.out.printf("%d. %s\n", i, laptop);
            i++;
        }
    }

    public static final String resultMsg = "\nПеречень ноутбуков:\n";
}