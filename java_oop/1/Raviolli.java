public class Raviolli extends Product {
    private int count;
    public Raviolli(int price, String name, int count) {
        super(price, name);
        this.count = count;
    }
    @Override
    public String toString() {
        
        return super.toString()  +" " + count;
    }
    
}