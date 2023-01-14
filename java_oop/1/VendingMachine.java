import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class VendingMachine {
    private List<Product> products = new ArrayList<>();

    public VendingMachine(List<Product> products) {
        this.products = products;
    }

    public List<Product> getProducts() {
        return products;
    }

    public VendingMachine() {

    }

    public VendingMachine(Product product) {
        this(new ArrayList<>(Arrays.asList(product)));
    }

    public void addProduct(Product product) {
        products.add(product);
    }

    public Product find(String name){
        for (Product product : products) {
            if (product.getName().contains(name)){
                return product;
            }   
        }
     return null;   
    }
}