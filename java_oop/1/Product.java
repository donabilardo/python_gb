public class Product {
    private int price;
    private String name;

    public Product(int price, String name) {
        this.price = price;
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public int getPrice() {
        return price;
    }
    
    @Override
    public String toString() {
        return String.format("product %s, price %d", name, price);
    }

    

}