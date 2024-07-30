public class Ingredient {
    private String name;
    private double fat;
    private double calories;
    private double protein;

    public Ingredient(String name, double fat, double calories, double protein) {
        this.name = name;
        this.fat = fat;
        this.calories = calories;
        this.protein = protein;
    }

    public String getName() {
        return name;
    }

    public double getFats() {
        return fat;
    }

    public double getCalories() {
        return calories;
    }

    public double getProtein() {
        return protein;
    }
}
