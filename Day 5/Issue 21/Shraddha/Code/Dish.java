import java.util.ArrayList;
import java.util.List;

public class Dish {
    private String name;
    private List<IngredientQuantity> ingredientQuantities;

    public Dish(String name) {
        this.name = name;
        this.ingredientQuantities = new ArrayList<>();
    }

    public void addIngredient(Ingredient ingredient, double quantity) {
        this.ingredientQuantities.add(new IngredientQuantity(ingredient, quantity));
    }

    public double calculateTotalCalories() {
        double totalCalories = 0;
        for (IngredientQuantity iq : ingredientQuantities) {
            totalCalories += iq.getIngredient().getCalories() * iq.getQuantity();
        }
        return totalCalories;
    }

    public double calculateTotalFat() {
        double totalFat = 0;
        for (IngredientQuantity iq : ingredientQuantities) {
            totalFat += iq.getIngredient().getFats()* iq.getQuantity();
        }
        return totalFat;
    }

    public double calculateTotalProtein() {
        double totalProtein = 0;
        for (IngredientQuantity iq : ingredientQuantities) {
            totalProtein += iq.getIngredient().getProtein() * iq.getQuantity();
        }
        return totalProtein;
    }

    public String getName() {
        return name;
    }

    private static class IngredientQuantity {
        private Ingredient ingredient;
        private double quantity;

        public IngredientQuantity(Ingredient ingredient, double quantity) {
            this.ingredient = ingredient;
            this.quantity = quantity;
        }

        public Ingredient getIngredient() {
            return ingredient;
        }

        public double getQuantity() {
            return quantity;
        }
    }
}
