import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Day {
    private Date date;
    private List<DishQuantity> dishQuantities;

    public Day(Date date) {
        this.date = date;
        this.dishQuantities = new ArrayList<>();
    }

    public void addDish(Dish dish, double quantity) {
        this.dishQuantities.add(new DishQuantity(dish, quantity));
    }

    public double calculateTotalCalories() {
        double totalCalories = 0;
        for (DishQuantity dq : dishQuantities) {
            totalCalories += dq.getDish().calculateTotalCalories() * dq.getQuantity();
        }
        return totalCalories;
    }

    public double calculateTotalFat() {
        double totalFat = 0;
        for (DishQuantity dq : dishQuantities) {
            totalFat += dq.getDish().calculateTotalFat() * dq.getQuantity();
        }
        return totalFat;
    }

    public double calculateTotalProtein() {
        double totalProtein = 0;
        for (DishQuantity dq : dishQuantities) {
            totalProtein += dq.getDish().calculateTotalProtein() * dq.getQuantity();
        }
        return totalProtein;
    }

    public Date getDate() {
        return date;
    }

    private static class DishQuantity {
        private Dish dish;
        private double quantity;

        public DishQuantity(Dish dish, double quantity) {
            this.dish = dish;
            this.quantity = quantity;
        }

        public Dish getDish() {
            return dish;
        }

        public double getQuantity() {
            return quantity;
        }
    }
}
